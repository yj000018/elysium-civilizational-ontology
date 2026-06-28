#!/usr/bin/env python3
"""
FCS Dynamic Binder View Generator
Scans BOOK/**/*.md for files with fcs_role frontmatter.
Generates:
  - BOOK/_fcs/binder_views/current_binder_view.md  (full manuscript)
  - BOOK/_fcs/binder_views/opening_binder_view.md  (Opening Part only)

No external dependencies beyond Python standard library.
"""

import os
import sys
from pathlib import Path
from datetime import datetime

BOOK_ROOT = Path(__file__).parent.parent / "BOOK"
BINDER_DIR = BOOK_ROOT / "_fcs" / "binder_views"
EXCLUDE_PARTS = {"_fcs", "templates", "views", "output", "reviews", "test_fixtures"}


def parse_frontmatter(text):
    """Minimal YAML frontmatter parser — returns dict of key: value strings."""
    fm = {}
    if not text.startswith("---"):
        return fm
    end = text.find("\n---", 3)
    if end == -1:
        return fm
    block = text[3:end].strip()
    for line in block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val.lower() == "null":
                val = ""
            fm[key] = val
    return fm


def collect_modules():
    """Walk BOOK/**/*.md and collect files with fcs_role in frontmatter."""
    modules = []
    for md in sorted(BOOK_ROOT.rglob("*.md")):
        # Skip excluded directories
        if EXCLUDE_PARTS.intersection(set(md.parts)):
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except Exception:
            continue
        fm = parse_frontmatter(text)
        # Accept files with fcs_role OR with type=module/facet/beat (legacy FCS)
        if not fm.get("fcs_role") and fm.get("type") not in ("module", "facet", "beat", "chapter"):
            continue
        # Infer fcs_role if missing
        if not fm.get("fcs_role"):
            t = fm.get("type", "")
            fm["fcs_role"] = f"manuscript_{t}" if t else "manuscript_module"
        # Infer part from path if missing
        if not fm.get("part"):
            parts_map = {
                "01_opening": "OPENING",
                "02_foundations": "FOUNDATIONS",
                "03_transition": "TRANSITION",
                "04_implementation": "IMPLEMENTATION",
                "05_appendices": "APPENDICES",
            }
            for seg, label in parts_map.items():
                if seg in str(md):
                    fm["part"] = label
                    break
        fm["_path"] = str(md.relative_to(BOOK_ROOT.parent))
        modules.append(fm)
    return modules


def sort_key(m):
    part_order = {
        "OPENING": "01",
        "FOUNDATIONS": "02",
        "TRANSITION": "03",
        "IMPLEMENTATION": "04",
        "APPENDICES": "05",
    }
    part = part_order.get(m.get("part", ""), "99")
    order = m.get("order", m.get("module_id", "999")).zfill(6)
    return f"{part}_{order}"


def render_table(modules, columns):
    """Render a Markdown pipe table."""
    header = "| " + " | ".join(c[1] for c in columns) + " |"
    sep = "| " + " | ".join("---" for _ in columns) + " |"
    rows = []
    for m in modules:
        cells = []
        for key, _ in columns:
            val = m.get(key, "")
            if key == "_path":
                val = f"`{val}`"
            cells.append(val or "—")
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, sep] + rows)


def generate_full_binder(modules, generated_at):
    cols_full = [
        ("module_id", "ID"),
        ("title", "Title"),
        ("type", "Type"),
        ("part", "Part"),
        ("movement_id", "Movement"),
        ("order", "Order"),
        ("status", "FCS Status"),
        ("operational_status", "Op. Status"),
        ("prose_status", "Prose"),
        ("routing_status", "Routing"),
    ]
    lines = [
        "# ELYSIUM — Current Binder View (Generated)",
        "",
        f"> Generated: {generated_at}",
        "> Source of truth: module frontmatter + book_module_registry.yaml",
        "> Do not edit manually. Regenerate with: `python scripts/generate_binder_view.py`",
        "",
        "---",
        "",
        "## All Manuscript Modules",
        "",
        render_table(modules, cols_full),
        "",
        "---",
        "",
    ]

    # Group by part
    parts_seen = {}
    for m in modules:
        p = m.get("part", "UNKNOWN")
        parts_seen.setdefault(p, []).append(m)

    for part, mods in sorted(parts_seen.items()):
        lines += [
            f"## {part}",
            "",
            render_table(mods, cols_full),
            "",
        ]

    # Status distribution
    status_dist = {}
    for m in modules:
        s = m.get("status", "UNKNOWN")
        status_dist[s] = status_dist.get(s, 0) + 1
    lines += [
        "## Status Distribution",
        "",
        "| FCS Status | Count |",
        "| --- | --- |",
    ]
    for s, c in sorted(status_dist.items()):
        lines.append(f"| {s} | {c} |")

    return "\n".join(lines) + "\n"


def generate_opening_binder(modules, generated_at):
    opening = [m for m in modules if m.get("part") == "OPENING"]
    cols = [
        ("module_id", "ID"),
        ("title", "Title"),
        ("movement_id", "Movement"),
        ("order", "Order"),
        ("status", "FCS Status"),
        ("operational_status", "Op. Status"),
        ("prose_status", "Prose"),
        ("routing_status", "Routing"),
        ("_path", "Path"),
    ]
    lines = [
        "# ELYSIUM — Opening Part Binder View (Generated)",
        "",
        f"> Generated: {generated_at}",
        "> Reader movement: sentir → comprendre l'échec → changer de métaphore → recevoir la carte",
        "> Do not edit manually. Regenerate with: `python scripts/generate_binder_view.py`",
        "",
        "---",
        "",
        "## All Opening Modules",
        "",
        render_table(opening, cols) if opening else "_No opening modules found with fcs_role._",
        "",
    ]

    # Group by movement
    movements = {}
    for m in opening:
        mv = m.get("movement_id") or m.get("movement_title") or "NO_MOVEMENT"
        movements.setdefault(mv, []).append(m)

    for mv, mods in sorted(movements.items()):
        mv_title = mods[0].get("movement_title", mv)
        lines += [
            f"## {mv} — {mv_title}",
            "",
            render_table(mods, cols),
            "",
        ]

    return "\n".join(lines) + "\n"


def main():
    generated_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    print(f"[generate_binder_view] Scanning {BOOK_ROOT} ...")
    modules = collect_modules()
    modules.sort(key=sort_key)
    print(f"[generate_binder_view] Found {len(modules)} modules with fcs_role")

    BINDER_DIR.mkdir(parents=True, exist_ok=True)

    # Full binder
    full_path = BINDER_DIR / "current_binder_view.md"
    full_path.write_text(generate_full_binder(modules, generated_at), encoding="utf-8")
    print(f"[generate_binder_view] Written: {full_path}")

    # Opening binder
    opening_path = BINDER_DIR / "opening_binder_view.md"
    opening_path.write_text(generate_opening_binder(modules, generated_at), encoding="utf-8")
    print(f"[generate_binder_view] Written: {opening_path}")

    print(f"[generate_binder_view] Done. {len(modules)} modules processed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
