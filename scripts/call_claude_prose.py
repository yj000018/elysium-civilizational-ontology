#!/usr/bin/env python3
"""
ELYSIUM — Generic Claude API Prose Generator
Handles all modes: initial prose, revision, compression.

Usage:
  # Initial prose
  python3 scripts/call_claude_prose.py --module OPN-014 --context_pack BOOK/_fcs/context_packs/..._OPN014_CONTEXT_PACK.md

  # Revision (after ChatGPT REVISE decision)
  python3 scripts/call_claude_prose.py --module OPN-014 --context_pack BOOK/_fcs/context_packs/..._OPN014_CONTEXT_PACK.md \
    --revision --prose BOOK/_fcs/api_outputs/..._OPN014_CLAUDE_RAW.md \
    --revision_instructions "Trim to 900 words. Strengthen closing bridge."

  # Compression only (trim word count)
  python3 scripts/call_claude_prose.py --module OPN-014 \
    --compress --prose BOOK/_fcs/api_outputs/..._OPN014_CLAUDE_RAW.md \
    --target_words 900
"""
import argparse
import os
import anthropic

# Key resolution: env var first, then .user_env file, then hardcoded fallback
def get_claude_key():
    key = os.environ.get("CLAUDE_API_KEY", "")
    if not key:
        user_env = os.path.expanduser("~/.user_env")
        if os.path.exists(user_env):
            for line in open(user_env):
                if line.startswith("CLAUDE_API_KEY="):
                    key = line.strip().split("=", 1)[1].strip('"').strip("'")
                    break
    if not key:
        raise ValueError("CLAUDE_API_KEY not found. Set via env var or ~/.user_env")
    return key

SYSTEM_PROMPT = """You are the prose writer for ELYSIUM, a civilizational ontology and transition map.
Voice: civilizational, lucid, literary but not ornate, rigorous but accessible. English only.
No headers, no bullet points in prose. Pure literary-diagnostic paragraphs.
Output ONLY the prose. No title, no preamble, no commentary."""

def read_prose_body(path):
    """Read a markdown file and strip YAML frontmatter."""
    content = open(path).read()
    if content.startswith("---"):
        parts = content.split("---", 2)
        return parts[2].strip() if len(parts) >= 3 else content
    return content

def save_output(output_dir, phase_slug, module_slug, suffix, module_id, prose, input_tokens, output_tokens):
    os.makedirs(output_dir, exist_ok=True)
    wc = len(prose.split())
    filename = f"PHASE_{phase_slug}_{module_slug}_CLAUDE_{suffix}.md"
    path = os.path.join(output_dir, filename)
    open(path, "w").write(
        f"---\nid: PHASE_{phase_slug}_{module_slug}_CLAUDE_{suffix}\n"
        f"module_id: {module_id}\nword_count: {wc}\n"
        f"input_tokens: {input_tokens}\noutput_tokens: {output_tokens}\n---\n\n{prose}"
    )
    return path, wc

