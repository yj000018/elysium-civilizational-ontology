# Review Model

Review in the Fractal Content Studio (FCS) operates on multiple hierarchical levels. The core principle is: **Write locally with AI. Review globally through rendered views. Correct at the source.**

## 1. The Review Hierarchy

The review process scales from atomic modules to the entire manuscript.

- **Module-Level Review:** Fast, tactical review of prose, tone, and immediate factual accuracy. Often handled by the Operator directly in Obsidian.
- **Facet-Level Review:** Ensuring that a cluster of modules correctly delivers the `reader_promise` defined in the facet's `index.md`.
- **Foundation/Part-Level Review:** Strategic review of structural flow, argument progression, and dependency mapping across major sections.
- **Global Review:** Reviewing the `master_corpus` for voice consistency, redundant concepts, and overall narrative arc.

## 2. Review Responsibilities

Different agents handle different types of review to optimize cognitive load.

### 2.1 The Founder (Operator)
- **Focus:** Strategic direction, taste, tone, and final go/no-go decisions.
- **Workflow:** Reviews rendered views (e.g., `render.py review`) and approves AI proposals. Locks nodes (`status: LOCKED`).

### 2.2 ChatGPT Chief Architect
- **Focus:** Structural integrity, canonical alignment, argument progression, and scope discipline.
- **Workflow:** Analyzes the `VALIDATION_REPORT.md` and the `master_corpus`. Identifies logical gaps or missing dependencies. Does not write prose.

### 2.3 Claude Reviewer
- **Focus:** Prose quality, readability, stylistic consistency, and adherence to the ELYSIUM voice.
- **Workflow:** Reviews specific modules flagged for revision. Proposes specific text replacements.

## 3. The Review Workflow

1. **Trigger:** A node reaches `status: REVIEW_PENDING` after AI generation.
2. **Render:** The Operator runs `python scripts/render.py review <path>` to generate a clean review document containing frontmatter, word count, and prose.
3. **Analyze:** The Operator (or an AI agent) reads the review document.
4. **Decision:**
   - **Approve:** Operator updates the source file to `status: LOCKED` and updates `review.last_reviewed_by`.
   - **Reject:** Operator updates the source file to `status: REVISION_REQUIRED`, creates an Action Request detailing the necessary changes, and queues it for the AI Writer.

## 4. Quality Gates

Before a node can be marked `LOCKED`, it must pass these gates:
- `python scripts/validate.py` returns 0 errors for the node.
- All `manifest.md` includes resolve correctly.
- The word count aligns with the structural target.
- The `reader_promise` is explicitly fulfilled.
