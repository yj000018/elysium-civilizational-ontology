# ELYSIUM Book Concept Graph Plan

**Status:** CANONICAL
**Phase:** Phase III-0B
**Last Updated:** 2026-06-27

## Purpose
This document defines how abstract ideas and theoretical constructs are mapped across the manuscript to ensure conceptual consistency and enable non-linear reading.

## What is a Concept?
A concept is a specific theoretical construct used within the ELYSIUM ontology. It is not a structural part of the book (like a facet or a module), but an idea that might appear in multiple places.
Examples: `metabolic_limits`, `hyper-fragility`, `regenerative_design`, `thermodynamic_debt`.

## The Concept Graph
While the *Content Graph* maps how chapters and modules relate structurally, the *Concept Graph* maps how ideas flow through the text. If a reader wants to understand `thermodynamic_debt`, the concept graph will show them every module that discusses it.

## Implementation Mechanics
1. **Frontmatter Tagging:** Every module has a `concepts:` list in its YAML frontmatter.
2. **Concept Files:** Each unique concept has a corresponding markdown file in `BOOK/views/concepts/` (e.g., `thermodynamic_debt.md`) containing a brief definition.
3. **Automated Linking:** The `graph.py` script reads the frontmatter tags and generates `BOOK/views/graph/concept_graph.json` and `.mmd`, visualizing which modules share which concepts.

## Phase III-0B Status
A small set of test concepts (e.g., `metabolic_foundation`, `transition_dynamics`) are currently used in the scaffolded nodes to validate the scripts. The full concept dictionary will be built iteratively as the drafting progresses.

## Rule for Concept Creation
Do not create concepts preemptively. A concept should only be added to the graph if it is actively used as a load-bearing idea in the drafted text. Over-tagging creates a noisy, useless graph.
