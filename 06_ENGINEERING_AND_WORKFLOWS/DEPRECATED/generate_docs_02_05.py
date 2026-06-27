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
        state["next_action"] = "Chief Architect Audit #1"
        
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
        "id": "02",
        "title": "Founding Manifesto",
        "path": "/home/ubuntu/ELYSIUM/01_FOUNDATIONAL_TEXTS/02_FOUNDING_MANIFESTO.md",
        "prompt": "Produce Document 02: The Founding Manifesto of ELYSIUM. Context: It should be a passionate, visionary call to action. We need a new epistemic infrastructure to guide civilizational transition. Include metadata header.",
        "next_id": "03",
        "next_title": "Philosophical Constitution"
    },
    {
        "id": "03",
        "title": "Philosophical Constitution",
        "path": "/home/ubuntu/ELYSIUM/01_FOUNDATIONAL_TEXTS/03_PHILOSOPHICAL_CONSTITUTION.md",
        "prompt": "Produce Document 03: Philosophical Constitution of ELYSIUM. Context: Define the core beliefs, the 3 Scales (Human, Society, Civilization), the 7 Foundations, and the non-reductive, holographic nature of reality. Include metadata header.",
        "next_id": "04",
        "next_title": "Civilizational Principles"
    },
    {
        "id": "04",
        "title": "Civilizational Principles",
        "path": "/home/ubuntu/ELYSIUM/01_FOUNDATIONAL_TEXTS/04_CIVILIZATIONAL_PRINCIPLES.md",
        "prompt": "Produce Document 04: Civilizational Principles of ELYSIUM. Context: Define the actionable principles derived from the Constitution that will guide the Foundation, the Platform, and the Community. Include metadata header.",
        "next_id": "05",
        "next_title": "Core Ontology Overview"
    },
    {
        "id": "05",
        "title": "Core Ontology Overview",
        "path": "/home/ubuntu/ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/05_CORE_ONTOLOGY_OVERVIEW.md",
        "prompt": "Produce Document 05: Core Ontology Overview. Context: Introduce the ELYSIUM ontology: 3 Scales, 7 Foundations (Foundation, Vitality, Agency, Cohesion, Governance, Vision, Consciousness), and the 3 Z-Axis dynamics (Digital, Evolutionary, Complexity). Include metadata header.",
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

print("\nBatch complete. Ready for Chief Architect Audit #1.")
