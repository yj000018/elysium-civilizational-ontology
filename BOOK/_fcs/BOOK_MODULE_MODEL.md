# ELYSIUM Book Module Model

**Status:** CANONICAL
**Phase:** Phase III-0B
**Last Updated:** 2026-06-27

## Purpose
This document defines the "Module," the atomic unit of narrative prose in the ELYSIUM manuscript.

## What is a Module?
A module is a cohesive piece of writing (typically 800–2000 words) that explores a specific concept, facet, or intersection of facets. It is the actual text the reader consumes.

## Module Scaffold Structure
Before a module is drafted, it exists as a scaffold (`.md` file) containing metadata and drafting instructions.

### Metadata Frontmatter
- `id`: Unique identifier (e.g., `F01_01_energy_trap`)
- `title`: Working title
- `type`: `module`
- `status`: `PLANNED`, `DRAFTING`, `REVIEW`, etc.
- `parent`: The facet or foundation it belongs to.
- `summary`: One-sentence description.
- `reader_promise`: What the reader gains.
- `matrix_steps`: Which steps of the 12-step matrix this module covers.
- `concepts`: Linked concepts.
- `resources`: Linked resources (people, books, etc.).
- `relations`: Graph edges (`depends_on`, `supports`, etc.).
- `ai_routing`: Which AI agent drafts/reviews it.

### Scaffold Content Sections
- `## Function of this Module`: Its role in the chapter.
- `## Intended Argument`: The core thesis.
- `## Source Requirements`: Which of the 126 models or specific data points must be cited.
- `## AI Drafting Instructions`: Specific prompts for Claude.
- `## Review Risks`: Potential pitfalls (e.g., "might sound too academic").

## Drafting Strategy
Modules are drafted independently by Claude based on their scaffolds, but they must be written to flow sequentially when rendered together via the `manifest.md` order.

## Example Module Types
- **The Diagnostic Module:** Focuses on the current pathological state (Matrix steps 1-4).
- **The Structural Module:** Explains the underlying mechanics and models (Matrix steps 5-8).
- **The Visionary Module:** Describes the regenerative state and transition vectors (Matrix steps 9-12).
