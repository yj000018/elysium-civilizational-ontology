#!/usr/bin/env python3
"""
ELYSIUM — LLM Output Guard
Shared utility for LLM output completion validation.
Implements: LLM_OUTPUT_COMPLETION_AND_SECTIONING_PROTOCOL.md

Usage (as library):
    from llm_output_guard import validate_llm_output_completion, normalize_finish_reason, build_llm_metadata

Usage (as CLI):
    python3 scripts/llm_output_guard.py --output_file path/to/output.md --provider anthropic --stop_reason end_turn
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from typing import Optional

# ── Constants ────────────────────────────────────────────────────────────────

TERMINAL_PUNCTUATION = {'.', '!', '?'}

# Endings that indicate truncation
TRUNCATION_ENDINGS = (
    ',', ':', '-', ';',
    ' and', ' or', ' but', ' the', ' a', ' an', ' of', ' in', ' to',
    ' that', ' which', ' with', ' for', ' on', ' at', ' by',
)

# Provider-specific finish reason → normalized status mapping
FINISH_REASON_MAP = {
    # Anthropic / Claude
    "end_turn":       "COMPLETE",
    "stop_sequence":  "COMPLETE",
    "max_tokens":     "TRUNCATED_MAX_TOKENS",
    "tool_use":       "TOOL_INTERRUPTED",
    # OpenAI / ChatGPT
    "stop":           "COMPLETE",
    "length":         "TRUNCATED_MAX_TOKENS",
    "content_filter": "CONTENT_FILTERED",
    "function_call":  "TOOL_INTERRUPTED",
    "tool_calls":     "TOOL_INTERRUPTED",
    # Google / Gemini
    "STOP":                    "COMPLETE",
    "MAX_TOKENS":              "TRUNCATED_MAX_TOKENS",
    "SAFETY":                  "CONTENT_FILTERED",
    "RECITATION":              "CONTENT_FILTERED",
    "FINISH_REASON_UNSPECIFIED": "UNKNOWN",
}

# Normalized completion status values
COMPLETION_STATUSES = {
    "COMPLETE",
    "TRUNCATED_MAX_TOKENS",
    "INTERRUPTED",
    "CONTENT_FILTERED",
    "TOOL_INTERRUPTED",
    "INVALID_FORMAT",
    "UNKNOWN",
}


# ── Core Functions ────────────────────────────────────────────────────────────

def normalize_finish_reason(finish_reason: Optional[str], provider: str = "") -> str:
    """
    Map provider-specific finish_reason / stop_reason to normalized llm_completion_status.
    Returns one of: COMPLETE, TRUNCATED_MAX_TOKENS, INTERRUPTED, CONTENT_FILTERED,
                    TOOL_INTERRUPTED, INVALID_FORMAT, UNKNOWN
    """
    if not finish_reason:
        return "UNKNOWN"
    normalized = FINISH_REASON_MAP.get(finish_reason.strip())
    if normalized:
        return normalized
    # Heuristic fallbacks
    fr_lower = finish_reason.lower()
    if "max" in fr_lower or "length" in fr_lower or "token" in fr_lower:
        return "TRUNCATED_MAX_TOKENS"
    if "stop" in fr_lower or "end" in fr_lower:
        return "COMPLETE"
    if "filter" in fr_lower or "safety" in fr_lower:
        return "CONTENT_FILTERED"
    if "tool" in fr_lower or "function" in fr_lower:
        return "TOOL_INTERRUPTED"
    return "UNKNOWN"


def strip_frontmatter(content: str) -> str:
    """Strip YAML frontmatter from a markdown file."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3:].strip()
    return content.strip()


