import sys
from pathlib import Path
import re

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

target = Path("/home/ubuntu/elysium-civilizational-ontology/BOOK/_fcs/test_fixtures/valid_minimal_project/manuscript/F01_material_base")
manifest = target / "manifest.md"
print(f"Manifest exists: {manifest.exists()}")
print(f"Manifest content: {manifest.read_text()}")
includes = read_manifest_includes(manifest)
print(f"Includes: {includes}")
for inc in includes:
    inc_path = target / inc
    print(f"Checking {inc_path}: exists={inc_path.exists()}, is_file={inc_path.is_file()}")
