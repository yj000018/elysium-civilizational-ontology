# FCS Architecture

## Purpose
This document defines the overarching architecture of the Fractal Content Studio (FCS). FCS is designed to manage the immense complexity of the ELYSIUM ontology without collapsing under its own weight.

## Scope
The architecture covers the physical directory layout, the logical data model, and the operational boundaries of the system.

## Directory Layout
The repository is structured as follows:

- `BOOK/` — The primary database and content root.
  - `_fcs/` — The application logic, documentation, templates, and action requests.
  - `manuscript/` — The structured content nodes (parts, foundations, facets, modules).
  - `resources/` — The canonical registry of people, books, institutions, concepts, etc.
  - `views/` — Generated dashboards, rendered read-views, and graph outputs.
  - `reviews/` — Temporary storage for AI review outputs before integration.
  - `output/` — The final master corpus, JSON indexes, and downstream handoff packages.
- `scripts/` — Python automation for validation, rendering, and graph generation.
- `PROGRAM_QUEUE/` — Execution protocol tracking for Manus and ChatGPT.
- `99_FINAL_REPORTS/` — Audit trails and completion reports for major execution phases.

## Logical Data Model
The system treats Markdown files as database records.
1. **Nodes**: Represented by `index.md` files within folders. They define structure, summaries, and metadata.
2. **Modules**: Represented by standalone `.md` files. They contain the actual long-form prose.
3. **Manifests**: Represented by `manifest.md` files. They dictate the exact sequence of children within a folder node.
4. **Resources/Concepts**: Represented by `.md` files in the `resources/` directory. They act as a centralized relational database.

## Operational Boundaries
- **FCS does NOT**: Generate final PDFs, compile static sites, or publish directly to social media.
- **FCS DOES**: Generate a pristine, validated, structurally sound "Master Content Layer" (JSON/Markdown) that downstream systems can reliably consume.

## Failure Modes
- **Orphaned Nodes**: A node exists but is not listed in its parent's manifest. (Caught by `validate.py`).
- **ID Collisions**: Two files share the same YAML `id`. (Caught by `validate.py`).
- **Graph Nulls**: A relation points to an ID that does not exist. (Caught by updated `validate.py` and handled gracefully by `graph.py`).

## Do-Not Rules
- Do NOT use alphabetical prefixes (e.g., `01_`, `02_`) to force ordering inside `manuscript/` files unless it matches the canonical ID. Rely on `manifest.md`.
- Do NOT embed massive prose directly inside an `index.md` folder node. Keep prose in modules.
