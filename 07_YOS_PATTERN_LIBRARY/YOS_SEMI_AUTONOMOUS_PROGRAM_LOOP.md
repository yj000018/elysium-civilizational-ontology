# yOS Semi-Autonomous Program Loop — v0.1

**Status:** CANDIDATE_YOS_CORE_PATTERN_PENDING_NOTION_RECONCILIATION
**Source:** ELYSIUM operational development
**Version:** v0.1
**Notion page:** https://app.notion.com/p/38d35e218cf881f9bafed883920c4353
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration

> ⚠️ This document describes a candidate yOS Program Mode pattern extracted from ELYSIUM.
> It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.
> Do NOT reinvent yOS. Do NOT overwrite existing yOS architecture.

---

## Purpose

The yOS Semi-Autonomous Program Loop defines how large projects such as ELYSIUM, FCS, CasaTAO, yOS Program Mode, future books, websites, and infrastructure systems can be executed by Manus with reduced manual copy-paste while keeping Founder and Chief Architect control.

It is not yet full autonomous execution. It is a controlled loop:

```
Founder intent
→ Chief Architect prompt/spec
→ GitHub Prompt Queue
→ Manus execution
→ GitHub commit/push
→ Completion report
→ Chief Architect review
→ Founder validation
→ next loop
```

**Current mode: Semi-autonomous now. Full self-driving later.**

---

## Core Roles

### Founder — Yannick

Final strategic authority.

- Validates major direction
- Approves prompts before execution when needed
- Gives taste, intuition, and strategic corrections
- Decides whether to proceed, pause, redirect, or escalate
- Does not need to micromanage files

### ChatGPT — Chief Architect

Architectural and editorial coherence authority.

- Designs MPMs
- Defines execution scope
- Prevents drift
- Reviews Manus outputs
- Identifies blockers
- Proposes next action
- Tells Yannick exactly what to do next

### Manus — Executive Orchestrator

Execution engine.

- Reads prompt from GitHub or attached MPM
- Executes in specified mode
- Calls APIs when required
- Writes files
- Commits and pushes to GitHub
- Updates Mem0 when durable facts change
- Produces completion report
- Does not silently change scope

### Claude API — Review Officer

Used for critique, nuance, contradiction detection, editorial review, and heavy coherence checks.

- Prefer `claude-sonnet-4-6` for normal substantial review
- Prefer `claude-opus-4-8` for heavy architectural review
- Do not silently fallback to ChatGPT if Claude works
- If Claude fails, mark `CLAUDE_REVIEW_BLOCKED`

### GitHub — Operational Source of Truth

- Stores canonical files, prompts, outputs, reports
- Supports versioning, branches, tags, diffs, and rollback

### Mem0 — Durable Operational Memory

- Persists only stable facts
- Records accepted canonical decisions
- Records durable process rules

---

## Standard Loop

1. ChatGPT prepares `NEXT_MANUS_PROMPT.md`
2. Yannick validates the prompt
3. Manus fetches `ACTIVE_PHASE.md` and `NEXT_MANUS_PROMPT.md` from GitHub
4. Manus executes in the specified mode
5. Manus commits and pushes results
6. Manus returns completion report and GitHub links
7. Yannick returns to ChatGPT with the report/link
8. ChatGPT reviews and gives next action

---

## Acceptance Gates

A Manus run is accepted only if:

- Required files exist
- Completion report exists
- Git commit exists
- Scope was respected
- No canonical facts were changed without authorization
- No silent fallback occurred
- Mem0 was handled honestly
- Next action is clear

If not, status is `CHANGES_REQUIRED` or `RUN_REJECTED_WRONG_PACKAGE_OR_INCOMPLETE_EXECUTION`.

---

## Current ELYSIUM Application

- ELYSIUM Pass 0.2C accepted
- GitHub: https://github.com/yj000018/elysium-civilizational-ontology
- Mem0 persistence: successful
- Phase III: authorized
- FCS under development in separate session
- Book drafting paused until FCS is ready

---

*Extracted from ELYSIUM operational workflow — 2026-06-28*
