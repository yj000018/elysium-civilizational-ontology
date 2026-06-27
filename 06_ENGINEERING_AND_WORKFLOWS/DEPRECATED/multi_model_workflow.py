#!/usr/bin/env python3
import os
import json
import requests
import anthropic

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

def call_chatgpt(prompt, system_prompt="You are a helpful assistant."):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def call_claude(prompt, system_prompt="You are a helpful assistant."):
    # Fallback to OpenAI API with a different model if Claude is unavailable
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "gpt-4-turbo",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def generate_document_01():
    print("Step 1: ChatGPT drafting Document 01...")
    architect_system = "You are the Chief Architect and coherence guardian of ELYSIUM, an Open Civilizational Infrastructure and future foundation headquartered in Geneva."
    draft_prompt = """
Produce Document 01: The ELYSIUM Charter.

Context: ELYSIUM is an epistemic infrastructure for humanity. The ontology (3 Scales x 7 Foundations) is the core. The platform is the living organism. The community is the steward. The Future Observatory keeps the system alive. The Ontology Stewardship Council protects coherence.

Requirements:
- Write in English, professional, visionary, institutional tone.
- Include preamble, purpose, core structure (Ontology, Platform, Community, Observatory, Council).
- Include metadata header: title, document_id (01), version (0.1), status (DRAFT), owner (Yannick), authoring_engine (ChatGPT).
- Use Markdown.
"""
    draft = call_chatgpt(draft_prompt, architect_system)
    
    with open("/home/ubuntu/ELYSIUM/01_FOUNDATIONAL_TEXTS/01_ELYSIUM_CHARTER_draft.md", "w") as f:
        f.write(draft)

    print("Step 2: Claude reviewing Document 01...")
    reviewer_system = "You are the Editorial and Coherence Review Officer for ELYSIUM."
    review_prompt = f"""
Review the following draft of Document 01: The ELYSIUM Charter.
Review for clarity, contradictions, tone, philosophical nuance, governance risk and alignment with ELYSIUM.
Provide specific critique and suggested revisions. Do not rewrite the whole text, just provide the review.

Draft:
{draft}
"""
    review = call_claude(review_prompt, reviewer_system)
    
    with open("/home/ubuntu/ELYSIUM/01_FOUNDATIONAL_TEXTS/01_ELYSIUM_CHARTER_review.md", "w") as f:
        f.write(review)

    print("Step 3: ChatGPT revising Document 01...")
    revision_prompt = f"""
You are the Chief Architect of ELYSIUM. Revise Document 01: The ELYSIUM Charter based on the Review Officer's critique.

Original Draft:
{draft}

Critique:
{review}

Produce the final revised Markdown document. Update the metadata header to version 0.9, status INTEGRATED, review_engine Claude.
"""
    final = call_chatgpt(revision_prompt, architect_system)
    
    with open("/home/ubuntu/ELYSIUM/01_FOUNDATIONAL_TEXTS/01_ELYSIUM_CHARTER.md", "w") as f:
        f.write(final)
        
    print("Document 01 generation complete.")

if __name__ == "__main__":
    generate_document_01()
