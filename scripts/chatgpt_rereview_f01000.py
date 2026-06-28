#!/usr/bin/env python3
"""ChatGPT API re-review of F01-000 after truncation repair."""

import os, re, json
from openai import OpenAI

# Use sandbox pre-configured OpenAI client
client = OpenAI()

REPO = "/home/ubuntu/elysium_github_clone"
DRAFT_PATH = f"{REPO}/BOOK/manuscript/02_foundations/F01_material_existence/drafts/F01-000_DRAFT_0.md"
BRIEF_PATH = f"{REPO}/BOOK/manuscript/02_foundations/F01_material_existence/writing_briefs/F01-000_writing_brief.md"
OUTPUT_PATH = f"{REPO}/BOOK/_fcs/api_outputs/PHASE_III_1A_S4_F01_F01000_CHATGPT_REREVIEW_AFTER_REPAIR.md"

def strip_fm(content):
    if not content.startswith('---'):
        return content
    end = content.find('---', 3)
    return content[end+3:].strip() if end > 0 else content

draft_content = open(DRAFT_PATH).read()
brief_content = open(BRIEF_PATH).read()
prose = strip_fm(draft_content)
wc = len(prose.split())

print(f"F01-000 prose: {wc} words, last_char={repr(prose.rstrip()[-1])}")

system_prompt = """You are the ELYSIUM Chief Architect reviewer. 
Your role is to review prose drafts against their writing briefs.
Return PASS or REVISE with brief justification.
Be strict about: canonical accuracy, completeness against brief requirements, terminal punctuation, no truncation."""

user_prompt = f"""Review this ELYSIUM prose module against its writing brief.

WRITING BRIEF:
{brief_content}

PROSE DRAFT (F01-000, {wc} words, post-repair):
{prose}

Review criteria:
1. Does the prose address all "Must include" items from the brief?
2. Does it respect all "Hard constraints"?
3. Does it end with terminal punctuation (not truncated)?
4. Is the canonical direction correct (Material Existence as first foundation)?
5. Does it bridge correctly to Energy as first facet?

Return format:
RESULT: PASS or REVISE
ISSUES: [list any issues, or "None"]
SUMMARY: [1-2 sentence summary]"""

print("Calling ChatGPT API...")
response = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    max_tokens=600,
    temperature=0.3
)

review_text = response.choices[0].message.content
result_match = re.search(r'RESULT:\s*(PASS|REVISE)', review_text, re.I)
result = result_match.group(1).upper() if result_match else "UNKNOWN"

print(f"\nChatGPT Review Result: {result}")
print(f"\nFull review:\n{review_text}")

# Save output
output_content = f"""---
id: PHASE_III_1A_S4_F01_F01000_CHATGPT_REREVIEW_AFTER_REPAIR
module_id: F01-000
review_type: chatgpt_rereview_post_repair
model: gpt-4o-2024-08-06
result: {result}
prose_word_count: {wc}
repair_type: truncation_restoration_from_CLAUDE_RAW
date: 2026-06-28
---

# F01-000 ChatGPT Re-Review (Post-Repair)

{review_text}
"""

open(OUTPUT_PATH, 'w').write(output_content)
print(f"\nOutput saved: {OUTPUT_PATH}")
print(f"FINAL RESULT: {result}")