def validate_llm_output_completion(
    output_text: str,
    metadata: Optional[dict] = None,
    is_prose: bool = True,
    word_target: Optional[int] = None,
    word_tolerance_pct: float = 0.25,
) -> dict:
    """
    Validate LLM output for completeness.

    Args:
        output_text: The raw output text (may include frontmatter).
        metadata: Dict with keys: stop_reason, finish_reason, output_tokens, max_tokens, provider, model
        is_prose: Whether this is prose (expects terminal punctuation).
        word_target: Expected word count target.
        word_tolerance_pct: Allowed deviation from word_target (default 25%).

    Returns:
        dict with keys:
            status: COMPLETE | TRUNCATED | INCOMPLETE | UNKNOWN
            reasons: list of reasons
            word_count: int
            terminal_char: str
            terminal_ok: bool
            finish_reason_normalized: str
            metadata_flags: list of metadata-based flags
    """
    metadata = metadata or {}
    reasons = []
    metadata_flags = []

    # Strip frontmatter for prose analysis
    prose = strip_frontmatter(output_text) if output_text.startswith("---") else output_text.strip()
    word_count = len(prose.split()) if prose else 0
    last_char = prose.rstrip()[-1] if prose.rstrip() else ""
    terminal_ok = last_char in TERMINAL_PUNCTUATION

    # ── Metadata-based checks ─────────────────────────────────────────────
    stop_reason = metadata.get("stop_reason") or metadata.get("finish_reason") or ""
    provider = metadata.get("provider", "").lower()
    output_tokens = metadata.get("output_tokens", 0)
    max_tokens = metadata.get("max_tokens", 0)

    finish_reason_normalized = normalize_finish_reason(stop_reason, provider)

    if finish_reason_normalized == "TRUNCATED_MAX_TOKENS":
        metadata_flags.append(f"stop_reason='{stop_reason}' → TRUNCATED_MAX_TOKENS")
        reasons.append(f"LLM reported max_tokens stop: {stop_reason}")

    if finish_reason_normalized in ("CONTENT_FILTERED", "TOOL_INTERRUPTED", "INTERRUPTED"):
        metadata_flags.append(f"stop_reason='{stop_reason}' → {finish_reason_normalized}")
        reasons.append(f"LLM interrupted: {finish_reason_normalized}")

    if max_tokens and output_tokens and output_tokens >= max_tokens:
        metadata_flags.append(f"output_tokens={output_tokens} >= max_tokens={max_tokens}")
        reasons.append("Output tokens hit max_tokens ceiling")

    # ── Text-based checks ─────────────────────────────────────────────────
    if not prose:
        reasons.append("Output is empty")
        return {
            "status": "INCOMPLETE",
            "reasons": reasons,
            "word_count": 0,
            "terminal_char": "",
            "terminal_ok": False,
            "finish_reason_normalized": finish_reason_normalized,
            "metadata_flags": metadata_flags,
        }

    if is_prose and not terminal_ok:
        reasons.append(f"Prose does not end with terminal punctuation (ends with {repr(last_char)})")

    # Check for truncation-indicating endings
    prose_stripped = prose.rstrip()
    for ending in TRUNCATION_ENDINGS:
        if prose_stripped.lower().endswith(ending):
            reasons.append(f"Prose ends with truncation indicator: {repr(ending)}")
            break

    # Check for explicit continuation requests in output
    continuation_patterns = [
        r"(shall|will|can) continue",
        r"due to (length|token|space|limit)",
        r"(truncated|cut off|incomplete)",
        r"(continue|proceed) (in|with) (the )?next",
        r"(rest|remainder) (of|will be)",
    ]
    for pat in continuation_patterns:
        if re.search(pat, prose[-500:], re.IGNORECASE):
            reasons.append(f"Output contains continuation indicator: pattern '{pat}'")
            break

    # Word count checks
    if word_target:
        lower_bound = word_target * (1 - word_tolerance_pct)
        upper_bound = word_target * (1 + word_tolerance_pct)
        if word_count < lower_bound:
            reasons.append(
                f"Word count {word_count} is far below target {word_target} "
                f"(>{word_tolerance_pct*100:.0f}% below)"
            )
        elif word_count > upper_bound:
            reasons.append(
                f"Word count {word_count} is far above target {word_target} "
                f"(>{word_tolerance_pct*100:.0f}% above — possible runaway)"
            )

    # ── Determine status ──────────────────────────────────────────────────
    if finish_reason_normalized == "TRUNCATED_MAX_TOKENS" or (
        max_tokens and output_tokens and output_tokens >= max_tokens
    ):
        status = "TRUNCATED"
    elif finish_reason_normalized in ("CONTENT_FILTERED", "INTERRUPTED", "TOOL_INTERRUPTED"):
        status = "INCOMPLETE"
    elif finish_reason_normalized == "UNKNOWN" and not stop_reason:
        # No metadata — rely on text checks only
        if reasons:
            status = "UNKNOWN"
        else:
            status = "COMPLETE"
    elif reasons:
        # Has text-based issues but metadata says COMPLETE
        if finish_reason_normalized == "COMPLETE":
            # Trust metadata but flag text issues
            status = "COMPLETE"  # Downgrade to INCOMPLETE if prose terminal check fails
            if is_prose and not terminal_ok:
                status = "INCOMPLETE"
        else:
            status = "INCOMPLETE"
    else:
        status = "COMPLETE"

    return {
        "status": status,
        "reasons": reasons,
        "word_count": word_count,
        "terminal_char": last_char,
        "terminal_ok": terminal_ok,
        "finish_reason_normalized": finish_reason_normalized,
        "metadata_flags": metadata_flags,
    }


