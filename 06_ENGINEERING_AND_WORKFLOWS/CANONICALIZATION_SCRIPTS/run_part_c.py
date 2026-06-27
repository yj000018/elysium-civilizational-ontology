#!/usr/bin/env python3
import json
import os
from pathlib import Path

BASE = Path("/home/ubuntu/ELYSIUM_CANON")
ELYSIUM = BASE / "ELYSIUM"
DATE = "2026-06-27"

# Define the canonical document list with correct paths
documents = [
    {"id": "01", "title": "ELYSIUM Charter", "path": "ELYSIUM/01_FOUNDATIONAL_TEXTS/01_ELYSIUM_CHARTER.md", "folder": "01_FOUNDATIONAL_TEXTS"},
    {"id": "02", "title": "Founding Manifesto", "path": "ELYSIUM/01_FOUNDATIONAL_TEXTS/02_FOUNDING_MANIFESTO.md", "folder": "01_FOUNDATIONAL_TEXTS"},
    {"id": "03", "title": "Philosophical Constitution", "path": "ELYSIUM/01_FOUNDATIONAL_TEXTS/03_PHILOSOPHICAL_CONSTITUTION.md", "folder": "01_FOUNDATIONAL_TEXTS"},
    {"id": "04", "title": "Civilizational Principles", "path": "ELYSIUM/01_FOUNDATIONAL_TEXTS/04_CIVILIZATIONAL_PRINCIPLES.md", "folder": "01_FOUNDATIONAL_TEXTS"},
    {"id": "05", "title": "Core Ontology Overview", "path": "ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/05_CORE_ONTOLOGY_OVERVIEW.md", "folder": "02_ONTOLOGY_AND_KNOWLEDGE"},
    {"id": "06", "title": "Ontology Specification", "path": "ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/06_ONTOLOGY_SPECIFICATION.md", "folder": "02_ONTOLOGY_AND_KNOWLEDGE"},
    {"id": "07", "title": "Knowledge Graph Specification", "path": "ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/07_KNOWLEDGE_GRAPH_SPECIFICATION.md", "folder": "02_ONTOLOGY_AND_KNOWLEDGE"},
    {"id": "08", "title": "Research Methodology", "path": "ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/08_RESEARCH_METHODOLOGY.md", "folder": "02_ONTOLOGY_AND_KNOWLEDGE"},
    {"id": "09", "title": "Model Registry", "path": "ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/09_MODEL_REGISTRY.md", "folder": "02_ONTOLOGY_AND_KNOWLEDGE"},
    {"id": "10", "title": "Evidence Standards", "path": "ELYSIUM/02_ONTOLOGY_AND_KNOWLEDGE/10_EVIDENCE_STANDARDS.md", "folder": "02_ONTOLOGY_AND_KNOWLEDGE"},
    {"id": "11", "title": "Governance Handbook", "path": "ELYSIUM/03_GOVERNANCE/11_GOVERNANCE_HANDBOOK.md", "folder": "03_GOVERNANCE"},
    {"id": "12", "title": "Ontology Stewardship Council Handbook", "path": "ELYSIUM/03_GOVERNANCE/12_ONTOLOGY_STEWARDSHIP_COUNCIL_HANDBOOK.md", "folder": "03_GOVERNANCE"},
    {"id": "13", "title": "Community Contribution Guide", "path": "ELYSIUM/03_GOVERNANCE/13_COMMUNITY_CONTRIBUTION_GUIDE.md", "folder": "03_GOVERNANCE"},
    {"id": "14", "title": "Future Observatory Framework", "path": "ELYSIUM/04_OBSERVATORY/14_FUTURE_OBSERVATORY_FRAMEWORK.md", "folder": "04_OBSERVATORY"},
    {"id": "15", "title": "Civilization State Report Template", "path": "ELYSIUM/04_OBSERVATORY/15_CIVILIZATION_STATE_REPORT_TEMPLATE.md", "folder": "04_OBSERVATORY"},
    {"id": "16", "title": "Book Canon", "path": "ELYSIUM/05_APPLICATIONS/16_BOOK_CANON.md", "folder": "05_APPLICATIONS"},
    {"id": "17", "title": "Brand & Visual System", "path": "ELYSIUM/05_APPLICATIONS/17_BRAND_AND_VISUAL_SYSTEM.md", "folder": "05_APPLICATIONS"},
    {"id": "18", "title": "Website Architecture", "path": "ELYSIUM/05_APPLICATIONS/18_WEBSITE_ARCHITECTURE.md", "folder": "05_APPLICATIONS"},
    {"id": "19", "title": "Educational Framework", "path": "ELYSIUM/05_APPLICATIONS/19_EDUCATIONAL_FRAMEWORK.md", "folder": "05_APPLICATIONS"},
    {"id": "20", "title": "AI Ecosystem / Y-OS Integration", "path": "ELYSIUM/05_APPLICATIONS/20_AI_ECOSYSTEM_YOS_INTEGRATION.md", "folder": "05_APPLICATIONS"},
    {"id": "21", "title": "Roadmap", "path": "ELYSIUM/06_OPERATIONS_AND_LEGACY/21_ROADMAP.md", "folder": "06_OPERATIONS_AND_LEGACY"},
    {"id": "22", "title": "Version History", "path": "ELYSIUM/06_OPERATIONS_AND_LEGACY/22_VERSION_HISTORY.md", "folder": "06_OPERATIONS_AND_LEGACY"},
    {"id": "23", "title": "Partnership Framework", "path": "ELYSIUM/06_OPERATIONS_AND_LEGACY/23_PARTNERSHIP_FRAMEWORK.md", "folder": "06_OPERATIONS_AND_LEGACY"},
    {"id": "24", "title": "Historical Archive", "path": "ELYSIUM/06_OPERATIONS_AND_LEGACY/24_HISTORICAL_ARCHIVE.md", "folder": "06_OPERATIONS_AND_LEGACY"},
    {"id": "25", "title": "Legacy & Succession Framework", "path": "ELYSIUM/06_OPERATIONS_AND_LEGACY/25_LEGACY_AND_SUCCESSION_FRAMEWORK.md", "folder": "06_OPERATIONS_AND_LEGACY"},
    {"id": "26", "title": "AI Collaboration Constitution", "path": "ELYSIUM/03_GOVERNANCE/26_AI_COLLABORATION_CONSTITUTION.md", "folder": "03_GOVERNANCE"},
]

