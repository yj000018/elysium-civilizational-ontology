# PHASE III-1A-R — ChatGPT Structure Refinement Request

---

**To:** ChatGPT Chief Architect + Founder

**From:** Manus (Executive Orchestrator)

**Date:** 2026-06-28

**Type:** Structure Refinement Request

**Priority:** HIGH — blocks all further writing

---

## Purpose

Use the attached/linked Context Pack and Binder View to refine the Opening Part structure iteratively. No prose writing until structure is validated at every layer.

---

## Context Documents (in this repository)

| Document | Path |
|---|---|
| Context Pack | `BOOK/_fcs/context_packs/PHASE_III_1A_R_OPENING_STRUCTURE_CONTEXT_PACK.md` |
| Binder View | `BOOK/_fcs/binder_views/PHASE_III_1A_R_OPENING_BINDER_VIEW.md` |
| Provisional Module Extraction | `BOOK/_fcs/context_packs/PHASE_III_1A_R_PROVISIONAL_MODULE_EXTRACTION.md` |
| Narrative Spine | `BOOK/_fcs/BOOK_NARRATIVE_SPINE.md` |
| Part Architecture | `BOOK/_fcs/BOOK_PART_ARCHITECTURE.md` |
| Style & Voice Guide | `BOOK/_fcs/BOOK_STYLE_AND_VOICE_GUIDE.md` |
| Drafting Sequence | `BOOK/_fcs/BOOK_DRAFTING_SEQUENCE.md` |

---

## Required Workflow

1. Review Context Pack
2. Review Binder View
3. Review Provisional Module Extraction
4. **Create macro-opening architecture** — how many movements? what is the emotional/intellectual arc of the opening?
5. **Validate with Founder** — confirm or revise
6. **Drill down to movements** — what does each movement accomplish? what is the reader state transition?
7. **Validate** — confirm or revise
8. **Drill down to modules** — what modules exist within each movement? what is each module's purpose?
9. **Validate** — confirm or revise
10. **Drill down to submodules / beats** — what are the paragraph-level beats within each module?
11. **Create executive summaries** — one paragraph per module stating purpose, reader state transition, constraints
12. **Create writing briefs** — voice, pacing, length, references, reader promise per module
13. **Only then hand back to Manus for materialization**

---

## Important Constraints

- Do NOT write prose yet
- Do NOT promote provisional modules to DRAFT_0
- Do NOT skip layers (validate each before drilling deeper)
- Do NOT modify the 7 Foundations / 38 Facets / 12-Step Matrix
- Do NOT rebuild FCS
- The 4 provisional modules are raw material only — mine them for ideas, do not preserve their structure
- Founder has final validation authority at every layer

---

## Key Architectural Decisions Required

1. **How many movements** does the opening have? (The provisional draft implies 4, but this may be wrong)
2. **Full reveal vs. gradual reveal** — should the Seven Foundations be fully revealed in the opening, or teased and gradually revealed?
3. **Emotional hook** — should the opening start with a concrete vignette or an abstract diagnosis?
4. **Module granularity** — are the current 4 modules the right granularity, or should there be more (smaller) or fewer (larger)?
5. **Silo critique** — standalone module or subsection of the diagnosis?
6. **Metabolic metaphor introduction** — full five-dimension breakdown in opening or simplified version?

---

## Deliverables Expected from ChatGPT Session

| Deliverable | Description |
|---|---|
| `opening_ultrafine_toc_v1` | Complete hierarchical TOC: movements → modules → beats |
| `opening_module_map_v1` | Module list with purpose, reader state transition, word target |
| `opening_exec_summaries_v1` | Executive summary per module (one paragraph each) |
| `opening_writing_briefs_v1` | Writing brief per module (voice, pacing, length, references, constraints) |
| Structure validation decision | Founder confirms: STRUCTURE_VALIDATED or REVISION_NEEDED |

---

## Handoff to Manus (after validation)

Once the Founder validates the structure, hand back to Manus with:

1. The validated TOC
2. The module map
3. The executive summaries
4. The writing briefs
5. A clear instruction: "Materialize this structure into FCS files"

Manus will then:
- Create/update manifest files
- Create module scaffolds with correct frontmatter
- Route prose writing to Claude API (not write internally)
- Route structure/content review to ChatGPT API
- Compile, validate, commit

---

## Status After This Request

| Item | Status |
|---|---|
| Opening Part structure | AWAITING_CHATGPT_REFINEMENT |
| Provisional modules | PROVISIONAL_MANUS_DRAFT (raw material only) |
| Writing | BLOCKED until structure validated |
| Next Manus action | WAIT for validated structure from ChatGPT + Founder |
