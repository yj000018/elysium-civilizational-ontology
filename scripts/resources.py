#!/usr/bin/env python3
"""
FCS Resources Script
Generates resource indexes and JSON outputs.

Usage:
    python scripts/resources.py
"""

import sys
import re
import json
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parent.parent
BOOK = REPO_ROOT / "BOOK"


def extract_frontmatter(filepath):
    """Extract YAML frontmatter fields."""
    content = filepath.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    fm_text = content[3:end]
    fields = {}
    current_key = None
    for line in fm_text.splitlines():
        m = re.match(r"^(\w[\w_]*):\s*(.+)$", line)
        if m and not line.startswith("  "):
            current_key = m.group(1)
            val = m.group(2).strip()
            if val == "[]":
                fields[current_key] = []
            else:
                fields[current_key] = val
            continue
        m2 = re.match(r"^\s+- (.+)$", line)
        if m2 and current_key:
            if not isinstance(fields.get(current_key), list):
                fields[current_key] = []
            fields[current_key].append(m2.group(1).strip())
        m3 = re.match(r"^(\w[\w_]*):\s*$", line)
        if m3:
            current_key = m3.group(1)
            fields[current_key] = {}
    return fields


def main():
    print("=" * 60)
    print("FCS RESOURCE INDEX GENERATION")
    print("=" * 60)

    resources = []
    concepts = set()
    concept_mentions = defaultdict(list)

    # Scan resources folder
    res_dir = BOOK / "resources"
    if res_dir.exists():
        for md in res_dir.rglob("*.md"):
            fields = extract_frontmatter(md)
            if fields.get("id"):
                resources.append({
                    "id": fields["id"],
                    "title": fields.get("title", ""),
                    "type": fields.get("type", ""),
                    "status": fields.get("status", ""),
                    "path": str(md.relative_to(REPO_ROOT)),
                })

    # Scan manuscript for concepts
    ms_dir = BOOK / "manuscript"
    if ms_dir.exists():
        for md in ms_dir.rglob("*.md"):
            fields = extract_frontmatter(md)
            if isinstance(fields.get("concepts"), list):
                for c in fields["concepts"]:
                    concepts.add(c)
                    concept_mentions[c].append(fields.get("id", str(md.relative_to(REPO_ROOT))))

    # Write resource index views
    ri_dir = BOOK / "views" / "resource_index"
    ri_dir.mkdir(parents=True, exist_ok=True)

    all_res = "# All Resources\n\n"
    if resources:
        all_res += "| ID | Title | Type | Status |\n|---|---|---|---|\n"
        for r in resources:
            all_res += f"| {r['id']} | {r['title']} | {r['type']} | {r['status']} |\n"
    else:
        all_res += "No resources indexed yet.\n"
    (ri_dir / "all_resources.md").write_text(all_res, encoding="utf-8")

    concept_idx = "# Concept Index\n\n"
    if concepts:
        concept_idx += "| Concept | Mentions |\n|---|---|\n"
        for c in sorted(concepts):
            concept_idx += f"| {c} | {len(concept_mentions[c])} |\n"
    else:
        concept_idx += "No concepts indexed yet.\n"
    (ri_dir / "concept_index.md").write_text(concept_idx, encoding="utf-8")

    # Category-specific indexes
    for cat in ["people", "institutions", "books", "websites", "movements"]:
        cat_res = [r for r in resources if r.get("type") == cat]
        idx = f"# {cat.title()} Index\n\n"
        if cat_res:
            idx += "| ID | Title | Status |\n|---|---|---|\n"
            for r in cat_res:
                idx += f"| {r['id']} | {r['title']} | {r['status']} |\n"
        else:
            idx += f"No {cat} resources indexed yet.\n"
        (ri_dir / f"{cat}_index.md").write_text(idx, encoding="utf-8")

    unverified = [r for r in resources if r.get("status") == "TO_VERIFY"]
    uv_idx = "# Unverified Resources\n\n"
    if unverified:
        uv_idx += "| ID | Title | Type |\n|---|---|---|\n"
        for r in unverified:
            uv_idx += f"| {r['id']} | {r['title']} | {r['type']} |\n"
    else:
        uv_idx += "No unverified resources.\n"
    (ri_dir / "unverified_resources.md").write_text(uv_idx, encoding="utf-8")

    # Write output indexes
    out_idx = BOOK / "output" / "indexes"
    out_idx.mkdir(parents=True, exist_ok=True)
    (out_idx / "resource_index.md").write_text(all_res, encoding="utf-8")
    (out_idx / "concept_index.md").write_text(concept_idx, encoding="utf-8")
    (out_idx / "bibliography_candidates.md").write_text("# Bibliography Candidates\n\nNo bibliography candidates yet.\n", encoding="utf-8")

    # Write JSON outputs
    out_json = BOOK / "output" / "json"
    out_json.mkdir(parents=True, exist_ok=True)
    (out_json / "resources.json").write_text(json.dumps(resources, indent=2), encoding="utf-8")
    (out_json / "concepts.json").write_text(json.dumps({"concepts": sorted(concepts), "mentions": dict(concept_mentions)}, indent=2, default=list), encoding="utf-8")

    # Search index
    search_index = []
    for r in resources:
        search_index.append({"id": r["id"], "title": r["title"], "type": "resource"})
    for c in sorted(concepts):
        search_index.append({"id": c, "title": c, "type": "concept"})
    (out_json / "search_index.json").write_text(json.dumps(search_index, indent=2), encoding="utf-8")

    print(f"\nResources indexed: {len(resources)}")
    print(f"Concepts indexed: {len(concepts)}")
    print(f"\nOutputs written to: BOOK/views/resource_index/ and BOOK/output/")


if __name__ == "__main__":
    main()
