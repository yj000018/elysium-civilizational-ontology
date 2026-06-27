#!/usr/bin/env python3
"""Part D v2: Facet Archive Recovery — download from CDN links and save locally."""
import json
import requests
import re
import time
from pathlib import Path

BASE = Path("/home/ubuntu/ELYSIUM_CANON")
FACET_DIR = BASE / "02_ONTOLOGY_AND_KNOWLEDGE" / "FACET_MATRICES"
FACET_DIR.mkdir(parents=True, exist_ok=True)
DATE = "2026-06-27"

# Foundation mapping for naming
FOUNDATION_MAP = {
    "FOUNDATION": "F01",
    "VITALITÉ": "F02",
    "VITALITY": "F02",
    "AGENTIVITÉ": "F03",
    "AGENCY": "F03",
    "COHÉSION": "F04",
    "COHESION": "F04",
    "GOUVERNANCE": "F05",
    "GOVERNANCE": "F05",
    "VISION": "F06",
    "CONSCIENCE": "F07",
    "CONSCIOUSNESS": "F07",
}

batch_files = [
    BASE / "facets_12_steps_batch_1.json",
    BASE / "facets_12_steps_batch_2.json",
    BASE / "remaining_facets_gouvernance.json",
    BASE / "remaining_facets_conscience.json",
]

recovered = []
missing = []
facet_counter = {}

for bf in batch_files:
    if not bf.exists():
        print(f"  SKIP: {bf.name} not found")
        continue
    
    data = json.loads(bf.read_text())
    results = data.get("results", [])
    print(f"  Processing {bf.name}: {len(results)} items")
    
    for item in results:
        inp = item.get("input", "")
        output = item.get("output", {})
        
        if not isinstance(output, dict):
            missing.append({"input": inp[:60], "reason": "Output is not a dict"})
            continue
        
        # Get CDN URL
        cdn_url = output.get("chapter_content", "")
        facet_name = output.get("facet_name", "")
        
        # Parse foundation from input
        foundation = ""
        for key in FOUNDATION_MAP:
            if key in inp.upper():
                foundation = key
                break
        
        fcode = FOUNDATION_MAP.get(foundation, "FXX")
        
        # Track facet number within foundation
        if fcode not in facet_counter:
            facet_counter[fcode] = 0
        facet_counter[fcode] += 1
        facet_num = facet_counter[fcode]
        
        # Generate safe filename
        safe_facet = re.sub(r'[^a-zA-Z0-9_]', '_', facet_name[:40]) if facet_name else f"facet_{facet_num}"
        filename = f"{fcode}_{facet_num:02d}_{safe_facet}.md"
        
        # Try to download from CDN
        content = ""
        if cdn_url and cdn_url.startswith("http"):
            try:
                r = requests.get(cdn_url, timeout=15)
                if r.status_code == 200:
                    content = r.text
            except Exception as e:
                pass
        
        if content and len(content) > 100:
            front_matter = f"""---
facet_id: {fcode}_{facet_num:02d}
foundation: {foundation}
facet_name: {facet_name}
scale_relevance: Human, Society, Civilization
matrix_status: 12-step complete
source_link: {cdn_url[:100] if cdn_url else 'local'}
recovered_at: {DATE}
status: RECOVERED_DRAFT_QA_PENDING
---

"""
            (FACET_DIR / filename).write_text(front_matter + content)
            recovered.append({
                "filename": filename,
                "foundation": foundation,
                "facet": facet_name,
                "words": len(content.split()),
                "status": "RECOVERED_DRAFT_QA_PENDING"
            })
            print(f"    ✓ {filename} ({len(content.split())} words)")
        else:
            missing.append({
                "filename": filename,
                "foundation": foundation,
                "facet": facet_name,
                "source_link": cdn_url[:100] if cdn_url else "",
                "reason": "CDN link inaccessible or empty content"
            })
            print(f"    ✗ {filename} — MISSING")
        
        time.sleep(0.2)  # Be gentle with CDN

# Also recover foundation-level matrices from research
matrices_dir = BASE / "ELYSIUM_CIVILIZATIONAL_ONTOLOGY_RESEARCH" / "matrices"
if matrices_dir.exists():
    for mf in sorted(matrices_dir.iterdir()):
        if mf.suffix == ".md":
            content = mf.read_text(errors="ignore")
            dest = FACET_DIR / f"FOUNDATION_MATRIX_{mf.stem}.md"
            front_matter = f"""---
facet_id: FOUNDATION_LEVEL
foundation: {mf.stem}
facet_name: Foundation-level 12-step matrix
scale_relevance: Human, Society, Civilization
matrix_status: 12-step complete
source_link: local_research_corpus
recovered_at: {DATE}
status: RECOVERED_DRAFT_QA_PENDING
---

"""
            dest.write_text(front_matter + content)
            recovered.append({"filename": dest.name, "foundation": mf.stem, "facet": "Foundation-level matrix", "words": len(content.split()), "status": "RECOVERED_DRAFT_QA_PENDING"})

# Write updated index
index_md = f"""# FACET MATRICES INDEX

**Date:** {DATE}
**Total Recovered:** {len(recovered)}
**Total Missing:** {len(missing)}
**Target:** 38 facets + 7 foundation-level matrices = 45 files

---

## Recovered Files

| # | Filename | Foundation | Facet | Words | Status |
|---|---|---|---|---|---|
"""
for i, r in enumerate(recovered, 1):
    index_md += f"| {i} | `{r['filename']}` | {r['foundation']} | {r['facet']} | {r['words']} | {r['status']} |\n"

if missing:
    index_md += f"""
---

## Missing Files

| # | Filename | Foundation | Facet | Reason |
|---|---|---|---|---|
"""
    for i, m in enumerate(missing, 1):
        index_md += f"| {i} | `{m.get('filename', 'N/A')}` | {m.get('foundation', 'N/A')} | {m.get('facet', 'N/A')} | {m.get('reason', 'Unknown')} |\n"

index_md += f"""
---

## Summary

All 38 facet files locally archived: **{'YES' if len(missing) == 0 else 'NO — ' + str(len(missing)) + ' missing'}**
"""

(FACET_DIR / "FACET_MATRICES_INDEX.md").write_text(index_md)
(FACET_DIR / "FACET_MATRICES_INDEX.json").write_text(json.dumps({"recovered": recovered, "missing": missing, "total_recovered": len(recovered), "total_missing": len(missing)}, indent=2))

# Update missing assets
(BASE / "00_PROGRAM_OFFICE" / "MISSING_ASSETS.md").write_text(
    f"# MISSING ASSETS\n\n**Date:** {DATE}\n**Total Missing:** {len(missing)}\n\n" +
    ("No missing assets — all facets recovered locally.\n" if not missing else
     "\n".join([f"- `{m.get('filename')}`: {m.get('reason')}" for m in missing]))
)
(BASE / "00_PROGRAM_OFFICE" / "MISSING_ASSETS.json").write_text(json.dumps({"missing": missing}, indent=2))

print(f"\n  TOTAL Recovered: {len(recovered)} files")
print(f"  TOTAL Missing: {len(missing)} files")
print("PART D v2 COMPLETE ✓")
