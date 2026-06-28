#!/usr/bin/env python3
"""
ELYSIUM — Generic Claude API Prose Generator
Usage: python3 call_claude_prose.py --module OPN-007 --context_pack BOOK/_fcs/context_packs/OPN007_CONTEXT_PACK.md
"""
import argparse
import os
import sys
import anthropic

CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY", "")  # Set via env var — never hardcode

SYSTEM_PROMPT = """You are a literary prose writer for ELYSIUM, a civilizational ontology book.

Voice: civilizational, lucid, literary but not ornate, rigorous but accessible. English only.
You produce final prose — not outlines, not drafts with commentary, not explanations.
You write exactly what will appear on the page.

Rules:
- Write only the current module specified in the context pack
- Do NOT write any subsequent module
- Do NOT use bullet points in prose
- Do NOT use markdown headings inside prose except the module title (H1)
- No WYS, no Manus prose
- ELYSIUM voice: civilizational, lucid, literary but not ornate, rigorous but accessible
- Respect the word target and forbidden moves specified in the context pack"""

def main():
    parser = argparse.ArgumentParser(description="ELYSIUM Claude API Prose Generator")
    parser.add_argument("--module", required=True, help="Module ID, e.g. OPN-007")
    parser.add_argument("--context_pack", required=True, help="Path to context pack markdown file")
    parser.add_argument("--output_dir", default="BOOK/_fcs/api_outputs", help="Output directory")
    parser.add_argument("--phase", default="III-1A-S4", help="Phase ID for output filename")
    args = parser.parse_args()

    module_id = args.module
    context_pack_path = args.context_pack
    output_dir = args.output_dir
    phase_slug = args.phase.replace("-", "_").replace("/", "_")
    module_slug = module_id.replace("-", "")

    # Read context pack
    if not os.path.exists(context_pack_path):
        print(f"ERROR: Context pack not found: {context_pack_path}")
        exit(1)
    with open(context_pack_path, "r") as f:
        context_pack = f.read()

    user_prompt = f"""Write the prose for {module_id} as specified in the context pack below.

Begin with the module title as a markdown H1, then write the prose directly.
No preamble, no explanation, no commentary — only the final prose.

CONTEXT PACK:
{context_pack}"""

    client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
    print(f"Calling Claude API (claude-opus-4-5) for {module_id}...", flush=True)

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    )

    prose = message.content[0].text
    word_count = len(prose.split())
    input_tokens = message.usage.input_tokens
    output_tokens = message.usage.output_tokens

    print(f"Prose received. Words: {word_count} | Tokens in: {input_tokens} / out: {output_tokens}", flush=True)

    os.makedirs(output_dir, exist_ok=True)
    output_filename = f"PHASE_{phase_slug}_{module_slug}_CLAUDE_RAW.md"
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, "w") as f:
        f.write(f"---\nid: PHASE_{phase_slug}_{module_slug}_CLAUDE_RAW\n")
        f.write(f"module_id: {module_id}\n")
        f.write(f"word_count: {word_count}\n")
        f.write(f"input_tokens: {input_tokens}\n")
        f.write(f"output_tokens: {output_tokens}\n---\n\n")
        f.write(prose)

    print(f"Saved: {output_path}", flush=True)
    # Also print word count for pipeline consumption
    print(f"WORD_COUNT={word_count}", flush=True)
    print(f"OUTPUT_PATH={output_path}", flush=True)

if __name__ == "__main__":
    main()
