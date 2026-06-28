import sys
from pathlib import Path

REPO_ROOT = Path("/home/ubuntu/elysium-civilizational-ontology")

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
            if line.startswith("- "):
                includes.append(line[2:].strip())
    return includes

target = REPO_ROOT / "BOOK/_fcs/test_fixtures/valid_minimal_project/manuscript/F01_material_base"
manifest = target / "manifest.md"
includes = read_manifest_includes(manifest)
print(f"Includes: {includes}")
for inc in includes:
    inc_path = target / inc
    print(f"Checking {inc_path}: exists={inc_path.exists()}, is_file={inc_path.is_file()}")
