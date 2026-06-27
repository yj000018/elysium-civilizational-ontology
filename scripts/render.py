#!/usr/bin/env python3
"""
FCS Render Script
Renders content views: brief, expanded, review, clean, master.

Usage:
    python scripts/render.py brief BOOK/manuscript/02_foundations/F01_material_base
    python scripts/render.py expanded BOOK/manuscript/02_foundations/F01_material_base
    python scripts/render.py review BOOK/manuscript/02_foundations/F01_material_base
    python scripts/render.py clean BOOK/manuscript/02_foundations/F01_material_base
    python scripts/render.py master BOOK/manuscript
"""

import sys
import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def strip_frontmatter(content):
    """Remove YAML frontmatter from content."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3:].strip()
    return content


def extract_frontmatter(content):
    """Extract YAML frontmatter as raw text."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[3:end].strip()
    return ""


def read_manifest_includes(manifest_path):
    """Read the ## Include section of a manifest.md file."""
    if not manifest_path.exists():
        return []
    content = manifest_path.read_text(encoding="utf-8")
    includes = []
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
                includes.append(m.group(1).strip())
    return includes


def render_brief(target_path):
    """Render brief view: just the index.md of the target."""
    target = REPO_ROOT / target_path
    index_file = target / "index.md" if target.is_dir() else target
    if not index_file.exists():
        return f"# Brief View\n\nNo index.md found at {index_file}"
    return index_file.read_text(encoding="utf-8")


def render_expanded(target_path):
    """Render expanded view: assemble children from manifest."""
    target = REPO_ROOT / target_path
    if not target.is_dir():
        return render_brief(target_path)
    manifest = target / "manifest.md"
    includes = read_manifest_includes(manifest)
    if not includes:
        return f"# Expanded View\n\nNo manifest includes found at {manifest}"
    parts = []
    index_file = target / "index.md"
    if index_file.exists():
        parts.append(strip_frontmatter(index_file.read_text(encoding="utf-8")))
    for inc in includes:
        inc_path = target / inc
        if inc_path.is_dir():
            sub_index = inc_path / "index.md"
            if sub_index.exists():
                parts.append(strip_frontmatter(sub_index.read_text(encoding="utf-8")))
        elif inc_path.exists() and inc_path.is_file():
            parts.append(strip_frontmatter(inc_path.read_text(encoding="utf-8")))
    return "\n\n---\n\n".join(parts)


def render_review(target_path):
    """Render review view: content + metadata."""
    target = REPO_ROOT / target_path
    if not target.is_dir():
        content = target.read_text(encoding="utf-8") if target.exists() else ""
        fm = extract_frontmatter(content)
        body = strip_frontmatter(content)
        wc = len(body.split())
        return f"# Review View\n\n**Word count:** {wc}\n**Frontmatter:**\n```\n{fm}\n```\n\n---\n\n{body}"
    index_file = target / "index.md"
    if not index_file.exists():
        return f"# Review View\n\nNo index.md found at {target}"
    content = index_file.read_text(encoding="utf-8")
    fm = extract_frontmatter(content)
    body = strip_frontmatter(content)
    wc = len(body.split())
    manifest = target / "manifest.md"
    includes = read_manifest_includes(manifest)
    missing = [i for i in includes if not (target / i).exists()]
    review = f"# Review View — {target_path}\n\n"
    review += f"**Word count (index):** {wc}\n"
    review += f"**Manifest includes:** {len(includes)}\n"
    if missing:
        review += f"**Missing files:** {missing}\n"
    review += f"\n**Frontmatter:**\n```\n{fm}\n```\n\n---\n\n{body}"
    return review


def render_clean(target_path):
    """Render clean view: content without frontmatter."""
    target = REPO_ROOT / target_path
    if not target.is_dir():
        if target.exists():
            return strip_frontmatter(target.read_text(encoding="utf-8"))
        return ""
    manifest = target / "manifest.md"
    includes = read_manifest_includes(manifest)
    parts = []
    for inc in includes:
        inc_path = target / inc
        if inc_path.exists():
            parts.append(strip_frontmatter(inc_path.read_text(encoding="utf-8")))
    return "\n\n---\n\n".join(parts)


def render_master(target_path):
    """Render master corpus from the entire manuscript."""
    target = REPO_ROOT / target_path
    manifest = target / "manifest.md"
    includes = read_manifest_includes(manifest)
    parts = []
    for inc in includes:
        sub = target / inc
        if sub.is_dir():
            sub_manifest = sub / "manifest.md"
            sub_includes = read_manifest_includes(sub_manifest)
            sub_index = sub / "index.md"
            if sub_index.exists():
                parts.append(strip_frontmatter(sub_index.read_text(encoding="utf-8")))
            for si in sub_includes:
                si_path = sub / si
                if si_path.is_dir():
                    deep_index = si_path / "index.md"
                    if deep_index.exists():
                        parts.append(strip_frontmatter(deep_index.read_text(encoding="utf-8")))
                elif si_path.exists() and si_path.is_file():
                    parts.append(strip_frontmatter(si_path.read_text(encoding="utf-8")))
    return "\n\n---\n\n".join(parts) if parts else "# Master Corpus\n\nNo content found."


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    mode = sys.argv[1]
    target_path = sys.argv[2]

    renderers = {
        "brief": render_brief,
        "expanded": render_expanded,
        "review": render_review,
        "clean": render_clean,
        "master": render_master,
    }

    if mode not in renderers:
        print(f"Unknown mode: {mode}. Use: {list(renderers.keys())}")
        sys.exit(1)

    output = renderers[mode](target_path)

    # Determine output path
    output_dir_map = {
        "brief": REPO_ROOT / "BOOK" / "views" / "brief",
        "expanded": REPO_ROOT / "BOOK" / "views" / "expanded",
        "review": REPO_ROOT / "BOOK" / "views" / "review",
        "clean": REPO_ROOT / "BOOK" / "views" / "full_corpus",
        "master": REPO_ROOT / "BOOK" / "output" / "master_corpus",
    }

    out_dir = output_dir_map[mode]
    out_dir.mkdir(parents=True, exist_ok=True)

    safe_name = target_path.replace("/", "_").replace("\\", "_")
    if mode == "master":
        out_file = out_dir / "full_source.md"
    else:
        out_file = out_dir / f"{safe_name}.md"

    out_file.write_text(output, encoding="utf-8")
    print(f"[render.py] {mode} view written to: {out_file}")


if __name__ == "__main__":
    main()
