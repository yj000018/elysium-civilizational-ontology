# Program Queue Implementation Protocol — v0.1

**Status:** Candidate yOS Program Mode Protocol
**Source:** ELYSIUM operational development
**Version:** v0.1
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration

> ⚠️ This document defines a candidate yOS Program Mode protocol. It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.

---

## 1. Purpose

The Program Queue Implementation Protocol defines the technical implementation of the GitHub-based prompt queue used in yOS Program Mode.

---

## 2. Queue Directory Structure

```
PROGRAM_QUEUE/
├── ACTIVE_PHASE.md          # Current phase description and context
├── NEXT_MANUS_PROMPT.md     # The next MPM to execute (one at a time)
├── QUEUE_STATUS.md          # Queue state: READY / EXECUTING / BLOCKED / EMPTY
├── COMPLETED/               # Archive of executed prompts
│   └── YYYYMMDD_PROMPTID_EXECUTED.md
└── BACKLOG/                 # Future prompts not yet ready
    └── YYYYMMDD_PROMPTID_PENDING.md
```

---

## 3. Queue State Machine

| State | Meaning | Transition |
|---|---|---|
| READY | Prompt available, waiting for Manus | → EXECUTING when Manus starts |
| EXECUTING | Manus is running the prompt | → READY (next prompt) or EMPTY |
| BLOCKED | Cannot proceed, blocker present | → READY when blocker resolved |
| EMPTY | No more prompts in queue | → READY when new prompt added |

---

## 4. Manus Launch Instruction

```
Go to the GitHub repository: [REPO_URL]
Read: PROGRAM_QUEUE/ACTIVE_PHASE.md and PROGRAM_QUEUE/NEXT_MANUS_PROMPT.md
Execute the prompt fully in the specified execution mode.
Do not execute archived prompts or backlog items.
Commit and push the results.
Return only:
1. Completion report
2. GitHub commit link
3. Blockers if any
4. Next recommended action
```

---

## 5. Queue Management Rules

- Only one prompt in NEXT_MANUS_PROMPT.md at a time
- Completed prompts must be moved to COMPLETED/ immediately after execution
- Backlog prompts must not be executed until moved to NEXT_MANUS_PROMPT.md
- QUEUE_STATUS.md must be updated after every execution
- ACTIVE_PHASE.md must be updated when phase changes

---

## 6. Prompt Naming Convention

```
YYYYMMDD_[PROGRAM]_[PHASE]_[PROMPTID]_EXECUTED.md
```

---

## 7. Notion Reference

Notion page: yOS / Program Mode / 10 Program Queue Implementation Protocol