def main():
    parser = argparse.ArgumentParser(description="ELYSIUM Claude API Prose Generator (all modes)")
    parser.add_argument("--module", required=True, help="Module ID, e.g. OPN-014")
    parser.add_argument("--context_pack", help="Path to context pack (required for initial prose)")
    parser.add_argument("--prose", help="Path to existing prose file (required for --revision and --compress)")
    parser.add_argument("--revision", action="store_true", help="Revision mode: revise existing prose")
    parser.add_argument("--revision_instructions", help="Specific revision instructions (for --revision mode)")
    parser.add_argument("--compress", action="store_true", help="Compression mode: trim word count only")
    parser.add_argument("--target_words", type=int, help="Target word count for compression")
    parser.add_argument("--output_dir", default="BOOK/_fcs/api_outputs", help="Output directory")
    parser.add_argument("--phase", default="III-1A-S4", help="Phase ID for output filename")
    args = parser.parse_args()

    module_id = args.module
    phase_slug = args.phase.replace("-", "_").replace("/", "_")
    module_slug = module_id.replace("-", "")
    client = anthropic.Anthropic(api_key=get_claude_key())

    # ── MODE: COMPRESS ──────────────────────────────────────────────────────
    if args.compress:
        if not args.prose:
            print("ERROR: --compress requires --prose"); exit(1)
        prose_body = read_prose_body(args.prose)
        current_wc = len(prose_body.split())
        target = args.target_words or int(current_wc * 0.9)
        prompt = (
            f"This ELYSIUM prose is {current_wc} words. Compress to approximately {target} words "
            f"by tightening sentences and removing redundancy. Do NOT remove any structural element "
            f"or key concept. Preserve ELYSIUM voice.\n\nPROSE:\n---\n{prose_body}\n---\n\n"
            f"Output ONLY the compressed prose."
        )
        print(f"[COMPRESS] {module_id}: {current_wc}w → target {target}w", flush=True)
        msg = client.messages.create(model="claude-opus-4-5", max_tokens=2048,
            system=SYSTEM_PROMPT, messages=[{"role": "user", "content": prompt}])
        prose = msg.content[0].text
        path, wc = save_output(args.output_dir, phase_slug, module_slug, "COMPRESSED",
                               module_id, prose, msg.usage.input_tokens, msg.usage.output_tokens)
        print(f"Compressed: {wc}w | {msg.usage.input_tokens} in / {msg.usage.output_tokens} out")
        print(f"OUTPUT_PATH={path}"); print(f"WORD_COUNT={wc}")

    # ── MODE: REVISION ───────────────────────────────────────────────────────
    elif args.revision:
        if not args.prose:
            print("ERROR: --revision requires --prose"); exit(1)
        prose_body = read_prose_body(args.prose)
        instructions = args.revision_instructions or "Apply the review instructions to improve the prose."
        context = ""
        if args.context_pack and os.path.exists(args.context_pack):
            context = f"\n\nORIGINAL CONTEXT PACK:\n{open(args.context_pack).read()}"
        prompt = (
            f"Revise this ELYSIUM {module_id} prose according to the instructions below.\n\n"
            f"REVISION INSTRUCTIONS:\n{instructions}{context}\n\n"
            f"CURRENT PROSE:\n---\n{prose_body}\n---\n\n"
            f"Output ONLY the revised prose."
        )
        print(f"[REVISION] {module_id}", flush=True)
        msg = client.messages.create(model="claude-opus-4-5", max_tokens=2048,
            system=SYSTEM_PROMPT, messages=[{"role": "user", "content": prompt}])
        prose = msg.content[0].text
        path, wc = save_output(args.output_dir, phase_slug, module_slug, "REVISED",
                               module_id, prose, msg.usage.input_tokens, msg.usage.output_tokens)
        print(f"Revised: {wc}w | {msg.usage.input_tokens} in / {msg.usage.output_tokens} out")
        print(f"OUTPUT_PATH={path}"); print(f"WORD_COUNT={wc}")

    # ── MODE: INITIAL PROSE ──────────────────────────────────────────────────
    else:
        if not args.context_pack:
            print("ERROR: initial prose mode requires --context_pack"); exit(1)
        if not os.path.exists(args.context_pack):
            print(f"ERROR: Context pack not found: {args.context_pack}"); exit(1)
        context_pack = open(args.context_pack).read()
        prompt = (
            f"Write the prose for {module_id} as specified in the context pack below.\n\n"
            f"Output ONLY the prose. No title, no headers, no preamble.\n\n"
            f"CONTEXT PACK:\n{context_pack}"
        )
        print(f"[PROSE] {module_id}", flush=True)
        msg = client.messages.create(model="claude-opus-4-5", max_tokens=2048,
            system=SYSTEM_PROMPT, messages=[{"role": "user", "content": prompt}])
        prose = msg.content[0].text
        path, wc = save_output(args.output_dir, phase_slug, module_slug, "RAW",
                               module_id, prose, msg.usage.input_tokens, msg.usage.output_tokens)
        print(f"Generated: {wc}w | {msg.usage.input_tokens} in / {msg.usage.output_tokens} out")
        print(f"OUTPUT_PATH={path}"); print(f"WORD_COUNT={wc}")

if __name__ == "__main__":
    main()
