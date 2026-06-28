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


# ============================================================
# ELYSIUM PHASE III — CANONICAL CHECKS
# Non-invasive: all failures are errors or warnings, never crash
# ============================================================

# Required frontmatter fields for DRAFT_0 manuscript modules
DRAFT_REQUIRED_FIELDS = ["module_id", "title", "word_count", "status", "compile"]

# Canonical F01 module IDs (9 modules: F01-000 to F01-008)
F01_CANONICAL_IDS = [f"F01-{str(i).zfill(3)}" for i in range(9)]

# Canonical F01 material flows (7 flows — canonical since 2026-06-28 micro-patch)
F01_CANONICAL_FLOWS = ["Energy", "Water", "Habitat", "Infrastructure", "Mobility", "Food", "Materials"]

# Canonical Opening module IDs (13 modules: OPN-001 to OPN-013)
OPENING_CANONICAL_IDS = [f"OPN-{str(i).zfill(3)}" for i in range(1, 14)]

# Registry files that must exist
REQUIRED_REGISTRIES = [
    "BOOK/_fcs/registries/f01_prose_draft_registry.yaml",
    "BOOK/_fcs/registries/f01_writing_brief_registry.yaml",
    "BOOK/_fcs/registries/opening_prose_draft_registry.yaml",
    "BOOK/_fcs/registries/opening_writing_brief_registry.yaml",
]


def validate_elysium_draft_frontmatter():
    """Check that all DRAFT_0 manuscript modules have required frontmatter fields."""
    drafts_dirs = [
        BOOK / "manuscript" / "01_opening" / "drafts",
        BOOK / "manuscript" / "02_foundations" / "F01_material_existence" / "drafts",
    ]
    for drafts_dir in drafts_dirs:
        if not drafts_dir.exists():
            continue
        for md in sorted(drafts_dir.glob("*_DRAFT_0.md")):
            fields = extract_frontmatter_fields(md)
            if not fields:
                errors.append(f"[ELYSIUM] No frontmatter in DRAFT_0 file: {md.relative_to(REPO_ROOT)}")
                continue
            for req in DRAFT_REQUIRED_FIELDS:
                if req not in fields or fields[req] in (None, "", "null"):
                    errors.append(f"[ELYSIUM] Missing required frontmatter field '{req}' in: {md.relative_to(REPO_ROOT)}")
            # word_count must be a positive integer
            wc = fields.get("word_count")
            if wc is not None:
                try:
                    wc_int = int(str(wc).strip())
                    if wc_int <= 0:
                        errors.append(f"[ELYSIUM] word_count <= 0 in: {md.relative_to(REPO_ROOT)}")
                except ValueError:
                    errors.append(f"[ELYSIUM] word_count not an integer in: {md.relative_to(REPO_ROOT)}")


def validate_elysium_canonical_counts():
    """Check F01 and Opening module counts and IDs match canonical definitions."""
    # F01 drafts
    f01_drafts_dir = BOOK / "manuscript" / "02_foundations" / "F01_material_existence" / "drafts"
    if f01_drafts_dir.exists():
        found_ids = []
        for md in sorted(f01_drafts_dir.glob("F01-*_DRAFT_0.md")):
            fields = extract_frontmatter_fields(md)
            mid = fields.get("module_id", "")
            if mid:
                found_ids.append(mid)
        for cid in F01_CANONICAL_IDS:
            if cid not in found_ids:
                errors.append(f"[ELYSIUM] Missing canonical F01 module: {cid}")
        extra = [i for i in found_ids if i not in F01_CANONICAL_IDS]
        for eid in extra:
            warnings.append(f"[ELYSIUM] Non-canonical F01 module found: {eid}")
    # Opening drafts
    opn_drafts_dir = BOOK / "manuscript" / "01_opening" / "drafts"
    if opn_drafts_dir.exists():
        found_opn = []
        for md in sorted(opn_drafts_dir.glob("OPN-*_DRAFT_0.md")):
            fields = extract_frontmatter_fields(md)
            mid = fields.get("module_id", "")
            if mid:
                found_opn.append(mid)
        for cid in OPENING_CANONICAL_IDS:
            if cid not in found_opn:
                errors.append(f"[ELYSIUM] Missing canonical Opening module: {cid}")
        extra_opn = [i for i in found_opn if i not in OPENING_CANONICAL_IDS]
        for eid in extra_opn:
            warnings.append(f"[ELYSIUM] Non-canonical Opening module found: {eid}")


