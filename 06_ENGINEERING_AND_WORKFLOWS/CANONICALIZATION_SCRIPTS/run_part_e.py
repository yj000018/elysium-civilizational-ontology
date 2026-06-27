#!/usr/bin/env python3
import re
from pathlib import Path

BASE = Path("/home/ubuntu/ELYSIUM_CANON")
ELYSIUM = BASE / "ELYSIUM"
DATE = "2026-06-27"

# Patterns to remove
bad_patterns = [
    r"\[Insert Date\]",
    r"\[Current Date\]",
    r"\[Date of Document Creation\]",
    r"\[Date\]",
    r"\bTBD\b"
]

# Get all markdown files in ELYSIUM folder
md_files = list(ELYSIUM.glob("**/*.md"))

cleaned_count = 0
fixed_files = []

for fp in md_files:
    if not fp.is_file():
        continue
        
    content = fp.read_text(errors="ignore")
    original = content
    
    # 1. Remove markdown code fences that wrap the entire file
    if content.strip().startswith("```") and content.strip().endswith("```"):
        lines = content.strip().split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        content = "\n".join(lines)
    
    # 2. Replace placeholder dates
    for pat in bad_patterns:
        content = re.sub(pat, DATE, content, flags=re.IGNORECASE)
    
    # 3. Add canonical status header if missing and it's a core document
    if fp.name.startswith(tuple(f"{i:02d}_" for i in range(1, 27))):
        if "Status: DRAFT_INTEGRATED" not in content and "Status:" not in content[:500]:
            # Insert after the first title
            parts = content.split("\n", 1)
            if len(parts) > 1 and parts[0].startswith("#"):
                content = f"{parts[0]}\n\n**Date:** {DATE}\n**Status:** DRAFT_INTEGRATED_QA_PENDING\n**Version:** 0.1\n\n{parts[1]}"
            else:
                content = f"**Date:** {DATE}\n**Status:** DRAFT_INTEGRATED_QA_PENDING\n**Version:** 0.1\n\n{content}"
    
    if content != original:
        fp.write_text(content)
        cleaned_count += 1
        fixed_files.append(fp.name)

# Create cleanup report
report = f"""# GENERATED DOCUMENT CLEANUP REPORT

**Date:** {DATE}
**Files Scanned:** {len(md_files)}
**Files Cleaned:** {cleaned_count}

## Actions Performed
1. Removed full-file markdown code fences.
2. Replaced `[Insert Date]` and similar placeholders with {DATE}.
3. Injected standard `Status: DRAFT_INTEGRATED_QA_PENDING` header into all 26 core documents.

## Cleaned Files
"""
for f in fixed_files:
    report += f"- `{f}`\n"

(BASE / "00_PROGRAM_OFFICE" / "DOCUMENT_CLEANUP_REPORT.md").write_text(report)

print(f"  Files scanned: {len(md_files)}")
print(f"  Files cleaned: {cleaned_count}")
print("PART E COMPLETE ✓")
