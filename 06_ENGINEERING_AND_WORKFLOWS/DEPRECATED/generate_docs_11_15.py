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
        state["next_action"] = "Chief Architect Audit #3"
        
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
        "id": "11",
        "title": "Governance Handbook",
        "path": "/home/ubuntu/ELYSIUM/03_GOVERNANCE/11_GOVERNANCE_HANDBOOK.md",
        "prompt": "Produce Document 11: Governance Handbook. Context: Define the overall governance model of the ELYSIUM Foundation. How are decisions made? What is the role of the Founder vs the Community? Include metadata header.",
        "next_id": "12",
        "next_title": "Ontology Stewardship Council Handbook"
    },
    {
        "id": "12",
        "title": "Ontology Stewardship Council Handbook",
        "path": "/home/ubuntu/ELYSIUM/03_GOVERNANCE/12_ONTOLOGY_STEWARDSHIP_COUNCIL_HANDBOOK.md",
        "prompt": "Produce Document 12: Ontology Stewardship Council Handbook. Context: Define the specific body responsible for maintaining the 7 Foundations and 38 Facets. How do they approve changes? Include metadata header.",
        "next_id": "13",
        "next_title": "Community Contribution Guide"
    },
    {
        "id": "13",
        "title": "Community Contribution Guide",
        "path": "/home/ubuntu/ELYSIUM/03_GOVERNANCE/13_COMMUNITY_CONTRIBUTION_GUIDE.md",
        "prompt": "Produce Document 13: Community Contribution Guide. Context: How can individuals, researchers, and organizations contribute to the ELYSIUM ontology or platform? What is the process? Include metadata header.",
        "next_id": "14",
        "next_title": "Future Observatory Framework"
    },
    {
        "id": "14",
        "title": "Future Observatory Framework",
        "path": "/home/ubuntu/ELYSIUM/04_OBSERVATORY/14_FUTURE_OBSERVATORY_FRAMEWORK.md",
        "prompt": "Produce Document 14: Future Observatory Framework. Context: Define the 'Future Observatory'—the sensory organ of ELYSIUM that monitors global trends, weak signals, and maps them to the 7 Foundations. Include metadata header.",
        "next_id": "15",
        "next_title": "Civilization State Report Template"
    },
    {
        "id": "15",
        "title": "Civilization State Report Template",
        "path": "/home/ubuntu/ELYSIUM/04_OBSERVATORY/15_CIVILIZATION_STATE_REPORT_TEMPLATE.md",
        "prompt": "Produce Document 15: Civilization State Report Template. Context: Provide the official template for the annual 'State of Civilization' report, structured around the 3 Scales and 7 Foundations. Include metadata header.",
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

print("\nBatch complete. Ready for Chief Architect Audit #3.")