def validate_elysium_registries_exist():
    """Check that all required registry files exist."""
    for reg_path in REQUIRED_REGISTRIES:
        full_path = REPO_ROOT / reg_path
        if not full_path.exists():
            errors.append(f"[ELYSIUM] Required registry missing: {reg_path}")


def _load_yaml_frontmatter_only(filepath):
    """Load only the YAML frontmatter from a file (handles Markdown+frontmatter files)."""
    try:
        import yaml
        content = filepath.read_text(encoding="utf-8")
        if not content.startswith("---"):
            return yaml.safe_load(content)
        end = content.find("---", 3)
        if end == -1:
            return yaml.safe_load(content[3:])
        fm_text = content[3:end]
        return yaml.safe_load(fm_text)
    except Exception:
        return None


def validate_elysium_registry_module_crossref():
    """Cross-reference f01_prose_draft_registry against actual DRAFT_0 files.
    Only checks registries that have a 'modules:' list in pure YAML format.
    Markdown-with-frontmatter registries (like opening_prose_draft_registry) are skipped.
    """
    try:
        import yaml
    except ImportError:
        warnings.append("[ELYSIUM] PyYAML not available — skipping registry cross-reference")
        return
    # Only check pure-YAML registries with modules: list
    registry_map = {
        REPO_ROOT / "BOOK/_fcs/registries/f01_prose_draft_registry.yaml": (
            BOOK / "manuscript" / "02_foundations" / "F01_material_existence" / "drafts",
            "F01-"
        ),
        REPO_ROOT / "BOOK/_fcs/registries/f01_writing_brief_registry.yaml": (
            BOOK / "manuscript" / "02_foundations" / "F01_material_existence" / "drafts",
            "F01-"
        ),
    }
    for reg_file, (drafts_dir, prefix) in registry_map.items():
        if not reg_file.exists():
            continue  # already caught by validate_elysium_registries_exist
        try:
            reg = yaml.safe_load(reg_file.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"[ELYSIUM] Registry YAML parse error in {reg_file.name}: {e}")
            continue
        if not reg or "modules" not in reg:
            # Registry may be Markdown-with-frontmatter — skip silently
            continue
        for mod in reg["modules"]:
            mid = mod.get("module_id", "")
            if not mid:
                errors.append(f"[ELYSIUM] Registry entry missing module_id in {reg_file.name}")
                continue
            draft_file = mod.get("draft_file", "")
            if draft_file:
                full_draft = REPO_ROOT / draft_file
                if not full_draft.exists():
                    errors.append(f"[ELYSIUM] Registry references missing draft: {draft_file} (in {reg_file.name})")
            else:
                warnings.append(f"[ELYSIUM] Registry entry {mid} has no draft_file in {reg_file.name}")


def validate_elysium_f01_seven_flows():
    """Check F01-000 prose does not say 'six' flows when it should say 'seven'."""
    f01_000 = BOOK / "manuscript" / "02_foundations" / "F01_material_existence" / "drafts" / "F01-000_DRAFT_0.md"
    if not f01_000.exists():
        return
    content = f01_000.read_text(encoding="utf-8")
    # Strip frontmatter before checking
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            prose = content[end + 3:]
        else:
            prose = content
    else:
        prose = content
    # Check for canonical count mismatch patterns
    bad_patterns = [
        r"six primary domains",
        r"six material flows",
        r"six domains",
        r"six flows",
        r"encompasses six",
        r"These six domains",
        r"These six flows",
    ]
    for pat in bad_patterns:
        if re.search(pat, prose, re.IGNORECASE):
            errors.append(f"[ELYSIUM] Canonical count mismatch in F01-000: found pattern '{pat}' — should be 'seven'")
    # Check all 7 canonical flows are mentioned
    for flow in F01_CANONICAL_FLOWS:
        if flow not in prose:
            errors.append(f"[ELYSIUM] F01-000 missing canonical flow mention: '{flow}'")


