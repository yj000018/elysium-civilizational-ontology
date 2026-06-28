#!/usr/bin/env python3
"""
ELYSIUM — Generic ChatGPT API Prose Reviewer
Usage: python3 call_chatgpt_review.py --module OPN-007 --prose BOOK/_fcs/api_outputs/..._CLAUDE_RAW.md --brief BOOK/manuscript/01_opening/writing_briefs/OPN-007_writing_brief.md
"""
import argparse
import os
import sys
import requests

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")  # Set via env var — never hardcode

SYSTEM_PROMPT = """You are the ChatGPT Chief Architect and coherence reviewer for ELYSIUM, a civilizational ontology book.
You provide precise, actionable reviews with clear PASS/REVISE/FAIL decisions.
Format your response exactly as:
DECISION: [PASS/REVISE/FAIL]
RATIONALE: [brief explanation]
REVISION_INSTRUCTIONS: [if REVISE/FAIL, list specific changes; if PASS, write "None"]"""

def main():
    parser = argparse.ArgumentParser(description="ELYSIUM ChatGPT API Prose Reviewer")
    parser.add_argument("--module", required=True, help="Module ID, e.g. OPN-007")
    parser.add_argument("--prose", required=True, help="Path to Claude raw prose markdown file")
    parser.add_argument("--brief", required=True, help="Path to writing brief markdown file")
    parser.add_argument("--output_dir", default="BOOK/_fcs/reviews", help="Output directory")
    parser.add_argument("--phase", default="III-1A-S4", help="Phase ID for output filename")
    args = parser.parse_args()

    module_id = args.module
    phase_slug = args.phase.replace("-", "_").replace("/", "_")
    module_slug = module_id.replace("-", "")

    # Read prose
    if not os.path.exists(args.prose):
        print(f"ERROR: Prose file not found: {args.prose}")
        exit(1)
    with open(args.prose, "r") as f:
        prose_raw = f.read()
    # Strip frontmatter if present
    if prose_raw.startswith("---"):
        parts = prose_raw.split("---", 2)
        prose = parts[2].strip() if len(parts) >= 3 else prose_raw
    else:
        prose = prose_raw

    # Read brief
    if not os.path.exists(args.brief):
        print(f"ERROR: Brief file not found: {args.brief}")
        exit(1)
    with open(args.brief, "r") as f:
        brief = f.read()

    review_prompt = f"""Review the following prose for {module_id} against its writing brief.

WRITING BRIEF:
{brief}

PROSE TO REVIEW:
{prose}

EVALUATE AGAINST:
1. Brief fidelity (purpose, beats, tone, word target)
2. Structural fidelity (movement role, reader transition)
3. Forbidden moves (none should appear)
4. ELYSIUM voice (civilizational, lucid, literary but not ornate, rigorous but accessible)
5. Continuity with previous module (if specified in brief)
6. Readiness for DRAFT_0

REQUIRED DECISION: PASS / REVISE / FAIL"""

    print(f"Calling ChatGPT API for {module_id} review...", flush=True)

    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-4o-2024-08-06",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": review_prompt}
        ],
        "max_tokens": 1024
    }
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers, json=payload, timeout=120
    )
    response.raise_for_status()
    data = response.json()

    review = data["choices"][0]["message"]["content"]
    input_tokens = data["usage"]["prompt_tokens"]
    output_tokens = data["usage"]["completion_tokens"]

    print(f"Review received. Tokens in: {input_tokens} / out: {output_tokens}", flush=True)
    print(f"\n--- REVIEW ---\n{review}\n--- END REVIEW ---", flush=True)

    # Parse decision
    decision = "UNKNOWN"
    for line in review.splitlines():
        if line.startswith("DECISION:"):
            decision = line.replace("DECISION:", "").strip()
            break

    print(f"DECISION={decision}", flush=True)

    os.makedirs(args.output_dir, exist_ok=True)
    output_filename = f"PHASE_{phase_slug}_{module_slug}_CHATGPT_REVIEW.md"
    output_path = os.path.join(args.output_dir, output_filename)

    with open(output_path, "w") as f:
        f.write(f"---\nid: PHASE_{phase_slug}_{module_slug}_CHATGPT_REVIEW\n")
        f.write(f"module_id: {module_id}\n")
        f.write(f"decision: {decision}\n")
        f.write(f"input_tokens: {input_tokens}\n")
        f.write(f"output_tokens: {output_tokens}\n---\n\n")
        f.write(review)

    print(f"Saved: {output_path}", flush=True)
    print(f"OUTPUT_PATH={output_path}", flush=True)

if __name__ == "__main__":
    main()
