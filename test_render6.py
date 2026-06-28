import sys
from pathlib import Path
import re

REPO_ROOT = Path("/home/ubuntu/elysium-civilizational-ontology")

def strip_frontmatter(content):
    if content.startswith("---"):
        lines = content.splitlines()
        end_idx = -1
        for i, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                end_idx = i
                break
        if end_idx != -1:
            return "\n".join(lines[end_idx+1:]).strip()
    return content

def read_manifest_includes(manifest_path):
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
            m = re.match(r"^\s*-\s+(.+)$", line.strip())
            if m:
                includes.append(m.group(1).strip())
    return includes

target = REPO_ROOT / "BOOK/_fcs/test_fixtures/valid_minimal_project/manuscript/F01_material_base"
parts = []

def process_node(path):
    print(f"Processing node: {path}")
    if path.is_file():
        if path.exists() and path.name != "manifest.md":
            print(f"Adding file content from {path}")
            parts.append(strip_frontmatter(path.read_text(encoding="utf-8")))
        return
        
    index = path / "index.md"
    if index.exists():
        print(f"Adding index content from {index}")
        parts.append(strip_frontmatter(index.read_text(encoding="utf-8")))
        
    manifest = path / "manifest.md"
    if manifest.exists():
        includes = read_manifest_includes(manifest)
        print(f"Manifest includes: {includes}")
        for inc in includes:
            inc_path = path / inc
            print(f"Checking inc_path: {inc_path}")
            if inc_path.exists():
                process_node(inc_path)
            elif (path.parent / inc).exists():
                print(f"Found at path.parent: {path.parent / inc}")
                process_node(path.parent / inc)
            elif (target / inc).exists():
                print(f"Found at target: {target / inc}")
                process_node(target / inc)

process_node(target)
print("PARTS:")
print(parts)