def validate_elysium_terminal_punctuation():
    """Check all DRAFT_0 prose files end with terminal punctuation (not truncated)."""
    import glob
    draft_dirs = [
        BOOK / "manuscript" / "01_opening" / "drafts",
        BOOK / "manuscript" / "02_foundations" / "F01_material_existence" / "drafts",
    ]
    bad_endings = (',', '-', ':', ';', 'and', 'or', 'but', 'the', 'a', 'an', 'of', 'in', 'to')
    for d in draft_dirs:
        if not d.exists():
            continue
        for f in sorted(d.glob("*_DRAFT_0.md")):
            content = f.read_text(encoding="utf-8")
            if content.startswith("---"):
                end = content.find("---", 3)
                prose = content[end + 3:].strip() if end != -1 else content
            else:
                prose = content.strip()
            if not prose:
                continue
            last_char = prose.rstrip()[-1]
            if last_char not in '.!?':
                errors.append(
                    f"[ELYSIUM] Truncated prose — does not end with terminal punctuation "
                    f"(ends with {repr(last_char)}): {f.relative_to(REPO_ROOT)}"
                )


def validate_elysium_no_four_flows():
    """Check no Opening module uses 'four flows' without explicit scope qualification."""
    opn_dir = BOOK / "manuscript" / "01_opening" / "drafts"
    if not opn_dir.exists():
        return
    import re as _re
    for f in sorted(opn_dir.glob("*_DRAFT_0.md")):
        content = f.read_text(encoding="utf-8")
        if content.startswith("---"):
            end = content.find("---", 3)
            prose = content[end + 3:] if end != -1 else content
        else:
            prose = content
        if _re.search(r'\bfour flows\b', prose, _re.IGNORECASE):
            errors.append(
                f"[ELYSIUM] Canonical terminology error — 'four flows' found in Opening module "
                f"(must be 'five flow classes' or 'Five Classes of Civilizational Flows'): "
                f"{f.relative_to(REPO_ROOT)}"
            )


def validate_elysium_founder_reader_view():
    """Check Founder Reader View exists and ends with terminal punctuation."""
    frv = BOOK / "views" / "founder_reading" / "ELYSIUM_Draft_0_Opening_plus_F01_FounderReview.md"
    if not frv.exists():
        warnings.append("[ELYSIUM] Founder Reader View not found: BOOK/views/founder_reading/ELYSIUM_Draft_0_Opening_plus_F01_FounderReview.md")
        return
    content = frv.read_text(encoding="utf-8")
    last_char = content.rstrip()[-1]
    if last_char not in '.!?*_':
        errors.append(
            f"[ELYSIUM] Founder Reader View may be truncated — ends with {repr(last_char)}: "
            f"{frv.relative_to(REPO_ROOT)}"
        )
    # Check module count: must contain all 22 module headings
    import re as _re
    opn_headings = len(_re.findall(r'### OPN-\d{3}', content))
    f01_headings = len(_re.findall(r'### F01-\d{3}', content))
    if opn_headings < 13:
        errors.append(f"[ELYSIUM] Founder Reader View missing Opening modules: found {opn_headings}/13")
    if f01_headings < 9:
        errors.append(f"[ELYSIUM] Founder Reader View missing F01 modules: found {f01_headings}/9")


def validate_elysium_llm_completion_status():
    """Check all API output files for llm_completion_status != COMPLETE."""
    api_outputs_dir = BOOK / "_fcs" / "api_outputs"
    if not api_outputs_dir.exists():
        return
    for f in sorted(api_outputs_dir.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        if not content.startswith("---"):
            continue
        end = content.find("---", 3)
        if end == -1:
            continue
        fm = content[3:end]
        status_match = re.search(r'^llm_completion_status:\s*(\S+)', fm, re.M)
        if not status_match:
            continue  # No guard field — older output, skip
        status = status_match.group(1).strip()
        if status not in ("COMPLETE", "UNKNOWN"):
            errors.append(
                f"[ELYSIUM] API output has llm_completion_status={status} (not COMPLETE): "
                f"{f.relative_to(REPO_ROOT)}"
            )
        elif status == "UNKNOWN":
            warnings.append(
                f"[ELYSIUM] API output has llm_completion_status=UNKNOWN (no finish_reason available): "
                f"{f.relative_to(REPO_ROOT)}"
            )


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
    # ELYSIUM Phase III canonical checks
    validate_elysium_draft_frontmatter()
    validate_elysium_canonical_counts()
    validate_elysium_registries_exist()
    validate_elysium_registry_module_crossref()
    validate_elysium_f01_seven_flows()
    validate_elysium_terminal_punctuation()
    validate_elysium_no_four_flows()
    validate_elysium_founder_reader_view()
    validate_elysium_llm_completion_status()

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