# Check existence and word count
for doc in documents:
    fp = BASE / doc["path"]
    doc["exists"] = fp.exists()
    if doc["exists"]:
        content = fp.read_text(errors="ignore")
        doc["word_count"] = len(content.split())
    else:
        doc["word_count"] = 0
    doc["status"] = "DRAFT_INTEGRATED_QA_PENDING"
    doc["canonicality"] = "DRAFT_INTEGRATED_QA_PENDING"
    doc["qa_state"] = "PENDING"

# Build synchronized Program State
program_state = {
    "program_name": "ELYSIUM",
    "phase": "Canonicalization / QA",
    "package_status": "Alpha generated package under canonicalization",
    "date": DATE,
    "documents_total": 26,
    "documents_status": "DRAFT_INTEGRATED_QA_PENDING",
    "ontology_status": "Structurally validated, canonicalization pending",
    "model_corpus": "126 analyzed + 10 candidates proposed",
    "facets": 38,
    "datasets": "QA pending",
    "api_routing": "Protocol repair required",
    "local_archive": "Incomplete until verified",
    "yos_program_os": "Pattern discovered, extraction pending",
    "next_action": "Complete QA + Canonicalization Pass 0.1",
    "documents": documents,
    "audits": [
        {"id": "01", "scope": "Docs 01-05", "status": "COMPLETED"},
        {"id": "02", "scope": "Docs 06-10", "status": "COMPLETED"},
        {"id": "03", "scope": "Docs 11-15", "status": "COMPLETED"},
        {"id": "04", "scope": "Docs 16-20", "status": "COMPLETED"},
        {"id": "05", "scope": "Docs 21-26", "status": "COMPLETED"},
    ]
}

# Build synchronized Documentation Registry
doc_registry = {
    "date": DATE,
    "total_documents": 26,
    "documents": []
}
for doc in documents:
    doc_registry["documents"].append({
        "id": doc["id"],
        "title": doc["title"],
        "file_path": doc["path"],
        "status": doc["status"],
        "exists": doc["exists"],
        "word_count": doc["word_count"],
        "qa_state": doc["qa_state"],
        "canonicality": doc["canonicality"],
        "dependencies": [],
        "notes": ""
    })

# Write Program State
state_md = f"""# ELYSIUM PROGRAM STATE

**Date:** {DATE}
**Phase:** Canonicalization / QA
**Package Status:** Alpha generated package under canonicalization

---

## Core Metrics

| Metric | Value |
|---|---|
| Documents | 26 (DRAFT_INTEGRATED_QA_PENDING) |
| Ontology | Structurally validated, canonicalization pending |
| Model Corpus | 126 analyzed + 10 candidates proposed |
| Facets | 38 canonical |
| Datasets | QA pending |
| API Routing | Protocol repair required |
| Local Archive | Incomplete until verified |
| yOS Program OS | Pattern discovered, extraction pending |
| Next Action | Complete QA + Canonicalization Pass 0.1 |

---

## Document Status

| ID | Title | Exists | Words | Status |
|---|---|---|---|---|
"""
for doc in documents:
    state_md += f"| {doc['id']} | {doc['title']} | {'✅' if doc['exists'] else '❌'} | {doc['word_count']} | {doc['status']} |\n"

# Save all files
(BASE / "00_PROGRAM_OFFICE" / "ELYSIUM_PROGRAM_STATE.md").write_text(state_md)
(BASE / "00_PROGRAM_OFFICE" / "ELYSIUM_PROGRAM_STATE.json").write_text(json.dumps(program_state, indent=2))
(BASE / "00_PROGRAM_OFFICE" / "DOCUMENTATION_REGISTRY.md").write_text(
    f"# DOCUMENTATION REGISTRY\n\n**Date:** {DATE}\n**Total:** 26 documents\n\nSee DOCUMENTATION_REGISTRY.json for full details.\n"
)
(BASE / "00_PROGRAM_OFFICE" / "DOCUMENTATION_REGISTRY.json").write_text(json.dumps(doc_registry, indent=2))

print("PART C COMPLETE ✓")
