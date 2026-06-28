# Handoff & Communication Protocol — v0.1

## Status

**Status:** Candidate yOS Program Mode Protocol
**Source:** ELYSIUM operational development
**Version:** v0.1
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration
**Label:** CANDIDATE_YOS_CORE_PATTERN_PENDING_NOTION_RECONCILIATION

> ⚠️ This document defines a candidate Handoff & Communication Protocol for yOS Program Mode. It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.

**Notion page:** https://app.notion.com/p/38d35e218cf88157b8fde080f7d1b126

---

## 1. Purpose

The Handoff & Communication Protocol defines how information moves between Founder, ChatGPT Chief Architect, Manus, Claude API, GitHub, Notion, Mem0, and future sessions.

It prevents: lost context, ambiguous next actions, repeated questions, incomplete handoffs, unclear authority, hidden blockers, tool output confusion, session fragmentation, premature continuation after failure.

Core principle: Every handoff must make the next actor able to act without guessing.

---

## 2. Standard Handoff Types

### Founder → ChatGPT

Founder gives intention, correction, validation, or priority.

Expected ChatGPT response: clarify program state, propose next action, prepare MPM if needed, avoid asking for already-known details, state blockers if any.

### ChatGPT → Founder

Must include: what was decided, what to do next, what to give Manus if relevant, what not to do, expected return artifact.

### Founder → Manus

Instruction should be short:

> Execute the attached one-click Manus prompt fully.

Or:

> Go to the GitHub repository. Read PROGRAM_QUEUE/ACTIVE_PHASE.md and PROGRAM_QUEUE/NEXT_MANUS_PROMPT.md. Execute the prompt fully in the specified execution mode. Return completion report and GitHub commit link.

### Manus → Founder

Returns: completion report, blockers, links, next recommended step.

### ChatGPT → Manus through MPM

ChatGPT gives Manus complete executable instructions in one file or one block.

### Manus → Claude API

Manus calls Claude only if required by prompt.

### Claude API → Manus / ChatGPT

Claude returns review evidence, not final acceptance.

---

## 3. Handoff Packet Requirements

Complete handoff packet: project/program name, current phase, source of truth, execution mode, risk level, active prompt or task, deliverables, blockers, next action, do-not-list if relevant, expected return format.

Minimal handoff: task, file/prompt, mode, expected result.

---

## 4. Completion Handoff from Manus

Must include:

1. run status
2. execution mode used
3. pages/files created or updated
4. Git status
5. Notion status if relevant
6. Mem0 status if relevant
7. Claude status if relevant
8. blockers
9. next recommended step

---

## 5. Failure Handoff

Required: failure class, what succeeded, what failed, what was not attempted, blocker, recovery recommendation, whether continuation is safe.

Do not say complete if status is partial or blocked.

---

## 6. ChatGPT Review Handoff

After reviewing Manus output, ChatGPT should return one of: ACCEPTED, ACCEPTED_WITH_MINOR_NOTES, CHANGES_REQUIRED, BLOCKED, REJECTED, SUPERSEDED, ARCHIVED.

And include: reason, next action, whether Founder needs to decide, whether Manus repair prompt is needed.

---

## 7. Cross-Session Handoff

When moving to a new session, provide: project name, current state, last accepted milestone, active blocker, current phase, source of truth, latest artifacts, relevant decisions, next intended action, strict naming corrections, do-not-list.

For ELYSIUM / yOS: Use yOS only. Do not use WYS. FCS means Fractal Content Studio. Book drafting waits for FCS.

---

## 8. Manus Launch Instruction Templates

### Attached MPM

> Execute the attached one-click Manus prompt fully.

### GitHub Prompt Queue

> Go to the GitHub repository: [repo URL]. Read: PROGRAM_QUEUE/ACTIVE_PHASE.md and PROGRAM_QUEUE/NEXT_MANUS_PROMPT.md. Execute the prompt fully in the specified execution mode. Do not execute archived prompts or backlog items. Commit and push the results. Return only: 1. completion report, 2. GitHub commit link, 3. blockers if any, 4. next recommended action.

### Repair Run

> Execute only the attached repair prompt. Do not redo the full previous task unless explicitly instructed. Return repair report and updated Git/Notion/Mem0 status.

---

## 9. Founder-Facing Output Style

- be direct
- state exact action
- state exact file
- state exact expected return
- avoid vague "continue"
- avoid hidden assumptions

---

## 10. No Background Work Rule

Agents must not claim work will be completed later unless there is an actual scheduled automation.

---

## 11. Handoff Acceptance Criteria

A handoff is valid if the receiving actor knows: what to do, where to look, what mode to use, what not to do, what to return, what counts as success, what to do if blocked.

If not, handoff is incomplete. Status: `HANDOFF_INCOMPLETE`

---

## 12. Current ELYSIUM Application

Current handoff pattern:

1. ChatGPT creates MPM.
2. Founder gives MPM to Manus.
3. Manus syncs Notion / GitHub / Mem0.
4. Founder returns completion report if needed.
5. ChatGPT reviews and prepares next MPM.

Current active dependency: ELYSIUM Book drafting waits for FCS.

---

## 13. Strategic Summary

The Handoff & Communication Protocol makes semi-autonomous work legible. It ensures that every actor receives: enough context, clear authority, exact next action, expected output, failure path.

It is essential for multi-session, multi-agent, multi-project yOS Program Mode.