def build_llm_metadata(
    provider: str,
    model: str,
    max_tokens: int,
    input_tokens: int,
    output_tokens: int,
    stop_reason: str,
    script: str = "",
    output_file: str = "",
    timestamp: Optional[str] = None,
) -> dict:
    """Build a standardized LLM metadata dict for logging and validation."""
    return {
        "provider": provider,
        "model": model,
        "max_tokens": max_tokens,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "stop_reason": stop_reason,
        "finish_reason": stop_reason,  # alias
        "script": script,
        "output_file": output_file,
        "timestamp": timestamp or datetime.now(timezone.utc).isoformat(),
        "llm_completion_status": normalize_finish_reason(stop_reason, provider),
    }


def format_completion_block(metadata: dict, validation: dict) -> str:
    """Format a human-readable LLM completion block for reports."""
    lines = [
        "LLM completion:",
        f"  provider: {metadata.get('provider', 'unknown')}",
        f"  model: {metadata.get('model', 'unknown')}",
        f"  max_tokens: {metadata.get('max_tokens', 'unknown')}",
        f"  output_tokens: {metadata.get('output_tokens', 'unknown')}",
        f"  stop_reason: {metadata.get('stop_reason', 'unknown')}",
        f"  completion_status: {validation.get('finish_reason_normalized', 'UNKNOWN')}",
        f"  word_count: {validation.get('word_count', 0)}",
        f"  terminal_punctuation: {'PASS' if validation.get('terminal_ok') else 'FAIL'}",
        f"  validation_status: {validation.get('status', 'UNKNOWN')}",
    ]
    if validation.get("reasons"):
        lines.append(f"  issues: {'; '.join(validation['reasons'])}")
    return "\n".join(lines)


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="ELYSIUM LLM Output Guard — validate output completion")
    parser.add_argument("--output_file", required=True, help="Path to LLM output file to validate")
    parser.add_argument("--provider", default="", help="Provider: anthropic, openai, google, etc.")
    parser.add_argument("--model", default="", help="Model name")
    parser.add_argument("--stop_reason", default="", help="stop_reason / finish_reason from API")
    parser.add_argument("--output_tokens", type=int, default=0, help="Output token count")
    parser.add_argument("--max_tokens", type=int, default=0, help="Max tokens requested")
    parser.add_argument("--word_target", type=int, default=0, help="Expected word count target")
    parser.add_argument("--no_prose", action="store_true", help="Not prose (skip terminal punctuation check)")
    parser.add_argument("--json", action="store_true", dest="json_out", help="Output as JSON")
    args = parser.parse_args()

    if not os.path.exists(args.output_file):
        print(f"ERROR: File not found: {args.output_file}")
        sys.exit(1)

    content = open(args.output_file, encoding="utf-8").read()
    metadata = build_llm_metadata(
        provider=args.provider,
        model=args.model,
        max_tokens=args.max_tokens,
        input_tokens=0,
        output_tokens=args.output_tokens,
        stop_reason=args.stop_reason,
        output_file=args.output_file,
    )
    validation = validate_llm_output_completion(
        output_text=content,
        metadata=metadata,
        is_prose=not args.no_prose,
        word_target=args.word_target or None,
    )

    if args.json_out:
        print(json.dumps({**metadata, **validation}, indent=2))
    else:
        print(f"\n=== LLM OUTPUT GUARD ===")
        print(f"File: {args.output_file}")
        print(format_completion_block(metadata, validation))
        print(f"\nSTATUS: {validation['status']}")
        if validation["reasons"]:
            print("REASONS:")
            for r in validation["reasons"]:
                print(f"  - {r}")
        print("=== END ===")

    # Exit code: 0 = COMPLETE, 1 = issues found
    sys.exit(0 if validation["status"] == "COMPLETE" else 1)


if __name__ == "__main__":
    main()
