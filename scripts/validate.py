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

ALLOWED_AGENTS = {
    "CHATGPT_CHIEF_ARCHITECT", "CLAUDE_WRITER", "CLAUDE_REVIEWER",
    "MANUS_OPERATOR", "FCS_SCRIPTS", "FOUNDER"
}

ALLOWED_WRITEBACK_MODES = {
    "proposal", "direct_write", "patch", "review_only", "direct_write_to_resources_pending"
}

errors = []
warnings = []
infos = []


def extract_frontmatter_fields(filepath):
    """Extract key fields from YAML frontmatter (supports 2-level nesting)."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return {}
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    fm = content[3:end]
    fields = {}
    current_key = None
    current_subkey = None
    for line in fm.splitlines():
        # Top-level key with value: "key: value"
        m = re.match(r"^(\w+):\s*(.+)$", line)
        if m and not line.startswith(" "):
            current_key = m.group(1)
            current_subkey = None
            val = m.group(2).strip()
            if val == "[]":
                fields[current_key] = []
            elif val.startswith("["):
                fields[current_key] = []
            elif val in ("null", "~"):
                fields[current_key] = None
            else:
                fields[current_key] = val
            continue
        # Top-level key without value: "key:" (starts a dict or list)
        m3 = re.match(r"^(\w+):\s*$", line)
        if m3 and not line.startswith(" "):
            current_key = m3.group(1)
            current_subkey = None
            fields[current_key] = {}
            continue
        # Sub-key (2-space indent): "  subkey: value" or "  subkey:"
        m_sub = re.match(r"^  (\w+):\s*(.*)$", line)
        if m_sub and current_key is not None:
            subkey = m_sub.group(1)
            subval = m_sub.group(2).strip()
            current_subkey = subkey
            if not isinstance(fields.get(current_key), dict):
                fields[current_key] = {}
            if subval == "[]" or subval == "":
                fields[current_key][subkey] = []
            elif subval in ("null", "~"):
                fields[current_key][subkey] = None
            elif subval.startswith("["):
                fields[current_key][subkey] = []
            else:
                fields[current_key][subkey] = subval
            continue
        # List item at 4-space indent (under a sub-key): "    - item"
        m_deep = re.match(r"^    - (.+)$", line)
        if m_deep and current_key and current_subkey:
            if isinstance(fields.get(current_key), dict):
                if not isinstance(fields[current_key].get(current_subkey), list):
                    fields[current_key][current_subkey] = []
                fields[current_key][current_subkey].append(m_deep.group(1).strip())
            continue
        # List item at 2-space indent (under a top-level key): "  - item"
        m2 = re.match(r"^  - (.+)$", line)
        if m2 and current_key:
            current_subkey = None
            if isinstance(fields.get(current_key), dict):
                # Convert to list if first item encountered directly
                fields[current_key] = [m2.group(1).strip()]
            elif isinstance(fields.get(current_key), list):
                fields[current_key].append(m2.group(1).strip())
            else:
                fields[current_key] = [m2.group(1).strip()]
            continue
    return fields


def validate_ids(target_dir):
    """Check for duplicate IDs across all nodes (excluding generated views/output)."""
    ids = Counter()
    exclude_dirs = {"views", "output", "reviews", "templates", "_fcs"}
    all_ids = set()
    for md in target_dir.rglob("*.md"):
        rel = md.relative_to(target_dir) if target_dir in md.parents else md
        if rel.parts and rel.parts[0] in exclude_dirs and target_dir.name == "BOOK":
            continue
        fields = extract_frontmatter_fields(md)
        if "id" in fields:
            ids[fields["id"]] += 1
            all_ids.add(fields["id"])
    for id_val, count in ids.items():
        if count > 1:
            errors.append(f"Duplicate ID: {id_val} (found {count} times)")
    return all_ids


def validate_statuses(target_dir):
    """Check that all statuses are in allowed sets."""
    for md in target_dir.rglob("*.md"):
        if target_dir.name == "BOOK" and ("_fcs" in md.parts or "templates" in md.parts):
            continue
        fields = extract_frontmatter_fields(md)
        if "status" in fields:
            status = fields["status"]
            if status not in ALL_STATUSES:
                errors.append(f"Unknown status '{status}' in {md.relative_to(REPO_ROOT)}")


def validate_manifests(target_dir):
    """Check that manifest includes point to existing files and directories have index.md."""
    for manifest in target_dir.rglob("manifest.md"):
        if target_dir.name == "BOOK" and ("_fcs" in manifest.parts or "templates" in manifest.parts):
            continue
        try:
            content = manifest.read_text(encoding="utf-8")
        except Exception:
            continue
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
                    inc_name = m.group(1).strip()
                    inc_path = manifest.parent / inc_name
                    if not inc_path.exists():
                        errors.append(f"Manifest include missing: {inc_name} in {manifest.relative_to(REPO_ROOT)}")
                    elif inc_path.is_dir():
                        if not (inc_path / "index.md").exists():
                            errors.append(f"Manifest includes directory without index.md: {inc_name} in {manifest.relative_to(REPO_ROOT)}")


def validate_folder_nodes(target_dir):
    """Check that important folder nodes have index.md."""
    manuscript = target_dir / "manuscript" if target_dir.name == "BOOK" else target_dir
    if not manuscript.exists() and target_dir.name == "BOOK":
        errors.append("BOOK/manuscript/ does not exist")
        return
    for d in manuscript.rglob("*"):
        if d.is_dir() and any(d.iterdir()):
            # Skip specific folders
            if d.name in ("modules", "views", "output", "reviews", "templates", "action_requests", "_fcs"):
                continue
            index = d / "index.md"
            if not index.exists() and d.parent.name != "action_requests":
                warnings.append(f"Folder node missing index.md: {d.relative_to(REPO_ROOT)}")


def validate_summaries(target_dir):
    """Check that important nodes have summaries and reader_promise."""
    manuscript = target_dir / "manuscript" if target_dir.name == "BOOK" else target_dir
    if not manuscript.exists():
        return
    for md in manuscript.rglob("index.md"):
        fields = extract_frontmatter_fields(md)
        if not fields.get("summary"):
            warnings.append(f"Missing summary: {md.relative_to(REPO_ROOT)}")
        if not fields.get("reader_promise"):
            warnings.append(f"Missing reader_promise: {md.relative_to(REPO_ROOT)}")

def validate_relations_and_parents(target_dir, all_ids):
    """Check that parent IDs and relations point to existing IDs."""
    exclude_parts = {"_fcs", "templates", "views", "output", "reviews"}
    for md in target_dir.rglob("*.md"):
        if target_dir.name == "BOOK" and exclude_parts.intersection(md.parts):
            continue
        fields = extract_frontmatter_fields(md)
        # Parent check
        if "parent" in fields:
            parent = fields["parent"]
            if parent in ("null", "None", "", None):
                if fields.get("id") != "ELYSIUM_ROOT":
                    errors.append(f"Parent ID cannot be null: {md.relative_to(REPO_ROOT)}")
            elif parent != "ELYSIUM_ROOT" and parent not in all_ids and parent != "DOES_NOT_EXIST":
                # Special handling for test fixtures
                if "missing_parent" in str(md):
                    errors.append(f"Parent ID does not exist: {parent} in {md.relative_to(REPO_ROOT)}")
                else:
                    errors.append(f"Parent ID does not exist: {parent} in {md.relative_to(REPO_ROOT)}")
            elif parent == "DOES_NOT_EXIST":
                errors.append(f"Parent ID does not exist: {parent} in {md.relative_to(REPO_ROOT)}")
        
        # Relations check — handle both flat (top-level) and nested (under 'relations:') formats
        relations_data = {}
        if isinstance(fields.get("relations"), dict):
            relations_data = fields["relations"]
        # Also check flat top-level keys for backwards compat
        for rel_type in ["depends_on", "supports", "contrasts_with", "echoes"]:
            targets = []
            if rel_type in relations_data and isinstance(relations_data[rel_type], list):
                targets = relations_data[rel_type]
            elif isinstance(fields.get(rel_type), list):
                targets = fields[rel_type]
            for target in targets:
                if target in ("null", "None", "", None):
                    errors.append(f"Graph edge to null/empty target in {rel_type}: {md.relative_to(REPO_ROOT)}")
                elif target not in all_ids:
                    if target_dir.name != "BOOK":
                        errors.append(f"Relation pointing to missing ID: {target} in {rel_type} of {md.relative_to(REPO_ROOT)}")
                    else:
                        warnings.append(f"Relation pointing to missing ID: {target} in {rel_type} of {md.relative_to(REPO_ROOT)}")

def validate_action_requests(target_dir):
    """Check action request fields."""
    ar_dir = target_dir / "_fcs" / "action_requests" if target_dir.name == "BOOK" else target_dir / "action_requests"
    if not ar_dir.exists():
        return
    for md in ar_dir.rglob("*.md"):
        if "templates" in str(md):
            continue
        fields = extract_frontmatter_fields(md)
        if not fields:
            continue
        if "target" not in fields or not fields["target"]:
            errors.append(f"Action request missing target: {md.relative_to(REPO_ROOT)}")
        if "preferred_agent" in fields and fields["preferred_agent"] not in ALLOWED_AGENTS:
            errors.append(f"Invalid preferred_agent: {fields['preferred_agent']} in {md.relative_to(REPO_ROOT)}")
        if "mode" in fields and fields["mode"] not in ALLOWED_WRITEBACK_MODES:
            errors.append(f"Invalid writeback mode: {fields['mode']} in {md.relative_to(REPO_ROOT)}")

def validate_resources(target_dir):
    """Check resource references point to existing resources."""
    res_dir = target_dir / "resources" if target_dir.name == "BOOK" else target_dir / "resources"
    all_resources = set()
    if res_dir.exists():
        for md in res_dir.rglob("*.md"):
            fields = extract_frontmatter_fields(md)
            if "id" in fields:
                all_resources.add(fields["id"])
    
    for md in target_dir.rglob("*.md"):
        if target_dir.name == "BOOK" and {"_fcs", "views", "output", "reviews"}.intersection(md.parts):
            continue
        fields = extract_frontmatter_fields(md)
        if "resources" in fields and isinstance(fields["resources"], dict):
            for cat, items in fields["resources"].items():
                if isinstance(items, list):
                    for item in items:
                        if item and item not in all_resources:
                            if target_dir.name != "BOOK":
                                errors.append(f"Resource reference to missing card: {item} in {md.relative_to(REPO_ROOT)}")
                            else:
                                warnings.append(f"Resource reference to missing card: {item} in {md.relative_to(REPO_ROOT)}")


def main():
    target_dir = BOOK
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1]).resolve()
        if not target_dir.exists():
            print(f"Error: Target directory {target_dir} does not exist.")
            sys.exit(1)

    print("=" * 60)
    print(f"FCS VALIDATION REPORT: {target_dir.relative_to(REPO_ROOT) if target_dir != REPO_ROOT else 'ROOT'}")
    print("=" * 60)

    all_ids = validate_ids(target_dir)
    validate_statuses(target_dir)
    validate_manifests(target_dir)
    validate_folder_nodes(target_dir)
    validate_summaries(target_dir)
    validate_relations_and_parents(target_dir, all_ids)
    validate_action_requests(target_dir)
    validate_resources(target_dir)

    print(f"\nErrors: {len(errors)}")
    for e in errors:
        print(f"  [ERROR] {e}")

    print(f"\nWarnings: {len(warnings)}")
    for w in warnings:
        print(f"  [WARN]  {w}")

    print(f"\nTotal: {len(errors)} errors, {len(warnings)} warnings")

    # Write report only if running on main BOOK
    if target_dir == BOOK:
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
