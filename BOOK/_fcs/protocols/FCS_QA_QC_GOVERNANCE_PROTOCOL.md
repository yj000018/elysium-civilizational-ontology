---
id: FCS_QA_QC_GOVERNANCE_PROTOCOL
title: "FCS QA/QC Governance Protocol"
type: protocol
phase: III-1A
status: ACTIVE
last_updated: "2026-06-28"
---

# FCS QA/QC Governance Protocol

## Purpose
Define who owns QA/QC authority in the ELYSIUM production system and how automated, delegated, and final review layers interact.

---

## 1. QA/QC Authority Model

The QA/QC authority model ensures strict separation of concerns between operational execution, prose generation, and architectural validation.

*   **Manus:** May execute QA/QC tasks, run scripts, inspect files, produce audit reports, and apply safe metadata/process patches. Manus is an orchestrator and operational auditor, not a final architectural authority.
*   **Automated Scripts:** May detect structural, metadata, validation, registry, and compilation errors (e.g., `validate.py`).
*   **ChatGPT API Reviewer:** May perform module-level prose review against the writing brief and return PASS / REVISE. This is a local, module-bounded QA.
*   **Claude API:** Is strictly for prose generation. Claude API holds **no** QA authority.
*   **ChatGPT Chief Architect:** Is the final QA/QC authority for architecture, canon, coherence, gates, scope, and approval status.
*   **Founder:** Holds sovereign authority and may override or redirect any decision at any time.

---

## 2. QA/QC Layers

Quality control is executed across five distinct layers, moving from automated structural checks to sovereign human approval.

| Layer | Owner | Scope | Output |
|-------|-------|-------|--------|
| **L0** | Automated Scripts | Structural validation, YAML frontmatter, registries, links | `0 errors, 0 warnings` |
| **L1** | Manus | Operational audit, process adherence, patch application | Audit Reports, Patches |
| **L2** | ChatGPT API | Module-level prose review against writing brief | PASS / REVISE |
| **L3** | Chief Architect | Global review, architecture, canon, coherence, gating | APPROVED / HOLD / REJECTED |
| **L4** | Founder | Sovereign approval, ultimate vision alignment | SOVEREIGN OVERRIDE / APPROVAL |

---

## 3. Hard Rule: Delegation Limits

*   **Operational QA/QC** (L0, L1, L2) **can be delegated** to automated systems and APIs to ensure speed and consistency.
*   **Final architectural QA/QC** (L3, L4) **cannot be silently delegated**. It requires explicit Chief Architect or Founder sign-off. No structural, canonical, or phase-gating decisions can be made without this explicit approval.

---

## 4. Stop Conditions

Any of the following conditions must immediately **stop production**. Execution cannot resume until the condition is resolved and explicitly cleared by the Chief Architect or Founder.

*   Architecture drift
*   Scope drift
*   Canonical contradiction (e.g., mismatch in the number of flows or facets)
*   Metadata/registry mismatch
*   Validation failure (L0 errors > 0)
*   Missing API proof (logs or raw outputs missing)
*   Manus prose contamination (Manus generating book prose instead of Claude API)
*   Unresolved review failure (L2 REVISE loop stuck)
*   Movement/foundation boundary crossing without authorization
*   Truncated prose
*   Incomplete module ending
*   Source draft ending without terminal punctuation
*   Compiled reader truncation
*   Compiled reader/source mismatch
*   Word total mismatch between registry and compiled reader
*   Module count mismatch between source drafts and compiled reader
*   Founder or Chief Architect uncertainty

---

## 5. Approval Semantics

The ELYSIUM production system uses strict terminology for module and architectural status.

*   **DRAFT:** Work in progress, incomplete.
*   **DRAFT_0:** First complete prose generation by Claude API. *Note: DRAFT_0 complete does not equal publication-ready.*
*   **PASS:** ChatGPT API (L2) has reviewed the DRAFT_0 against the brief and found no blocking issues. *Note: ChatGPT API PASS does not equal Chief Architect approval.*
*   **REVISE:** ChatGPT API (L2) has rejected the draft and requires Claude API to regenerate.
*   **APPROVED:** Chief Architect or Founder has explicitly approved the module or architecture.
*   **APPROVED_WITH_PATCHES:** Approved, subject to specific, localized fixes (micro-patches) being applied.
*   **HOLD:** Production or progression is paused pending review or resolution of a stop condition.
*   **REJECTED:** The module or architecture is fundamentally flawed and must be re-architected.
*   **SUPERSEDED:** Replaced by a newer version or architectural decision.

---

## 6. Before Foundation 02 (F02)

Foundation 02 (Vitality) **cannot start** until all the following conditions are met:

1.  End-of-F01 hardening is complete.
2.  F01-000 truncation repaired and re-reviewed via ChatGPT API.
3.  OPN-013 canonical terminology patched from "four flows" to "five flow classes".
4.  F01 metadata and registries are standardized.
5.  `validate.py` returns 0 errors and 0 warnings.
6.  Founder reader draft is regenerated after all repairs.
7.  Compiled reader totals match registry totals.
8.  Compiled reader module count matches all `compile: true` source modules.
9.  Chief Architect explicitly approves F01 (or explicitly approves F02 progression despite pending issues).
