# Views and Rendering Model

## Purpose
The Render Model defines how the fragmented, fractal source files in `BOOK/manuscript/` are assembled into coherent documents for reading, review, and downstream handoff. 

Because the FCS uses a highly modular architecture (hundreds of atomic files), a robust rendering pipeline is essential to view the content as a traditional book.

## Scope
This model is implemented by `scripts/render.py`. It operates strictly as a read-only process, reading source files and writing outputs to `BOOK/views/` and `BOOK/output/`.

## Render Modes

### 1. Brief View (`python scripts/render.py brief <path>`)
**Purpose**: To inspect the architectural intent of a single node without the noise of its children.
**Operation**: Reads only the target file (or the `index.md` if the target is a folder). Retains frontmatter.
**Output Location**: `BOOK/views/brief/`

### 2. Expanded View (`python scripts/render.py expanded <path>`)
**Purpose**: To read a section (e.g., a Foundation or Facet) as a continuous, flowing document.
**Operation**: Reads the target folder's `index.md`, then recursively reads all children specified in the `manifest.md` under the `## Include` section. Frontmatter is stripped from the children to create a seamless reading experience.
**Output Location**: `BOOK/views/expanded/`

### 3. Review View (`python scripts/render.py review <path>`)
**Purpose**: To provide the Operator or AI Reviewer with the content alongside critical metadata for editorial decisions.
**Operation**: Similar to the Brief view, but prepends a metadata block containing word count, raw frontmatter values, manifest inclusion counts, and any missing file warnings.
**Output Location**: `BOOK/views/review/`

### 4. Clean View (`python scripts/render.py clean <path>`)
**Purpose**: To generate a clean, prose-only version of a specific section without any YAML metadata.
**Operation**: Recursively traverses the target path via manifests, stripping all frontmatter, internal notes, and AI metadata.
**Output Location**: `BOOK/views/full_corpus/`

### 5. Master Corpus (`python scripts/render.py master BOOK/manuscript`)
**Purpose**: To generate the pristine Master Content Layer for downstream systems.
**Operation**: Recursively traverses the entire manuscript (starting from the root `index.md`), stripping all frontmatter. It produces a single, massive Markdown file containing only the canonical prose.
**Output Location**: `BOOK/output/master_corpus/full_source.md`

## Workflow Integration
1. The Operator or an AI agent invokes `render.py` via the command line or an Obsidian QuickAdd command.
2. The script processes the target according to the specified mode.
3. The resulting file is written to the appropriate directory, where it can be viewed in Obsidian or picked up by another process (e.g., Pandoc for PDF generation).

## Failure Modes
- **Manifest Parsing Errors**: If a manifest is malformed, the Expanded and Master views will skip content. (This is why `validate.py` must be run frequently).
- **Infinite Recursion**: Prevented by strict directory structures, but possible if manifests circularly reference each other.
- **Path Resolution**: The render script must accurately resolve relative paths within manifests against the current node's location.

## Do-Not Rules
- **Do NOT** modify the source files in `BOOK/manuscript/` during the rendering process. `render.py` must be strictly read-only on the source directory.
- **Do NOT** commit generated views in `BOOK/views/` to version control unless necessary. They are ephemeral artifacts. The Master Corpus in `BOOK/output/` should be committed.
