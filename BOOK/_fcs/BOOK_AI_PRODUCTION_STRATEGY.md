# ELYSIUM Book AI Production Strategy

**Status:** CANONICAL
**Phase:** Phase III-0B
**Last Updated:** 2026-06-27

## Purpose
This document defines how AI agents are orchestrated to produce the ELYSIUM manuscript within the Fractal Content Studio (FCS) infrastructure.

## The Principle of Separation of Concerns
We do not use a single AI prompt to "write a chapter." We separate architecture, drafting, review, and repository management across specialized roles.

## The AI Roles

### 1. CHATGPT_CHIEF_ARCHITECT
- **Function:** Strategic direction, structural integrity, and canonical alignment.
- **Tasks:** Designs the part/chapter/module map. Writes the scaffolds, executive summaries, and reader promises. Reviews Claude's drafts to ensure they align with the 126 integrated models and the 12-step matrix.
- **Platform:** ChatGPT (Web interface, driven by the Founder).

### 2. CLAUDE_WRITER
- **Function:** Long-form prose generation.
- **Tasks:** Takes a module scaffold (with its drafting instructions, source requirements, and style guide) and generates the actual book text.
- **Platform:** Anthropic API (invoked programmatically by Manus).

### 3. CLAUDE_REVIEWER
- **Function:** Stylistic and rhetorical critique.
- **Tasks:** Reviews drafts specifically against the `BOOK_STYLE_AND_VOICE_GUIDE.md`. Flags generic futurism, academic dryness, or tone inconsistencies.
- **Platform:** Anthropic API (invoked programmatically by Manus).

### 4. MANUS_OPERATOR
- **Function:** Autonomous execution, repository management, and pipeline orchestration.
- **Tasks:** Reads action requests, creates directory structures, runs scripts, invokes Claude API, commits to GitHub, and generates status reports.
- **Platform:** Manus Agent (Autonomous).

### 5. FCS_SCRIPTS
- **Function:** Deterministic validation and compilation.
- **Tasks:** `validate.py`, `render.py`, `graph.py`, `status.py`, `resources.py`. Ensures the markdown files form a valid, unbroken graph and compile correctly.
- **Platform:** Python environment within the Manus sandbox.

## The Production Loop
1. **Plan:** Chief Architect defines the structure and creates action requests in `action_requests/active/`.
2. **Execute:** Manus Operator reads the queue, prepares the context, and invokes Claude Writer via API.
3. **Draft:** Claude generates the markdown prose and saves it to the manuscript directories.
4. **Validate:** Manus runs FCS scripts to ensure the new files haven't broken the graph or validation rules.
5. **Review:** Claude Reviewer or Chief Architect analyzes the output.
6. **Refine:** Iterative updates until the module reaches `STATUS: DRAFT_INTEGRATED_QA_PENDING`.
