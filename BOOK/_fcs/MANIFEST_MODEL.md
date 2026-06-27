# Manifest Model

Use `manifest.md` only when explicit order is needed. Do not create unnecessary manifests everywhere.

A manifest is required for:
- book root
- major part
- chapter/foundation
- facet with multiple child modules
- any folder where order matters

A manifest is optional or unnecessary for:
- folder with no children
- folder with one child
- scratch area
- resource folders

## Manifest Format

Use simple Markdown sections for human readability and script parsing. `render.py` must read the `## Include` list. The manifest is the binder. Compilation/rendering reads the manifest, not arbitrary filesystem order.

Example format includes `## Include`, `## Optional / Parked`, and `## Exclude` sections.
