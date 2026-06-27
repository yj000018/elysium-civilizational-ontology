#!/usr/bin/env python3
"""Part I: yOS Program OS Extraction."""
import json
from pathlib import Path

BASE = Path("/home/ubuntu/ELYSIUM_CANON")
YOS_DIR = BASE / "YOS_PROGRAM_OS"
YOS_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATE_DIR = YOS_DIR / "PROGRAM_OS_FOLDER_TEMPLATE"
TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)
DATE = "2026-06-27"

# 1. Create the Master Specification
yos_spec = f"""# yOS PROGRAM OPERATING SYSTEM (V1)
**Generic Specification for Autonomous AI-Driven Program Execution**

**Date:** {DATE}
**Version:** 1.0
**Extracted From:** ELYSIUM Program
**Status:** CANONICAL

---

## 1. Purpose
The yOS Program Operating System (Program OS) provides a rigorous, generic, and reusable execution layer for complex, multi-stage, AI-driven projects. It solves the problem of context loss, hallucination, and architectural drift when LLMs execute long-running programs over days or weeks.

## 2. Why this exists inside yOS Core
Standard AI workflows are stateless and forgetful. The Program OS forces AI agents (like Manus, ChatGPT, or Claude) to act as disciplined Program Managers. It provides the "scaffolding" required for yOS to execute massive undertakings autonomously while maintaining absolute integrity.

## 3. When to use it
- Projects requiring >10 generated documents.
- Projects with complex ontologies or knowledge graphs.
- Projects where multiple AI models collaborate (e.g., ChatGPT drafts, Claude reviews, Manus orchestrates).
- Projects requiring strict version control and human-in-the-loop audit gates.

## 4. When not to use it
- Quick, single-shot generation tasks.
- Routine code generation where Git alone is sufficient.
- Exploratory, unstructured brainstorming sessions.

## 5. Core Principles
1. **State is Supreme:** The AI must read the Program State before acting and update it after acting.
2. **Sequential over Parallel:** For foundational architecture, sequential execution prevents catastrophic drift.
3. **Audit Gates:** Execution must pause at predefined intervals for Chief Architect (Human or Lead AI) review.
4. **Engine Provenance:** Every artifact must explicitly declare which model drafted, reviewed, and orchestrated it.
5. **No Implicit Finality:** Documents are DRAFT_INTEGRATED until explicitly canonicalized.

## 6. Core Entities
- **Program State:** The single source of truth for the current execution phase.
- **Documentation Registry:** The manifest of all expected, draft, and final documents.
- **Decision Log:** A record of *why* architectural choices were made.
- **Risk Register:** A proactive log of execution blockers or contradictions.

## 7. State Machine
1. `INIT`: Scaffold created.
2. `RESEARCH`: Data gathered, matrices built.
3. `DRAFTING`: Documents generated sequentially.
4. `AUDIT_GATE`: Execution paused for review.
5. `QA_REPAIR`: Integrity checks, dataset fixing.
6. `CANONICALIZATION`: Facts locked, drafts finalized.
7. `DEPLOYMENT`: Integration into yOS Core or publication.

## 8. Program Folder Architecture
```
/00_PROGRAM_OFFICE
/01_CANONICAL_FACTS
/02_KNOWLEDGE_BASE
/03_GENERATED_DOCS
/04_DATASETS
/05_EXPORTS
/99_AUDITS
```

## 9. Documentation Registry
A strict JSON/MD manifest tracking document ID, Title, Status, Word Count, and Dependencies.

## 10. Decision Log
Format: `[Date] [Decision] [Rationale] [Alternatives Rejected]`

## 11. Risk Register
Format: `[Risk ID] [Description] [Severity] [Mitigation]`

## 12. Evidence Registry
All claims made in generated documents must link back to datasets or external sources logged here.

## 13. Asset Registry
Tracks non-text assets (images, PDFs, external links).

## 14. Agent Roles
- **Chief Architect:** Human (Yannick) or Lead AI (ChatGPT). Sets vision, reviews audits.
- **Orchestrator:** AI Agent (Manus). Manages files, runs scripts, updates state.
- **Drafter:** Specialized AI (e.g., Claude for structure, GPT-4o for prose).
- **Reviewer:** Specialized AI (cross-model review).

## 15. Engine Routing
See `MODEL_ROUTING_MATRIX.md`. Right tool for the right job.

## 16. API Call Protocol
Scripts must explicitly use correct SDKs (Anthropic for Claude, OpenAI for GPT). Fallbacks must be logged.

## 17. Memory Protocol
Key facts pushed to Mem0/Notion at the end of every major phase.

## 18. Notion Persistence Protocol
Program State and Canonical Facts mirrored to public Notion pages for universal access.

## 19. Git Persistence Protocol
Code and Markdown pushed to GitHub.

## 20. Audit Gates
Mandatory pause after every N documents (default N=5) for Chief Architect review.

## 21. Human-in-the-Loop Authority
Only the Human can upgrade a document from `DRAFT_INTEGRATED` to `PUBLICATION_READY`.

## 22. Recovery Protocol
If execution crashes, the Orchestrator reads `PROGRAM_STATE.json` and resumes from the last completed ID.

## 23. Contradiction Detection Protocol
Orchestrator must periodically cross-reference new documents against `CANONICAL_FACTS.md`.

## 24. Quality Gates
No zero-byte files. No full-file markdown fences. No placeholder dates.

## 25. Canonicalization Protocol
The process of freezing the core architecture so downstream generation relies on a stable foundation.

## 26. Research Integration Protocol
External models/sources must be explicitly mapped to the internal ontology before use.

## 27. Dataset QA Protocol
CSVs and JSONs must be validated for structure, empty cells, and correct keys.

## 28. Publication Readiness Protocol
Final pass to remove AI artifacts ("As an AI...", "Here is the document...").

## 29. Failure Modes
- **Hallucination Drift:** Cured by frequent Audit Gates.
- **Parallel Collision:** Cured by sequential generation.
- **State Loss:** Cured by JSON state files.

## 30. Minimum Viable Implementation
Just the `00_PROGRAM_OFFICE` folder with State and Registry.

## 31. Example Application: ELYSIUM
Used to generate the 26 foundational documents of the Civilizational Ontology.

## 32. Adaptation Template: CasaTAO
Can be used to orchestrate the architectural design, material sourcing, and legal documentation for CasaTAO.

## 33. Adaptation Template: Y Travel
Can be used to generate the business plan, technical specs, and partner agreements for Y Travel.

## 34. Adaptation Template: Peace of Mind
Can be used to map the security, legal, and operational protocols for Peace of Mind.

## 35. Adaptation Template: Y World / YOUniverse
Can be used to manage the world-building, lore, and technical infrastructure of Y World.

## 36. Integration path into yOS Core
1. Convert this spec into a Manus Skill (`yos-program-os`).
2. Add the template folder to the yOS scaffolding repository.
3. Train ChatGPT on this spec.

## 37. Open questions for Yannick
- Should Audit Gates be purely AI-driven, or always require your manual approval?
- Do you want this implemented as a CLI tool (`yos-program init <name>`)?

## 38. Open questions for ChatGPT Chief Architect
- How can we improve the contradiction detection protocol without excessive token consumption?
- What is the optimal prompt structure for the Reviewer role to prevent "rubber stamping" the Drafter's work?
"""

