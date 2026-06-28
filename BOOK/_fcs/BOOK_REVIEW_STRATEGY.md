# ELYSIUM Book Review Strategy

**Status:** CANONICAL
**Phase:** Phase III-0B
**Last Updated:** 2026-06-27

## Purpose
This document outlines how content is evaluated, refined, and approved as it moves from scaffold to final manuscript.

## Review Layers

### 1. Structural Validation (FCS Scripts)
- **What it checks:** Broken links, missing IDs, orphaned nodes, invalid YAML frontmatter, empty parent references.
- **Who performs it:** `validate.py` and `graph.py` (run by Manus).
- **Pass condition:** 0 errors, 0 warnings (except documented placeholders).

### 2. Stylistic Review (Claude)
- **What it checks:** Adherence to the `BOOK_STYLE_AND_VOICE_GUIDE.md`. Is the tone authoritative? Is the density high? Are we avoiding generic platitudes?
- **Who performs it:** Claude Reviewer via API.
- **Pass condition:** A clean report indicating the prose matches the Senior Cognitive Architect persona.

### 3. Canonical Alignment Review (Chief Architect)
- **What it checks:** Does the module accurately reflect the 126 integrated models? Does it fulfill its assigned matrix steps without mechanically listing them? Does it align with the core ontology?
- **Who performs it:** ChatGPT Chief Architect.
- **Pass condition:** Chief Architect confirms the conceptual fidelity.

### 4. Founder Review (Yannick)
- **What it checks:** Does this resonate with the overarching vision? Does it serve the "Architect of the New Society" reader?
- **Who performs it:** The Founder.
- **Pass condition:** Manual approval and status update to `FINAL`.

## Status Lifecycle
1. `PLANNED`: Node exists in architecture, no scaffold yet.
2. `SCAFFOLDED`: Frontmatter and structural headings exist.
3. `DRAFTING`: Claude is actively generating prose.
4. `REVIEW`: Draft exists, awaiting stylistic/canonical review.
5. `REVISION`: Draft is being rewritten based on review feedback.
6. `DRAFT_INTEGRATED_QA_PENDING`: Draft is solid, awaiting final holistic read-through.
7. `FINAL`: Approved for publication.

## Handling Review Risks
Each module scaffold includes a `Review Risks` section. Reviewers must specifically check if the drafted module fell into the anticipated trap (e.g., "Risk: This module on energy might become too technical and lose the narrative thread. Check for accessibility.").
