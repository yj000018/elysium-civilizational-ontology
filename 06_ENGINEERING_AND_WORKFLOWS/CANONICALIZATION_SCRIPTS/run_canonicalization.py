#!/usr/bin/env python3
"""
ELYSIUM Canonicalization Pass 0.1 - Master Script
Parts A through L executed sequentially.
"""
import os
import json
import csv
import re
import hashlib
from datetime import datetime
from pathlib import Path

BASE = Path("/home/ubuntu/ELYSIUM_CANON")
ELYSIUM = BASE / "ELYSIUM"
RESEARCH = BASE / "ELYSIUM_CIVILIZATIONAL_ONTOLOGY_RESEARCH"
NOW = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
DATE = "2026-06-27"

# Create canonical folder structure
CANONICAL_DIRS = [
    "00_PROGRAM_OFFICE",
    "01_CANONICAL_FACTS",
    "02_ONTOLOGY_AND_KNOWLEDGE",
    "02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES",
    "03_BOOK_AND_PUBLICATION",
    "04_DATASETS_AND_MATRICES",
    "04_DATASETS_AND_MATRICES/REPAIRED",
    "05_RESEARCH_CORPUS",
    "06_ENGINEERING_AND_WORKFLOWS",
    "07_YOS_PATTERN_LIBRARY",
    "YOS_PROGRAM_OS",
    "YOS_PROGRAM_OS/PROGRAM_OS_FOLDER_TEMPLATE",
    "99_FINAL_REPORTS",
]

for d in CANONICAL_DIRS:
    (BASE / d).mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("PART A: PACKAGE INTEGRITY AUDIT")
print("=" * 60)

# Collect all files
all_files = []
for root, dirs, files in os.walk(BASE):
    for f in files:
        fp = Path(root) / f
        rel = fp.relative_to(BASE)
        size = fp.stat().st_size
        all_files.append({
            "path": str(rel),
            "size": size,
            "extension": fp.suffix,
            "is_zero": size == 0
        })

# Check for issues
issues = []

# 1. Zero-byte files
for f in all_files:
    if f["is_zero"]:
        issues.append({"file": f["path"], "issue": "Zero-byte file", "severity": "HIGH"})

# 2. Duplicate content detection (by hash for files < 1MB)
hashes = {}
for f in all_files:
    fp = BASE / f["path"]
    if fp.stat().st_size > 0 and fp.stat().st_size < 1_000_000 and fp.suffix in [".md", ".json", ".csv", ".py"]:
        h = hashlib.md5(fp.read_bytes()).hexdigest()
        if h in hashes:
            issues.append({"file": f["path"], "issue": f"Duplicate of {hashes[h]}", "severity": "MEDIUM"})
        else:
            hashes[h] = f["path"]

# 3. Check for markdown code fence wrapping
for f in all_files:
    if f["extension"] == ".md":
        fp = BASE / f["path"]
        content = fp.read_text(errors="ignore")
        if content.strip().startswith("```") and content.strip().endswith("```"):
            issues.append({"file": f["path"], "issue": "Entire file wrapped in markdown code fences", "severity": "HIGH"})

# 4. Check for placeholder dates
placeholder_patterns = [r'\[Insert Date\]', r'\[Current Date\]', r'\[Date of Document Creation\]', r'\bTBD\b']
for f in all_files:
    if f["extension"] == ".md":
        fp = BASE / f["path"]
        content = fp.read_text(errors="ignore")
        for pat in placeholder_patterns:
            if re.search(pat, content):
                issues.append({"file": f["path"], "issue": f"Placeholder found: {pat}", "severity": "MEDIUM"})
                break

# 5. JSON validity check
for f in all_files:
    if f["extension"] == ".json" and f["size"] > 0:
        fp = BASE / f["path"]
        try:
            json.loads(fp.read_text(errors="ignore"))
        except json.JSONDecodeError as e:
            issues.append({"file": f["path"], "issue": f"Invalid JSON: {str(e)[:80]}", "severity": "CRITICAL"})

# 6. CSV validity check
for f in all_files:
    if f["extension"] == ".csv" and f["size"] > 0:
        fp = BASE / f["path"]
        try:
            with open(fp, 'r', errors='ignore') as csvf:
                reader = csv.reader(csvf)
                rows = list(reader)
                if len(rows) < 2:
                    issues.append({"file": f["path"], "issue": "CSV has fewer than 2 rows", "severity": "HIGH"})
        except Exception as e:
            issues.append({"file": f["path"], "issue": f"CSV parse error: {str(e)[:80]}", "severity": "HIGH"})

