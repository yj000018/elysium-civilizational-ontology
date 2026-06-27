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
        state["next_action"] = "Chief Architect Audit #2"
        
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
        "id": "06",
        "title": "Ontology Specification",
        "path": "/home/ubuntu/ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/06_ONTOLOGY_SPECIFICATION.md",
        "prompt": "Produce Document 06: Ontology Specification. Context: Provide the detailed technical specification of the 3 Scales, 7 Foundations, and 38 Facets. Explain how they interlock holographically. Include metadata header.",
        "next_id": "07",
        "next_title": "Knowledge Graph Specification"
    },
    {
        "id": "07",
        "title": "Knowledge Graph Specification",
        "path": "/home/ubuntu/ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/07_KNOWLEDGE_GRAPH_SPECIFICATION.md",
        "prompt": "Produce Document 07: Knowledge Graph Specification. Context: Detail how the ontology is translated into a machine-readable Knowledge Graph (nodes, edges, relationships, properties) for the ELYSIUM platform. Include metadata header.",
        "next_id": "08",
        "next_title": "Research Methodology"
    },
    {
        "id": "08",
        "title": "Research Methodology",
        "path": "/home/ubuntu/ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/08_RESEARCH_METHODOLOGY.md",
        "prompt": "Produce Document 08: Research Methodology. Context: Document the 'Adventurer's Approach' used to audit the 136 models. Explain the 12-step Universal Analysis Matrix and how future research should be conducted. Include metadata header.",
        "next_id": "09",
        "next_title": "Model Registry"
    },
    {
        "id": "09",
        "title": "Model Registry",
        "path": "/home/ubuntu/ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/09_MODEL_REGISTRY.md",
        "prompt": "Produce Document 09: Model Registry. Context: Establish the framework for registering, categorizing, and scoring civilizational models (like the 136 already audited) within the ELYSIUM ecosystem. Include metadata header.",
        "next_id": "10",
        "next_title": "Evidence Standards"
    },
    {
        "id": "10",
        "title": "Evidence Standards",
        "path": "/home/ubuntu/ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/10_EVIDENCE_STANDARDS.md",
        "prompt": "Produce Document 10: Evidence Standards. Context: Define what constitutes valid epistemic evidence for the ELYSIUM ontology. How do we balance hard science, indigenous knowledge, and philosophical models? Include metadata header.",
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

print("\nBatch complete. Ready for Chief Architect Audit #2.")
