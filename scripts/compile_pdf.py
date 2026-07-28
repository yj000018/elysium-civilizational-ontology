#!/usr/bin/env python3
"""Compile full ELYSIUM manuscript to PDF."""
import os, re, subprocess
from pathlib import Path

REPO = Path("/home/ubuntu/elysium_github_clone")
OUT_MD = Path("/home/ubuntu/ELYSIUM_Complete_Manuscript_Founder_Review.md")
OUT_PDF = Path("/home/ubuntu/ELYSIUM_Complete_Manuscript_Founder_Review.pdf")

def strip_yaml(text):
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            return text[end+3:].strip()
    return text

def count_words(text):
    return len(re.findall(r'\b\w+\b', text))

def collect_modules():
    """Collect all DRAFT_0 modules in order."""
    modules = []
    
    # Opening
    opn_dir = REPO / "BOOK" / "manuscript" / "01_opening"
    if opn_dir.exists():
        for f in sorted(opn_dir.glob("OPN-*_DRAFT_0.md")):
            modules.append(("Opening", f.stem.split("_")[0], strip_yaml(f.read_text())))
    
    # Foundations F01-F07
    foundations_dir = REPO / "BOOK" / "manuscript" / "02_foundations"
    for fdir in sorted(foundations_dir.iterdir()):
        if not fdir.is_dir():
            continue
        fname = fdir.name
        fkey = fname.split("_")[0] if "_" in fname else fname
        
        # Check drafts subdir first, then root
        for search_dir in [fdir / "drafts", fdir]:
            drafts = sorted(search_dir.glob(f"{fkey}-*_DRAFT_0.md")) if search_dir.exists() else []
            if drafts:
                for f in drafts:
                    modules.append((fkey, f.stem.split("_")[0], strip_yaml(f.read_text())))
                break
    
    return modules

def build_markdown(modules):
    """Build the full manuscript markdown."""
    lines = [
        "# ELYSIUM — A Civilizational Ontology",
        "",
        "**Founder Review Draft** — 2026-07-28",
        "",
        "---",
        "",
    ]
    
    current_section = None
    total_words = 0
    
    for section, module_id, prose in modules:
        if section != current_section:
            if section == "Opening":
                lines.append("# OPENING")
            else:
                lines.append(f"# FOUNDATION {section[-2:]}")
            lines.append("")
            current_section = section
        
        lines.append(f"## {module_id}")
        lines.append("")
        lines.append(prose)
        lines.append("")
        lines.append("---")
        lines.append("")
        total_words += count_words(prose)
    
    lines.append(f"\n*Total words: {total_words:,}*")
    return "\n".join(lines), total_words

def main():
    print("Collecting modules...", flush=True)
    modules = collect_modules()
    print(f"Found {len(modules)} modules", flush=True)
    
    print("Building markdown...", flush=True)
    md_content, total_words = build_markdown(modules)
    
    OUT_MD.write_text(md_content)
    print(f"Markdown written: {OUT_MD} ({total_words:,} words)", flush=True)
    
    print("Converting to PDF...", flush=True)
    result = subprocess.run(
        ["manus-md-to-pdf", str(OUT_MD), str(OUT_PDF)],
        capture_output=True, text=True, timeout=120
    )
    
    if result.returncode == 0 and OUT_PDF.exists():
        size_mb = OUT_PDF.stat().st_size / 1024 / 1024
        print(f"PDF created: {OUT_PDF} ({size_mb:.1f} MB)", flush=True)
    else:
        print(f"PDF conversion output: {result.stdout[:200]}", flush=True)
        print(f"PDF conversion error: {result.stderr[:200]}", flush=True)
    
    return total_words, len(modules)

if __name__ == "__main__":
    main()
