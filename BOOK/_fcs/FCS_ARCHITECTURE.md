# FCS Architecture

FCS (Fractal Content Studio) is an AI-first logical app for structuring, generating, rewriting, reviewing, navigating, graphing, and consolidating complex content systems into a clean structured source corpus.

## Core Formula

`FCS = fractal content nodes + Markdown/YAML + manifests + AI action palette + model routing + render views + graph/resource indexes + review/status loops.`

## Master Content Layer

FCS produces the **Master Content Layer**, not final media products. This layer includes:
- structure
- source content
- metadata
- status
- AI action requests
- review states
- concept graph
- resource graph
- content graph
- indexes
- rendered working views
- handoff-ready structured outputs

## Primary Structure

- `BOOK/_fcs/`: Core models, documentation, templates, and action requests.
- `BOOK/manuscript/`: The fractal content nodes (folders with index.md and module files).
- `BOOK/resources/`: Extracted entities (people, concepts, books, etc.).
- `BOOK/views/`: Rendered working views (brief, expanded, review, dashboards).
- `BOOK/reviews/`: Logs of AI and human reviews.
- `BOOK/output/`: Master corpus, graphs, JSON, and downstream handoff packages.
- `scripts/`: Deterministic generation scripts.
- `PROGRAM_QUEUE/`: Action tracking for AI execution.
