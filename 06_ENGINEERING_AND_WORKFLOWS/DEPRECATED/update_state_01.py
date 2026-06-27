#!/usr/bin/env python3
import json

# Update Program State
with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/ELYSIUM_PROGRAM_STATE.json", "r") as f:
    state = json.load(f)

state["documents_completed"] = 1
state["active_document"] = "02"
state["next_action"] = "Start Document 02: Founding Manifesto"

for doc in state["documents"]:
    if doc["id"] == "01":
        doc["status"] = "INTEGRATED"
        doc["version"] = "0.9"

with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/ELYSIUM_PROGRAM_STATE.json", "w") as f:
    json.dump(state, f, indent=2)

# Update Documentation Registry
with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/DOCUMENTATION_REGISTRY.json", "r") as f:
    registry = json.load(f)

for doc in registry["documents"]:
    if doc["id"] == "01":
        doc["status"] = "INTEGRATED"

with open("/home/ubuntu/ELYSIUM/00_PROGRAM_OFFICE/DOCUMENTATION_REGISTRY.json", "w") as f:
    json.dump(registry, f, indent=2)

print("State updated for Document 01")
