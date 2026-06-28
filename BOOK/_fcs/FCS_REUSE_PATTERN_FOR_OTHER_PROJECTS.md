# FCS Reuse Pattern for Other Projects

While currently built for ELYSIUM, the Fractal Content Studio (FCS) architecture is designed to be reusable for other complex knowledge projects.

## 1. Potential Use Cases
- Books and Manifestos
- Documentation Sites
- Knowledge Bases
- Course Curricula
- Program Operating Systems
- Content Universes

## 2. Reusable Layers
To reuse FCS for a new project, the architecture can be decoupled into the following layers:

### A. FCS Core (Reusable)
- The Python script engine (`validate.py`, `render.py`, `graph.py`, `status.py`, `resources.py`).
- The YAML frontmatter schema (`id`, `parent`, `status`, `type`, `relations`).
- The Action Request model and queue system.
- The Obsidian dashboard templates (Dataview queries).

### B. Project-Specific Implementation (Custom)
- The specific taxonomy (e.g., ELYSIUM uses Parts, Foundations, Facets, Modules).
- The Master Content Plan and Narrative Spine.
- The actual Markdown content nodes.

### C. Abstraction Strategy
To extract FCS into a standalone template later:
1. Move `scripts/` to a global utility package.
2. Abstract `BOOK/` to a generic `WORKSPACE/` directory.
3. Replace the hardcoded `ELYSIUM_ROOT` logic in scripts with dynamic root detection.

*Note: Do not build this standalone app now. This document merely outlines the pattern.*
