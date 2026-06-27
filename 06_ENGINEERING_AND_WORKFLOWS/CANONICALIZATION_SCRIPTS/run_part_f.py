#!/usr/bin/env python3
"""Part F: Model Count Reconciliation — reconcile 126 vs 136 claims."""
import json
from pathlib import Path

BASE = Path("/home/ubuntu/ELYSIUM_CANON")
DATE = "2026-06-27"

# Load all lot data to get the actual model list
lot_files = [
    ("A", BASE / "lot_a_human_development.json"),
    ("B", BASE / "lot_b_civilization_sustainability.json"),
    ("C", BASE / "lot_c_systems_complexity.json"),
    ("D", BASE / "lot_d_ecology_regeneration.json"),
    ("E", BASE / "lot_e_economy_technology_future.json"),
    ("F", BASE / "lot_f_philosophy_spirituality.json"),
    ("G", BASE / "lot_g_discovered_models.json"),
    ("H", BASE / "lot_h_missing_models.json"),
]

all_models = []
for lot_name, lot_file in lot_files:
    if not lot_file.exists():
        continue
    data = json.loads(lot_file.read_text())
    results = data.get("results", [])
    for item in results:
        output = item.get("output", {})
        if isinstance(output, dict):
            model_name = output.get("model_name", output.get("name", ""))
            author = output.get("author", output.get("creator", ""))
        else:
            model_name = ""
            author = ""
        
        inp = item.get("input", "")
        if not model_name:
            # Try to extract from input
            model_name = inp.split("—")[0].strip() if "—" in inp else inp[:60]
        
        all_models.append({
            "lot": lot_name,
            "model_name": model_name,
            "author": author,
            "status": "ANALYZED" if lot_name in "ABCDEFG" else "ANALYZED_LATE_ADDITION"
        })

# The 10 candidates from Stage 5
candidates = [
    "Collective Intelligence (Lévy/Malone)",
    "Integrated Information Theory (Tononi)",
    "Cultural Evolution (Boyd/Richerson/Henrich)",
    "Earth System Governance (Biermann)",
    "Afrofuturism/Afrotopia (Sarr/Mbembe)",
    "Digital Civilization (Floridi/Zuboff/Lessig)",
    "Relational Ontology/Pluriverse (Escobar)",
    "Metamodernism (Freinacht)",
    "Network Science (Barabási)",
    "Cosmolocalism (Ramos/Bauwens)",
]

# Build reconciliation report
report = f"""# MODEL COUNT RECONCILIATION

**Date:** {DATE}
**Auditor:** Manus (Executive Orchestrator)

---

## Canonical Count

| Category | Count | Status |
|---|---|---|
| Lots A-G (original research) | {sum(1 for m in all_models if m['lot'] in 'ABCDEFG')} | ANALYZED — canonical |
| Lot H (gap-fill additions) | {sum(1 for m in all_models if m['lot'] == 'H')} | ANALYZED — canonical |
| **Total Analyzed** | **{len(all_models)}** | **CANONICAL** |
| Stage 5 Candidates | 10 | PROPOSED — not yet integrated |
| **Total Including Candidates** | **{len(all_models) + 10}** | **MIXED** |

---

## Reconciliation Decision

The canonical model count is **{len(all_models)} analyzed models**.

The 10 candidates from Stage 5 are **PROPOSED** only. They have not been through the full analysis pipeline (12-step extraction, matrix mapping, coverage scoring). Until they are, the correct claim is:

> **{len(all_models)} models analyzed and integrated + 10 candidates proposed.**

Any document claiming "136 models" must be corrected to "{len(all_models)} + 10 candidates" unless the candidates have been fully processed.

---

## Model List by Lot

| # | Lot | Model Name | Status |
|---|---|---|---|
"""
for i, m in enumerate(all_models, 1):
    report += f"| {i} | {m['lot']} | {m['model_name'][:60]} | {m['status']} |\n"

report += f"""
---

## Candidate Models (NOT YET CANONICAL)

| # | Model | Status |
|---|---|---|
"""
for i, c in enumerate(candidates, 1):
    report += f"| {i} | {c} | PROPOSED |\n"

report += f"""
---

## Files Requiring Correction

Files that claim "136 models" must be updated to "{len(all_models)} analyzed + 10 candidates":
"""

# Scan for files claiming 136
files_to_fix = []
for fp in BASE.rglob("*.md"):
    content = fp.read_text(errors="ignore")
    if "136" in content and ("model" in content.lower() or "modèle" in content.lower()):
        files_to_fix.append(str(fp.relative_to(BASE)))
        report += f"- `{fp.relative_to(BASE)}`\n"

for fp in BASE.rglob("*.json"):
    content = fp.read_text(errors="ignore")
    if '"136"' in content or ": 136" in content:
        files_to_fix.append(str(fp.relative_to(BASE)))
        report += f"- `{fp.relative_to(BASE)}`\n"

# Save
(BASE / "00_PROGRAM_OFFICE" / "MODEL_COUNT_RECONCILIATION.md").write_text(report)

reconciliation_json = {
    "date": DATE,
    "canonical_analyzed": len(all_models),
    "candidates_proposed": 10,
    "total_claimed_incorrect": len(all_models) + 10,
    "correct_statement": f"{len(all_models)} models analyzed and integrated + 10 candidates proposed",
    "files_requiring_correction": files_to_fix,
    "models": all_models,
    "candidates": candidates
}
(BASE / "00_PROGRAM_OFFICE" / "MODEL_COUNT_RECONCILIATION.json").write_text(json.dumps(reconciliation_json, indent=2))

# Also save canonical model registry
(BASE / "05_RESEARCH_CORPUS" / "CANONICAL_MODEL_REGISTRY.json").write_text(json.dumps({
    "date": DATE,
    "total_analyzed": len(all_models),
    "total_candidates": 10,
    "models": all_models,
    "candidates": [{"name": c, "status": "PROPOSED"} for c in candidates]
}, indent=2))

print(f"  Total analyzed models: {len(all_models)}")
print(f"  Candidates proposed: 10")
print(f"  Files requiring correction: {len(files_to_fix)}")
print("PART F COMPLETE ✓")
