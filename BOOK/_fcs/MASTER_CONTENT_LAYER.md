# Master Content Layer

## Purpose
The Master Content Layer is the ultimate, pristine output of the FCS. It serves as the single source of truth for the entire ELYSIUM ontology.

## Scope
This layer represents the structured, validated, and approved corpus of knowledge. It is completely decoupled from presentation logic, formatting (like PDF styling or web CSS), or specific downstream media formats.

## Objects Managed
The Master Content Layer consists of:
1. **The Core Manuscript**: The hierarchy of Parts, Foundations, Facets, and Modules.
2. **The Resource Registry**: A normalized database of people, institutions, books, and concepts.
3. **The Relational Graph**: The explicit connections (supports, depends_on, contrasts_with) between all nodes and resources.
4. **Metadata & State**: Review statuses, summaries, reader promises, and AI action histories.

## File Conventions
- The layer is physically realized in the `BOOK/output/` directory.
- `master_corpus/full_source.md` contains the flattened, frontmatter-stripped prose.
- `json/` contains the machine-readable graph and resource data.
- `handoff_packages/` contains bundles specifically formatted for downstream ingestion.

## Workflow
1. Content is drafted and iterated in `BOOK/manuscript/`.
2. Scripts validate and compile the content.
3. The `render.py` and `graph.py` scripts generate the Master Content Layer artifacts.

## Downstream Consumption
Once the Master Content Layer is compiled, other systems (like a static site generator, a PDF typesetting engine, or a slide deck builder) can consume the JSON and Markdown files. Because the layer is structurally validated, downstream systems do not need to perform complex parsing or error correction.

## Failure Modes
- **Incomplete Compilation**: If `render.py` fails due to manifest errors, the Master Content Layer will be incomplete.
- **State Leakage**: Draft or unverified content leaking into the final handoff packages. (Prevented by strict status filtering during generation).

## Do-Not Rules
- Do NOT manually edit files inside `BOOK/output/`. They are generated artifacts.
- Do NOT include HTML, CSS, or specific formatting tags in the source manuscript that would pollute the Master Content Layer.
