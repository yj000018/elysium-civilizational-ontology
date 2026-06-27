#!/usr/bin/env python3
"""
FCS Validate Script
Validates the FCS repository structure for common issues.

Usage:
    python scripts/validate.py
"""

import sys
import os
import re
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).resolve().parent.parent
BOOK = REPO_ROOT / "BOOK"

ALLOWED_CONTENT_STATUSES = {
    "PLANNED", "SCAFFOLDED", "DRAFT", "AI_PROPOSAL_READY",
    "REVIEW_PENDING", "REVISION_REQUIRED", "REVISED", "LOCKED"
}
ALLOWED_ACTION_STATUSES = {
    "DRAFT_ACTION", "READY_FOR_AI", "IN_PROGRESS",
    "AI_PROPOSAL_READY", "COMPLETED", "BLOCKED", "ARCHIVED"
}
ALLOWED_RESOURCE_STATUSES = {
    "IDENTIFIED", "TO_VERIFY", "VERIFIED", "CANONICAL_SOURCE",
    "NON_CANONICAL_TEXTURE", "MENTION_ONLY", "REJECTED", "ARCHIVED"
}

ALL_STATUSES = ALLOWED_CONTENT_STATUSES | ALLOWED_ACTION_STATUSES | ALLOWED_RESOURCE_STATUSES

errors = []
warnings = []


def extract_frontmatter_fields(filepath):
    """Extract key fields from YAML frontmatter (simple parser)."""
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


def validate_ids():
    """Check for duplicate IDs across all nodes (excluding generated views/output)."""
    ids = Counter()
    exclude_dirs = {"views", "output", "reviews"}
    for md in BOOK.rglob("*.md"):
        # Skip generated output directories
        rel = md.relative_to(BOOK)
        if rel.parts and rel.parts[0] in exclude_dirs:
            continue
        fields = extract_frontmatter_fields(md)
        if "id" in fields:
            ids[fields["id"]] += 1
    for id_val, count in ids.items():
        if count > 1:
            errors.append(f"Duplicate ID: {id_val} (found {count} times)")


def validate_statuses():
    """Check that all statuses are in allowed sets."""
    for md in BOOK.rglob("*.md"):
        fields = extract_frontmatter_fields(md)
        if "status" in fields:
            status = fields["status"]
            if status not in ALL_STATUSES:
                warnings.append(f"Unknown status '{status}' in {md.relative_to(REPO_ROOT)}")


def validate_manifests():
    """Check that manifest includes point to existing files."""
    for manifest in BOOK.rglob("manifest.md"):
        content = manifest.read_text(encoding="utf-8")
        in_include = False
        for line in content.splitlines():
            if line.strip() == "## Include":
                in_include = True
                continue
            if in_include:
                if line.startswith("## "):
                    break
                m = re.match(r"^- (.+)$", line.strip())
                if m:
                    inc_path = manifest.parent / m.group(1).strip()
                    if not inc_path.exists() and not (manifest.parent / m.group(1).strip()).is_dir():
                        warnings.append(f"Manifest include missing: {m.group(1)} in {manifest.relative_to(REPO_ROOT)}")


def validate_folder_nodes():
    """Check that important folder nodes have index.md."""
    manuscript = BOOK / "manuscript"
    if not manuscript.exists():
        errors.append("BOOK/manuscript/ does not exist")
        return
    for d in manuscript.rglob("*"):
        if d.is_dir() and any(d.iterdir()):
            # Skip modules/ folders
            if d.name == "modules":
                continue
            index = d / "index.md"
            if not index.exists():
                warnings.append(f"Folder node missing index.md: {d.relative_to(REPO_ROOT)}")


def validate_summaries():
    """Check that important nodes have summaries."""
    for md in (BOOK / "manuscript").rglob("index.md"):
        fields = extract_frontmatter_fields(md)
        if not fields.get("summary"):
            warnings.append(f"Missing summary: {md.relative_to(REPO_ROOT)}")


def main():
    print("=" * 60)
    print("FCS VALIDATION REPORT")
    print("=" * 60)

    validate_ids()
    validate_statuses()
    validate_manifests()
    validate_folder_nodes()
    validate_summaries()

    print(f"\nErrors: {len(errors)}")
    for e in errors:
        print(f"  [ERROR] {e}")

    print(f"\nWarnings: {len(warnings)}")
    for w in warnings:
        print(f"  [WARN]  {w}")

    print(f"\nTotal: {len(errors)} errors, {len(warnings)} warnings")

    # Write report
    report_dir = BOOK / "views" / "dashboards"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / "VALIDATION_REPORT.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Validation Report\n\n")
        f.write(f"**Errors:** {len(errors)}\n")
        f.write(f"**Warnings:** {len(warnings)}\n\n")
        if errors:
            f.write("## Errors\n\n")
            for e in errors:
                f.write(f"- {e}\n")
            f.write("\n")
        if warnings:
            f.write("## Warnings\n\n")
            for w in warnings:
                f.write(f"- {w}\n")
            f.write("\n")
        if not errors and not warnings:
            f.write("No issues found.\n")

    print(f"\nReport written to: {report_path.relative_to(REPO_ROOT)}")

    if errors:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
