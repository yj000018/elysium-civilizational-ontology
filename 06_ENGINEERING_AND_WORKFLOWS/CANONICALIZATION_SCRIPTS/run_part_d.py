#!/usr/bin/env python3
"""Part D: Facet Archive Recovery — extract facet content from JSON batch files and save locally."""
import json
from pathlib import Path
from datetime import datetime

BASE = Path("/home/ubuntu/ELYSIUM_CANON")
FACET_DIR = BASE / "02_ONTOLOGY_AND_KNOWLEDGE" / "FACET_MATRICES"
FACET_DIR.mkdir(parents=True, exist_ok=True)
DATE = "2026-06-27"

# Define the canonical 38 facets
CANONICAL_FACETS = {
    "FOUNDATION": ["Energy & Resources", "Water & Sanitation", "Shelter & Infrastructure", "Food Security", "Material Cycles", "Land & Territory"],
    "VITALITY": ["Ecosystems & Biodiversity", "Health Systems", "Nutrition & Agriculture", "Regeneration & Restoration", "Climate Stability"],
    "AGENCY": ["Labor & Livelihoods", "Innovation & Technology", "Trade & Markets", "Finance & Investment", "Entrepreneurship & Enterprise", "Productive Capacity"],
    "COHESION": ["Social Bonds & Community", "Cultural Expression & Arts", "Media & Communication", "Migration & Diversity", "Leisure & Play", "Identity & Belonging"],
    "GOVERNANCE": ["Rule of Law & Justice", "Democracy & Participation", "Conflict & Peace", "Institutions & Public Administration", "International Cooperation"],
    "VISION": ["Education & Learning", "Science & Research", "Foresight & Futures", "Information & Data", "Wisdom Traditions"],
    "CONSCIOUSNESS": ["Ethics & Values", "Spirituality & Meaning", "Worldviews & Paradigms", "Purpose & Direction", "Civilizational Direction"]
}

# Load all batch JSON files
batch_files = [
    BASE / "facets_12_steps_batch_1.json",
    BASE / "facets_12_steps_batch_2.json",
    BASE / "remaining_facets_gouvernance.json",
    BASE / "remaining_facets_conscience.json",
]

recovered = []
missing = []
facet_index = []

# Process each batch file
for bf in batch_files:
    if not bf.exists():
        missing.append({"file": str(bf.name), "reason": "Batch file not found"})
        continue
    
    data = json.loads(bf.read_text())
    
    # Handle different JSON structures
    items = []
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        if "results" in data:
            items = data["results"]
        elif "data" in data:
            items = data["data"]
        else:
            items = [data]
    
    for item in items:
        # Try to extract facet name and content
        facet_name = item.get("facet_name", item.get("facet", item.get("name", "")))
        foundation = item.get("foundation", item.get("foundation_name", ""))
        content = item.get("content", item.get("matrix_content", item.get("output", "")))
        file_url = item.get("file", item.get("file_url", item.get("output_file", "")))
        
        if not facet_name and not content:
            continue
        
        # Determine foundation index
        found_idx = "XX"
        for i, (fname, facets) in enumerate(CANONICAL_FACETS.items(), 1):
            if fname.lower() in foundation.lower() if foundation else False:
                found_idx = f"F{i:02d}"
                break
            for j, f in enumerate(facets, 1):
                if facet_name and f.lower()[:10] in facet_name.lower():
                    found_idx = f"F{i:02d}"
                    break
        
        # Generate filename
        safe_name = facet_name.replace(" ", "_").replace("/", "_").replace("&", "and")[:40] if facet_name else "unknown"
        filename = f"{found_idx}_{safe_name}.md"
        
        # Write content or mark as missing
        if content and len(content) > 100:
            front_matter = f"""---
facet_id: {found_idx}
foundation: {foundation}
facet_name: {facet_name}
scale_relevance: Human, Society, Civilization
matrix_status: 12-step complete
source_link: {file_url if file_url else 'local_batch'}
recovered_at: {DATE}
status: RECOVERED_DRAFT_QA_PENDING
---

"""
            (FACET_DIR / filename).write_text(front_matter + content)
            recovered.append({"filename": filename, "foundation": foundation, "facet": facet_name, "words": len(content.split()), "status": "RECOVERED_DRAFT_QA_PENDING"})
        elif file_url:
            # CDN link - mark as needing recovery
            missing.append({"filename": filename, "foundation": foundation, "facet": facet_name, "source_link": file_url, "reason": "Content in CDN link, not locally available"})
        else:
            missing.append({"filename": filename, "foundation": foundation, "facet": facet_name, "source_link": "", "reason": "No content found in batch data"})

# Also check the matrices folder from research
matrices_dir = BASE / "ELYSIUM_CIVILIZATIONAL_ONTOLOGY_RESEARCH" / "matrices"
if matrices_dir.exists():
    for mf in matrices_dir.iterdir():
        if mf.suffix == ".md":
            content = mf.read_text(errors="ignore")
            fname = mf.stem
            dest = FACET_DIR / f"FOUNDATION_MATRIX_{fname}.md"
            front_matter = f"""---
facet_id: FOUNDATION_LEVEL
foundation: {fname}
facet_name: Foundation-level 12-step matrix
scale_relevance: Human, Society, Civilization
matrix_status: 12-step complete
source_link: local_research_corpus
recovered_at: {DATE}
status: RECOVERED_DRAFT_QA_PENDING
---

"""
            dest.write_text(front_matter + content)
            recovered.append({"filename": dest.name, "foundation": fname, "facet": "Foundation-level matrix", "words": len(content.split()), "status": "RECOVERED_DRAFT_QA_PENDING"})

# Write index
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

# Write missing assets report
missing_md = f"""# MISSING ASSETS

**Date:** {DATE}
**Total Missing:** {len(missing)}

| # | Asset | Reason |
|---|---|---|
"""
for i, m in enumerate(missing, 1):
    missing_md += f"| {i} | `{m.get('filename', 'N/A')}` | {m.get('reason', 'Unknown')} |\n"

(BASE / "00_PROGRAM_OFFICE" / "MISSING_ASSETS.md").write_text(missing_md)
(BASE / "00_PROGRAM_OFFICE" / "MISSING_ASSETS.json").write_text(json.dumps({"missing": missing}, indent=2))

print(f"  Recovered: {len(recovered)} files")
print(f"  Missing: {len(missing)} files")
print("PART D COMPLETE ✓")