# 7. Check for status contradictions
status_files = [
    "ELYSIUM/00_PROGRAM_OFFICE/ELYSIUM_PROGRAM_STATE.json",
    "ELYSIUM/00_PROGRAM_OFFICE/DOCUMENTATION_REGISTRY.json"
]
for sf in status_files:
    fp = BASE / sf
    if fp.exists():
        content = fp.read_text(errors="ignore")
        if '"COMPLETE"' in content or '"FINAL"' in content:
            issues.append({"file": sf, "issue": "Claims COMPLETE/FINAL status prematurely", "severity": "HIGH"})

# 8. Check for CDN links that may be inaccessible
cdn_files = []
for f in all_files:
    if f["extension"] == ".json" and f["size"] > 0:
        fp = BASE / f["path"]
        content = fp.read_text(errors="ignore")
        if "manus.storage" in content or "cdn" in content.lower():
            cdn_files.append(f["path"])
            issues.append({"file": f["path"], "issue": "Contains CDN/external links that may be inaccessible", "severity": "MEDIUM"})

# 9. Check for model count inconsistencies
model_count_issues = []
for f in all_files:
    if f["extension"] in [".md", ".json"] and f["size"] > 0:
        fp = BASE / f["path"]
        content = fp.read_text(errors="ignore")
        if "136" in content and "model" in content.lower():
            model_count_issues.append(f["path"])

if model_count_issues:
    issues.append({"file": "; ".join(model_count_issues[:5]), "issue": "Claims 136 models (should be 126 confirmed + 10 candidates)", "severity": "HIGH"})

# Sort by severity
severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}
issues.sort(key=lambda x: severity_order.get(x["severity"], 5))

# Write audit report
audit_md = f"""# PACKAGE INTEGRITY AUDIT

**Date:** {DATE}
**Package:** ELYSIUM_EVERYTHING.zip
**Total files:** {len(all_files)}
**Total issues found:** {len(issues)}
**Auditor:** Manus (Executive Orchestrator)

---

## Summary by Severity

| Severity | Count |
|---|---|
| CRITICAL | {sum(1 for i in issues if i['severity'] == 'CRITICAL')} |
| HIGH | {sum(1 for i in issues if i['severity'] == 'HIGH')} |
| MEDIUM | {sum(1 for i in issues if i['severity'] == 'MEDIUM')} |
| LOW | {sum(1 for i in issues if i['severity'] == 'LOW')} |
| INFO | {sum(1 for i in issues if i['severity'] == 'INFO')} |

---

## Full File Inventory

| # | Path | Size (bytes) | Extension |
|---|---|---|---|
"""
for i, f in enumerate(sorted(all_files, key=lambda x: x["path"]), 1):
    audit_md += f"| {i} | `{f['path']}` | {f['size']} | {f['extension']} |\n"

audit_md += f"""
---

## Issues Detected

| # | Severity | File | Issue |
|---|---|---|---|
"""
for i, issue in enumerate(issues, 1):
    audit_md += f"| {i} | **{issue['severity']}** | `{issue['file'][:60]}` | {issue['issue'][:80]} |\n"

audit_md += f"""
---

## Top 20 Issues to Fix Before Next Creative Expansion

"""
for i, issue in enumerate(issues[:20], 1):
    audit_md += f"{i}. **[{issue['severity']}]** `{issue['file'][:50]}` — {issue['issue']}\n"

(BASE / "00_PROGRAM_OFFICE" / "PACKAGE_INTEGRITY_AUDIT.md").write_text(audit_md)

audit_json = {
    "date": DATE,
    "total_files": len(all_files),
    "total_issues": len(issues),
    "issues_by_severity": {
        "CRITICAL": sum(1 for i in issues if i['severity'] == 'CRITICAL'),
        "HIGH": sum(1 for i in issues if i['severity'] == 'HIGH'),
        "MEDIUM": sum(1 for i in issues if i['severity'] == 'MEDIUM'),
        "LOW": sum(1 for i in issues if i['severity'] == 'LOW'),
        "INFO": sum(1 for i in issues if i['severity'] == 'INFO'),
    },
    "files": all_files,
    "issues": issues,
    "cdn_files": cdn_files,
    "model_count_inconsistencies": model_count_issues
}
(BASE / "00_PROGRAM_OFFICE" / "PACKAGE_INTEGRITY_AUDIT.json").write_text(json.dumps(audit_json, indent=2))

print(f"  Total files: {len(all_files)}")
print(f"  Issues found: {len(issues)}")
print(f"  CRITICAL: {audit_json['issues_by_severity']['CRITICAL']}")
print(f"  HIGH: {audit_json['issues_by_severity']['HIGH']}")
print(f"  MEDIUM: {audit_json['issues_by_severity']['MEDIUM']}")
print("  Audit saved to 00_PROGRAM_OFFICE/PACKAGE_INTEGRITY_AUDIT.md/.json")
print("  PART A COMPLETE ✓")
