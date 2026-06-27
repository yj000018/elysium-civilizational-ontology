#!/usr/bin/env python3
import os
import json
import requests

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def call_llm(prompt, system_prompt, model="gpt-4o"):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def update_state(doc_id, next_doc_id, next_doc_title):
    with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/ELYSIUM_PROGRAM_STATE.json", "r") as f:
        state = json.load(f)
    
    state["documents_completed"] += 1
    state["active_document"] = next_doc_id
    if next_doc_id:
        state["next_action"] = f"Start Document {next_doc_id}: {next_doc_title}"
    else:
        state["next_action"] = "Chief Architect Audit #4"
        
    for doc in state["documents"]:
        if doc["id"] == doc_id:
            doc["status"] = "INTEGRATED"
            doc["version"] = "0.9"
            
    with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/ELYSIUM_PROGRAM_STATE.json", "w") as f:
        json.dump(state, f, indent=2)

    with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/DOCUMENTATION_REGISTRY.json", "r") as f:
        registry = json.load(f)
    for doc in registry["documents"]:
        if doc["id"] == doc_id:
            doc["status"] = "INTEGRATED"
    with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/DOCUMENTATION_REGISTRY.json", "w") as f:
        json.dump(registry, f, indent=2)

architect_system = "You are the Chief Architect and coherence guardian of ELYSIUM, an Open Civilizational Infrastructure and future foundation headquartered in Geneva."
reviewer_system = "You are the Editorial and Coherence Review Officer for ELYSIUM. Review for clarity, contradictions, tone, philosophical nuance, governance risk and alignment with ELYSIUM."

docs_to_generate = [
    {
        "id": "16",
        "title": "Book Canon",
        "path": "/home/ubuntu/ELYSIUM/05_APPLICATIONS/16_BOOK_CANON.md",
        "prompt": "Produce Document 16: Book Canon. Context: Define the strategy for the ELYSIUM foundational book (the one currently being researched). Outline its structure, tone, and target audience. Include metadata header.",
        "next_id": "17",
        "next_title": "Brand & Visual System"
    },
    {
        "id": "17",
        "title": "Brand & Visual System",
        "path": "/home/ubuntu/ELYSIUM/05_APPLICATIONS/17_BRAND_AND_VISUAL_SYSTEM.md",
        "prompt": "Produce Document 17: Brand & Visual System. Context: Define the visual identity of ELYSIUM. How do we visually represent the 7 Foundations and the holographic nature of the ontology? Include metadata header.",
        "next_id": "18",
        "next_title": "Website Architecture"
    },
    {
        "id": "18",
        "title": "Website Architecture",
        "path": "/home/ubuntu/ELYSIUM/05_APPLICATIONS/18_WEBSITE_ARCHITECTURE.md",
        "prompt": "Produce Document 18: Website Architecture. Context: Define the structure of the ELYSIUM digital platform. It is not just a brochure, but a living epistemic infrastructure. Include metadata header.",
        "next_id": "19",
        "next_title": "Educational Framework"
    },
    {
        "id": "19",
        "title": "Educational Framework",
        "path": "/home/ubuntu/ELYSIUM/05_APPLICATIONS/19_EDUCATIONAL_FRAMEWORK.md",
        "prompt": "Produce Document 19: Educational Framework. Context: How is the ELYSIUM ontology taught? Define the curriculum, from basic introduction to advanced civilizational architecture. Include metadata header.",
        "next_id": "20",
        "next_title": "AI Ecosystem / Y-OS Integration"
    },
    {
        "id": "20",
        "title": "AI Ecosystem / Y-OS Integration",
        "path": "/home/ubuntu/ELYSIUM/05_APPLICATIONS/20_AI_ECOSYSTEM_YOS_INTEGRATION.md",
        "prompt": "Produce Document 20: AI Ecosystem / Y-OS Integration. Context: How does ELYSIUM interact with AI agents and the Y-OS ecosystem? Define the API, the Knowledge Graph access, and the role of agents like Manus. Include metadata header.",
        "next_id": None,
        "next_title": None
    }
]

for doc in docs_to_generate:
    print(f"\nGenerating Document {doc['id']}: {doc['title']}...")
    
    print("  Drafting...")
    draft = call_llm(doc["prompt"], architect_system, "gpt-4o")
    
    print("  Reviewing...")
    review = call_llm(f"Review this draft:\n\n{draft}", reviewer_system, "gpt-4-turbo")
    
    print("  Revising...")
    revision_prompt = f"Revise Document {doc['id']} based on this critique.\n\nDraft:\n{draft}\n\nCritique:\n{review}\n\nProduce final Markdown. Set version to 0.9, status INTEGRATED."
    final = call_llm(revision_prompt, architect_system, "gpt-4o")
    
    with open(doc["path"], "w") as f:
        f.write(final)
        
    update_state(doc["id"], doc["next_id"], doc["next_title"])
    print(f"  Saved and state updated.")

print("\nBatch complete. Ready for Chief Architect Audit #4.")
