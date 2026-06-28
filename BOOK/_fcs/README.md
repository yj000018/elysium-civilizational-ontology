# Fractal Content Studio (FCS)

## Purpose
The Fractal Content Studio (FCS) is an AI-first logical application built directly into the file system of the ELYSIUM repository. Its primary purpose is to structure, navigate, generate, rewrite, review, graph, and consolidate complex content systems into a clean Master Content Layer. 

FCS is **not** a final publishing engine, a Scrivener clone, or a standalone heavy app. It is the structured source corpus factory.

## Scope
FCS manages:
- The ELYSIUM architectural ontology (3 Scales × 7 Foundations × 38 Facets × 12-Step Matrix).
- The source content in markdown.
- Metadata via YAML frontmatter.
- A canonical resource and concept registry.
- AI Action Requests to coordinate ChatGPT Chief Architect, Claude Writer/Reviewer, and Manus Operator.
- Review and status tracking.
- Downstream handoff packaging.

## Core Principles
1. **AI-First Editing**: The founder edits primarily through prompts, command palette actions, AI action requests, dashboards, and graph navigation. Manual text editing is secondary.
2. **YAML as Database**: Every node (folder index or module) is a database record defined by its YAML frontmatter.
3. **Manifest Ordering**: Folder order is strictly controlled by `manifest.md` files, not by alphabetical file names.
4. **Scripted Intelligence**: Python scripts validate structure, generate graphs, compile resources, and render views.

## Quick Start
To operate FCS within Obsidian:
1. Open the repository root in Obsidian.
2. Ensure required plugins are enabled (Dataview, Templater, QuickAdd).
3. Refer to the `OBSIDIAN_OPERATOR_MANUAL.md` for daily workflows.
4. Run `python scripts/validate.py` from the terminal to ensure structural integrity.

## Documentation Index
- `FCS_ARCHITECTURE.md`: Core system architecture.
- `AI_EDITOR_MODEL.md`: How AI interacts with the corpus.
- `AI_ROLE_ROUTER.md`: Which AI agent handles which task.
- `ACTION_REQUEST_MODEL.md`: Structure of AI tasks.
- `NODE_MODEL.md`: Definitions of folder nodes and modules.
- `MANIFEST_MODEL.md`: Ordering and inclusion rules.
- `OBSIDIAN_OPERATOR_MANUAL.md`: Daily usage guide.
