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

def run_audit():
    # Read docs 1-5
    docs_content = ""
    for i in range(1, 6):
        filename = f"0{i}" if i < 10 else str(i)
        path = ""
        if i <= 4:
            path = f"/home/ubuntu/ELYSIUM/01_FOUNDATIONAL_TEXTS/"
        else:
            path = f"/home/ubuntu/ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/"
            
        files = os.listdir(path)
        for f in files:
            if f.startswith(filename) and f.endswith(".md"):
                with open(os.path.join(path, f), "r") as doc_file:
                    docs_content += f"\n\n--- DOCUMENT {filename} ---\n"
                    docs_content += doc_file.read()
    
    architect_system = "You are the Chief Architect and coherence guardian of ELYSIUM."
    audit_prompt = f"""
Perform Chief Architect Audit #1 on Documents 01-05.

The audit must review:
* architectural coherence
* document dependency consistency
* alignment with ELYSIUM purpose (epistemic infrastructure, 7 Foundations)
* governance implications
* missing documents or gaps
* next steps
* strategic risks
* Y-OS orchestration improvements

Documents Content:
{docs_content}

Output the audit as a formal Markdown report.
"""
    print("Running Chief Architect Audit #1...")
    audit_report = call_llm(audit_prompt, architect_system)
    
    with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/AUDIT_01.md", "w") as f:
        f.write(audit_report)
        
    # Update State
    with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/ELYSIUM_PROGRAM_STATE.json", "r") as f:
        state = json.load(f)
        
    state["audits"][0]["status"] = "COMPLETED"
    state["next_action"] = "Start Document 06: Ontology Specification"
    state["active_document"] = "06"
    
    with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/ELYSIUM_PROGRAM_STATE.json", "w") as f:
        json.dump(state, f, indent=2)
        
    print("Audit #1 complete and state updated.")

if __name__ == "__main__":
    run_audit()
