# Node Model

## Purpose
The Node Model defines the fundamental units of content within the FCS architecture. It ensures that the hierarchical structure of the ELYSIUM ontology is accurately represented on the filesystem while remaining readable, machine-parsable, and compatible with Obsidian.

## Scope
This model applies to all content within `BOOK/manuscript/`. It explicitly prohibits the use of generic `node.md` files or YAML-only nodes.

## Node Types

### 1. Folder Nodes (Structural Containers)
A folder node represents a structural container (e.g., a Part, Foundation, or Facet). It consists of a directory containing an `index.md` file and a `manifest.md` file.

**Characteristics:**
- The directory name should match the canonical ID (e.g., `F01_material_base`).
- The `index.md` file serves as the database record and the human-readable entry point.
- The `manifest.md` file defines the explicit ordering of children.

**Contents of `index.md`:**
- Comprehensive YAML frontmatter.
- An executive summary.
- The `reader_promise` (what the reader gains from this section).
- High-level architectural notes.

### 2. File Nodes (Modules)
A file node represents a specific, atomic piece of long-form content. It is a standalone Markdown file (e.g., `01_energy_as_dependency.md`).

**Characteristics:**
- Modules reside within a `modules/` subdirectory of their parent folder node.
- They contain the actual prose of the manuscript.

**Contents of a Module:**
- YAML frontmatter (`id`, `title`, `status`, `parent`).
- The Markdown prose.

## Frontmatter Schema (The Database Layer)

Both node types require YAML frontmatter. This frontmatter acts as a distributed NoSQL database, queried by Dataview and Python scripts.

```yaml
id: F01_01_M01
title: Energy as a Dependency
type: module # part, foundation, facet, module, concept
status: SCAFFOLDED # PLANNED, DRAFT, READY_FOR_AI, REVIEW_PENDING, REVISION_REQUIRED, REVISED, LOCKED
parent: F01_01 # Must point to a valid ID
summary: "Why energy is the master resource."
reader_promise: "The reader understands that without energy, no other foundation functions."

concepts:
  - energy_metabolism

resources:
  people: []
  institutions: []
  organizations: []
  books: []
  websites: []
  movements: []
  technologies: []
  places: []
  datasets: []
  frameworks: []
  sources: []
  case_studies: []

relations:
  depends_on: []
  supports: []
  contrasts_with: []
  echoes: []
  should_reference: []
  avoid_duplicate_with: []

graph:
  layer: manuscript
  cluster: material_base
  node_type: module
  weight: 3
  show_in_public_graph: true

sources:
  canonical: []
  non_canonical_inspiration: []

review:
  review_unit: true
  last_reviewed_by: null
  review_notes: []
```

## Do-Not Rules
- **Do NOT** create a folder node without an `index.md` file.
- **Do NOT** use `node.md`. Always use `index.md`.
- **Do NOT** put long-form prose directly into an `index.md` file. Use a module.
- **Do NOT** omit the `id` or `parent` fields. `validate.py` will fail.
- **Do NOT** use a `parent` ID that does not exist in the repository.
