# Manifest Model

## Purpose
The Manifest Model dictates the exact sequence and inclusion of content nodes. Because filesystem sorting (alphabetical sorting of filenames) is rigid and insufficient for complex editorial sequencing, `manifest.md` acts as the definitive "binder" for any given section of the manuscript.

## Scope
Manifests are used exclusively within `BOOK/manuscript/` folder nodes. They are required for any folder where the order of children matters (e.g., the root, parts, foundations, and facets with multiple modules). They are **NOT** used in `BOOK/resources/` or `BOOK/views/`.

## Format and Parsing

A `manifest.md` file is a simple Markdown document designed to be easily read by humans and reliably parsed by `scripts/render.py` and `scripts/validate.py`.

It must contain specific heading sections:

### 1. `## Include`
This section lists the exact directory or file names (relative to the manifest's location) that should be included in the compiled output, in the exact order they appear.

**Syntax:** An unordered Markdown list.

**Example:**
```markdown
## Include
- F01_01_energy
- F01_02_water
- F01_03_food
```

### 2. `## Optional / Parked`
This section lists nodes that exist on the filesystem but are currently excluded from the main compilation. They might be drafts, alternative versions, or parked ideas that the Operator is not ready to delete.

**Syntax:** An unordered Markdown list.

### 3. `## Exclude`
This section lists items that explicitly should not be compiled (e.g., scratchpads, obsolete modules, or test files).

## Script Integration

When `render.py` processes a folder node (e.g., to generate an `expanded` view), it performs the following steps:
1. It reads the folder's `index.md` to get the introductory content.
2. It looks for `manifest.md`.
3. It reads the `## Include` list line by line.
4. For each item, it resolves the path.
5. If the item is a file (e.g., `modules/01_energy.md`), it appends its content.
6. If the item is a folder (e.g., `F01_01_energy`), it recursively repeats the process.

## Failure Modes

The FCS validation scripts actively monitor manifests to prevent silent failures:

- **Missing Include (Error):** A path listed in `## Include` does not exist on the filesystem. This will break the build and is caught by `validate.py`.
- **Directory Without Index (Error):** A folder is included in the manifest, but it lacks an `index.md` file. Caught by `validate.py`.
- **Orphaned Content (Warning):** A module or folder exists in the directory but is not listed in `## Include`, `## Optional / Parked`, or `## Exclude`. It will be silently ignored by `render.py`. Caught by `validate.py` as a warning.

## Do-Not Rules
- **Do NOT** rely on alphabetical filenames (like `01_intro.md`, `02_body.md`) to dictate the final output order. Always use the manifest.
- **Do NOT** include full absolute paths (like `/home/ubuntu/...` or `BOOK/manuscript/...`) in the manifest list. Use relative paths (just the directory or filename, e.g., `modules/01_intro.md`).
- **Do NOT** use complex Markdown formatting (bold, italics, links) inside the manifest list items. Keep it plain text.
