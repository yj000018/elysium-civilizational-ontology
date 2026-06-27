#!/usr/bin/env python3
"""
FCS Status Script
Generates status reports for the FCS repository.

Usage:
    python scripts/status.py
"""

import sys
import re
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).resolve().parent.parent
BOOK = REPO_ROOT / "BOOK"


def extract_frontmatter_fields(filepath):
    """Extract key fields from YAML frontmatter."""
    content = filepath.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    fm = content[3:end]
    fields = {}
    for line in fm.splitlines():
        m = re.match(r"^(\w+):\s*(.+)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip()
    return fields


def word_count(filepath):
    """Count words in file body (after frontmatter)."""
    content = filepath.read_text(encoding="utf-8")
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            content = content[end + 3:]
    return len(content.split())


def main():
    print("=" * 60)
    print("FCS STATUS REPORT")
    print("=" * 60)

    # Content statuses
    content_statuses = Counter()
    types = Counter()
    total_words = 0
    node_count = 0

    for md in BOOK.rglob("*.md"):
        fields = extract_frontmatter_fields(md)
        if "status" in fields:
            content_statuses[fields["status"]] += 1
        if "type" in fields:
            types[fields["type"]] += 1
        if md.parent.name != "_fcs" and "templates" not in str(md):
            total_words += word_count(md)
            node_count += 1

    print(f"\n## Content Nodes: {node_count}")
    print(f"## Total Word Count: {total_words}")

    print("\n## Status Distribution")
    for status, count in content_statuses.most_common():
        print(f"  {status}: {count}")

    print("\n## Type Distribution")
    for t, count in types.most_common():
        print(f"  {t}: {count}")

    # Write reports
    dash_dir = BOOK / "views" / "dashboards"
    dash_dir.mkdir(parents=True, exist_ok=True)

    report = f"# Status Report\n\n"
    report += f"**Total nodes:** {node_count}\n"
    report += f"**Total word count:** {total_words}\n\n"
    report += "## Status Distribution\n\n"
    report += "| Status | Count |\n|---|---|\n"
    for status, count in content_statuses.most_common():
        report += f"| {status} | {count} |\n"
    report += "\n## Type Distribution\n\n"
    report += "| Type | Count |\n|---|---|\n"
    for t, count in types.most_common():
        report += f"| {t} | {count} |\n"

    (dash_dir / "STATUS_REPORT.md").write_text(report, encoding="utf-8")
    (dash_dir / "STRUCTURE_STATUS.md").write_text(report, encoding="utf-8")

    print(f"\nReports written to: BOOK/views/dashboards/")


if __name__ == "__main__":
    main()
