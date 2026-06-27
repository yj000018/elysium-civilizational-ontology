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
    # Read docs 21-26
    docs_content = ""
    for i in range(21, 27):
        filename = f"{i}"
        path = ""
        if i == 26:
            path = f"/home/ubuntu/ELYSIUM/03_GOVERNANCE/"
        else:
            path = f"/home/ubuntu/ELYSIUM/06_OPERATIONS_AND_LEGACY/"
            
        files = os.listdir(path)
        for f in files:
            if f.startswith(filename) and f.endswith(".md"):
                with open(os.path.join(path, f), "r") as doc_file:
                    docs_content += f"\n\n--- DOCUMENT {filename} ---\n"
                    docs_content += doc_file.read()
    
    architect_system = "You are the Chief Architect and coherence guardian of ELYSIUM."
    audit_prompt = f"""
Perform Chief Architect Audit #5 on Documents 21-26 (Operations, Legacy, and AI Constitution).
This is also the FINAL AUDIT for the entire 26-document program.

The audit must review:
* architectural coherence of the operations and legacy block
* robustness of the AI Collaboration Constitution
* overall completion status of the ELYSIUM Program
* missing documents or gaps across the entire 26-document corpus
* next steps for the Founder
* strategic risks for launch
* Y-OS orchestration improvements

Documents Content:
{docs_content}

Output the audit as a formal Markdown report.
"""
    print("Running Chief Architect Audit #5 (Final)...")
    audit_report = call_llm(audit_prompt, architect_system)
    
    with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/AUDIT_05_FINAL.md", "w") as f:
        f.write(audit_report)
        
    # Update State
    with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/ELYSIUM_PROGRAM_STATE.json", "r") as f:
        state = json.load(f)
        
    # Add audit if it doesn't exist yet
    if len(state.get("audits", [])) < 5:
        if "audits" not in state:
            state["audits"] = []
        while len(state["audits"]) < 5:
            state["audits"].append({"id": f"0{len(state['audits'])+1}", "status": "PENDING"})
            
    state["audits"][4]["status"] = "COMPLETED"
    state["next_action"] = "Program Complete. Await Founder instructions."
    state["active_document"] = None
    state["status"] = "COMPLETE"
    
    with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/ELYSIUM_PROGRAM_STATE.json", "w") as f:
        json.dump(state, f, indent=2)
        
    print("Audit #5 complete and state updated. Program finished.")

if __name__ == "__main__":
    run_audit()