(YOS_DIR / "YOS_PROGRAM_OS_V1_SPEC.md").write_text(yos_spec)

yos_spec_json = {
    "version": "1.0",
    "date": DATE,
    "name": "yOS Program Operating System",
    "description": "Generic Specification for Autonomous AI-Driven Program Execution",
    "core_principles": [
        "State is Supreme",
        "Sequential over Parallel",
        "Audit Gates",
        "Engine Provenance",
        "No Implicit Finality"
    ],
    "state_machine": ["INIT", "RESEARCH", "DRAFTING", "AUDIT_GATE", "QA_REPAIR", "CANONICALIZATION", "DEPLOYMENT"]
}
(YOS_DIR / "YOS_PROGRAM_OS_V1_SPEC.json").write_text(json.dumps(yos_spec_json, indent=2))

# 2. Create Templates
templates = {
    "PROGRAM_OS_PROMPT_TEMPLATE.md": "# yOS Program OS Execution Prompt\n\n**Role:** You are the Orchestrator.\n**Task:** Read the PROGRAM_STATE.json. Execute the next pending task. Update the state. Do not proceed to the next task.",
    "PROGRAM_OS_STATE_SCHEMA.json": json.dumps({
        "program_name": "",
        "current_phase": "",
        "next_action": "",
        "documents": []
    }, indent=2),
    "PROGRAM_OS_DECISION_LOG_TEMPLATE.md": "# DECISION LOG\n\n| Date | Decision | Rationale | Alternatives Rejected |\n|---|---|---|---|",
    "PROGRAM_OS_RISK_REGISTER_TEMPLATE.md": "# RISK REGISTER\n\n| ID | Risk | Severity | Mitigation | Status |\n|---|---|---|---|---|",
    "PROGRAM_OS_AUDIT_TEMPLATE.md": "# AUDIT GATE REPORT\n\n**Scope:** Docs X to Y\n**Findings:**\n**Decision:** PASS/FAIL",
    "PROGRAM_OS_DOCUMENTATION_REGISTRY_TEMPLATE.md": "# DOCUMENTATION REGISTRY\n\n| ID | Title | Status | Word Count | Dependencies |\n|---|---|---|---|---|",
    "PROGRAM_OS_API_CALL_LOG_TEMPLATE.md": "# API CALL LOG\n\n| Timestamp | Task | Requested Engine | Executed Engine | Fallback? |\n|---|---|---|---|---|",
    "PROGRAM_OS_CANONICAL_FACTS_TEMPLATE.md": "# CANONICAL FACTS\n\n**Status:** LOCKED\n\nThese facts cannot be contradicted by generated documents.",
    "PROGRAM_OS_NEXT_ACTIONS_TEMPLATE.md": "# NEXT ACTIONS\n\n1. [ ] Task 1\n2. [ ] Task 2"
}

for name, content in templates.items():
    (YOS_DIR / name).write_text(content)

# Create placeholder files in the folder template
for folder in ["00_PROGRAM_OFFICE", "01_CANONICAL_FACTS", "02_KNOWLEDGE_BASE", "03_GENERATED_DOCS", "04_DATASETS", "05_EXPORTS", "99_AUDITS"]:
    (TEMPLATE_DIR / folder).mkdir(parents=True, exist_ok=True)
    (TEMPLATE_DIR / folder / ".gitkeep").write_text("")

(TEMPLATE_DIR / "00_PROGRAM_OFFICE" / "PROGRAM_STATE_TEMPLATE.json").write_text("{}")
(TEMPLATE_DIR / "00_PROGRAM_OFFICE" / "DOCUMENTATION_REGISTRY_TEMPLATE.json").write_text("{}")

print("PART I COMPLETE ✓")
