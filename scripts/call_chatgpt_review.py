#!/usr/bin/env python3
"""
ELYSIUM — Generic ChatGPT API Prose Reviewer
Handles initial review and final review after revision.

Usage:
  # Initial review
  python3 scripts/call_chatgpt_review.py --module OPN-014 \
    --prose BOOK/_fcs/api_outputs/..._OPN014_CLAUDE_RAW.md \
    --brief BOOK/manuscript/01_opening/writing_briefs/OPN-014_writing_brief.md

  # Final review after revision
  python3 scripts/call_chatgpt_review.py --module OPN-014 --final \
    --prose BOOK/_fcs/api_outputs/..._OPN014_CLAUDE_REVISED.md \
    --brief BOOK/manuscript/01_opening/writing_briefs/OPN-014_writing_brief.md
"""
import argparse
import os
import sys
import requests

# Import LLM Output Guard for completion validation
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPT_DIR not in sys.path:
    sys.path.insert(0, _SCRIPT_DIR)
try:
    from llm_output_guard import validate_llm_output_completion, build_llm_metadata
    _GUARD_AVAILABLE = True
except ImportError:
    _GUARD_AVAILABLE = False

CHATGPT_MODEL = "gpt-4o-2024-08-06"
CHATGPT_MAX_TOKENS = 500

# Key resolution: env var first, then .user_env file, then hardcoded fallback
def get_openai_key():
    key = os.environ.get("OPENAI_API_KEY", "")
    if not key:
        user_env = os.path.expanduser("~/.user_env")
        if os.path.exists(user_env):
            for line in open(user_env):
                if line.startswith("OPENAI_API_KEY="):
                    key = line.strip().split("=", 1)[1].strip('"').strip("'")
                    break
    if not key:
        raise ValueError("OPENAI_API_KEY not found. Set via env var or ~/.user_env")
    return key

def read_prose_body(path):
    content = open(path).read()
    if content.startswith("---"):
        parts = content.split("---", 2)
        return parts[2].strip() if len(parts) >= 3 else content
    return content

def main():
    parser = argparse.ArgumentParser(description="ELYSIUM ChatGPT API Prose Reviewer")
    parser.add_argument("--module", required=True, help="Module ID, e.g. OPN-014")
    parser.add_argument("--prose", required=True, help="Path to prose markdown file")
    parser.add_argument("--brief", required=True, help="Path to writing brief markdown file")
    parser.add_argument("--final", action="store_true", help="Final review mode (after revision)")
    parser.add_argument("--output_dir", default="BOOK/_fcs/api_outputs", help="Output directory")
    parser.add_argument("--phase", default="III-1A-S4", help="Phase ID for output filename")
    parser.add_argument("--max_tokens", type=int, default=CHATGPT_MAX_TOKENS,
                        help=f"Max output tokens for ChatGPT review (default: {CHATGPT_MAX_TOKENS})")
    args = parser.parse_args()

    module_id = args.module
    phase_slug = args.phase.replace("-", "_").replace("/", "_")
    module_slug = module_id.replace("-", "")
    suffix = "CHATGPT_FINAL_REVIEW" if args.final else "CHATGPT_REVIEW"
    label = "FINAL REVIEW" if args.final else "REVIEW"

    prose = read_prose_body(args.prose)
    wc = len(prose.split())

    if not os.path.exists(args.brief):
        print(f"ERROR: Brief not found: {args.brief}"); exit(1)
    brief = open(args.brief).read()

    review_prompt = f"""Review ELYSIUM {module_id} prose ({wc} words) against its writing brief.

WRITING BRIEF:
{brief}

PROSE:
---
{prose}
---

EVALUATE:
1. Brief fidelity (purpose, beats, tone, word target)
2. Structural fidelity (movement role, reader transition)
3. Forbidden moves (none should appear)
4. ELYSIUM voice (civilizational, lucid, literary but not ornate, rigorous but accessible)
5. Continuity with previous module
6. Readiness for DRAFT_0

Respond EXACTLY:
DECISION: [PASS / REVISE / FAIL]
WORD_COUNT: {wc}
FORBIDDEN_MOVES_FOUND: [list or NONE]
ISSUES: [list or NONE]
REVISIONS_REQUIRED: [specific instructions or NONE]
SUMMARY: [1-2 sentences]"""

    print(f"[{label}] {module_id} ({wc}w)", flush=True)

    max_tokens = args.max_tokens
    r = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {get_openai_key()}", "Content-Type": "application/json"},
        json={"model": CHATGPT_MODEL,
              "messages": [{"role": "user", "content": review_prompt}],
              "max_tokens": max_tokens, "temperature": 0.3},
        timeout=120
    )
    r.raise_for_status()
    data = r.json()
    review = data["choices"][0]["message"]["content"]
    in_tok = data["usage"]["prompt_tokens"]
    out_tok = data["usage"]["completion_tokens"]
    finish_reason = data["choices"][0].get("finish_reason", "")

    print(f"Tokens: {in_tok} in / {out_tok} out | finish_reason={finish_reason}", flush=True)

    # Run completion validation on the review output
    review_completion_status = "UNKNOWN"
    if _GUARD_AVAILABLE:
        meta = build_llm_metadata(
            provider="openai", model=CHATGPT_MODEL,
            max_tokens=max_tokens, input_tokens=in_tok, output_tokens=out_tok,
            stop_reason=finish_reason, script="call_chatgpt_review.py",
        )
        validation = validate_llm_output_completion(review, meta, is_prose=False)
        review_completion_status = validation["status"]
        if review_completion_status != "COMPLETE":
            print(f"[GUARD] WARNING: review completion_status={review_completion_status}", flush=True)
            for reason in validation.get("reasons", []):
                print(f"[GUARD]   - {reason}", flush=True)
        else:
            print(f"[GUARD] review completion_status=COMPLETE ✓", flush=True)

    print(f"\n=== {label} ===\n{review}\n=== END ===", flush=True)

    # Parse decision
    decision = "UNKNOWN"
    for line in review.splitlines():
        if line.startswith("DECISION:"):
            decision = line.replace("DECISION:", "").strip()
            break
    print(f"DECISION={decision}", flush=True)

    os.makedirs(args.output_dir, exist_ok=True)
    filename = f"PHASE_{phase_slug}_{module_slug}_{suffix}.md"
    path = os.path.join(args.output_dir, filename)
    open(path, "w").write(
        f"---\nid: PHASE_{phase_slug}_{module_slug}_{suffix}\n"
        f"module_id: {module_id}\ndecision: {decision}\n"
        f"input_tokens: {in_tok}\noutput_tokens: {out_tok}\n"
        f"finish_reason: {finish_reason}\nllm_completion_status: {review_completion_status}\n"
        f"max_tokens_requested: {max_tokens}\n---\n\n{review}"
    )
    print(f"Saved: {path}", flush=True)
    print(f"OUTPUT_PATH={path}", flush=True)

if __name__ == "__main__":
    main()
