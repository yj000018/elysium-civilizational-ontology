# Node Model

Do not use `node.md`.

Use:
- **folder node**: folder + `index.md`
- **file node**: markdown file directly

## Folder Node

A folder node uses `index.md`. Example: `BOOK/manuscript/02_foundations/F01_material_base/F01_01_energy/index.md`

`index.md` contains:
- YAML frontmatter
- human-readable executive summary
- function in the architecture
- reader promise
- status
- notes
- navigation links
- AI actions menu

YAML alone is not enough. Each important node must be readable by a human.

## File Node

A module file is also a node. Example: `BOOK/manuscript/02_foundations/F01_material_base/F01_01_energy/modules/02_energy_pathologies.md`

It includes frontmatter + content.

## Node Frontmatter Template

Use minimal but graph/resource-ready YAML. Do not force all fields on tiny scratch notes. Important architectural nodes and reviewable modules must use this model.
