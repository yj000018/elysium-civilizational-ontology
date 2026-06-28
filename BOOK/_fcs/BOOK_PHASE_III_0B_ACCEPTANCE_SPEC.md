# ELYSIUM Phase III-0B Acceptance Specification

**Status:** CANONICAL
**Phase:** Phase III-0B
**Last Updated:** 2026-06-27

## Purpose
This document defines the strict criteria that must be met for Phase III-0B (FCS Book Architecture & Master Content Plan) to be considered COMPLETE.

## Scope
Phase III-0B is an architectural pass. It must produce the structural scaffolding, the narrative strategy, and the AI action queue for future drafting. It must *not* produce long-form prose chapters.

## Acceptance Criteria

### 1. Structural Validation
- `python scripts/validate.py BOOK` must exit with code `0`.
- 0 errors are permitted.
- Warnings are only permitted if they relate to expected missing summaries/promises on placeholder nodes that are explicitly deferred to future phases.

### 2. Architecture Documentation
The following 13 core documents must exist, be fully populated (no "TBD" placeholders), and provide operational guidance:
1. `BOOK_MASTER_CONTENT_PLAN.md`
2. `BOOK_NARRATIVE_SPINE.md`
3. `BOOK_READER_JOURNEY.md`
4. `BOOK_PART_ARCHITECTURE.md`
5. `BOOK_CHAPTER_MODEL.md`
6. `BOOK_MODULE_MODEL.md`
7. `BOOK_DRAFTING_SEQUENCE.md`
8. `BOOK_STYLE_AND_VOICE_GUIDE.md`
9. `BOOK_AI_PRODUCTION_STRATEGY.md`
10. `BOOK_REVIEW_STRATEGY.md`
11. `BOOK_RESOURCE_EXTRACTION_PLAN.md`
12. `BOOK_CONCEPT_GRAPH_PLAN.md`
13. `BOOK_PHASE_III_0B_ACCEPTANCE_SPEC.md`

### 3. Manuscript Scaffolding
- Top-level parts (01_opening through 05_appendices) must exist with valid `index.md` and `manifest.md` files.
- All 7 foundations (F01 through F07) must exist under `02_foundations` with valid `index.md` and `manifest.md` files.
- All 38 canonical facets must be scaffolded with `index.md` and `manifest.md` files.
- Module scaffolds must be created for at least the opening and F01 to demonstrate the structure.

### 4. Action Queue
- At least 5 action requests must exist in `BOOK/_fcs/action_requests/active/`.
- All action requests must be marked `status: DRAFT_ACTION` and `execute_now: false`.

### 5. Graph and Render Scripts
- `python scripts/graph.py` must succeed and produce updated JSON and Mermaid files.
- `python scripts/render.py master BOOK/manuscript` must succeed and compile the available scaffolds into a single master document.

### 6. Final Reporting
- `PHASE_III_0B_ACCEPTANCE_EVIDENCE.md` must contain the output and exit codes of all validation commands.
- `PHASE_III_0B_SELF_AUDIT.md` must evaluate each criterion as PASS/FAIL.
- The final message to the user must include the real Git branch, commit hash, and tag.
