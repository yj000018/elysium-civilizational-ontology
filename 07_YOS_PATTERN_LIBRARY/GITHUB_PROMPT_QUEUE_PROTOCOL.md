# GitHub Prompt Queue Protocol — v0.1

**Status:** CANDIDATE_YOS_CORE_PATTERN_PENDING_NOTION_RECONCILIATION
**Source:** ELYSIUM operational development
**Version:** v0.1
**Notion page:** https://app.notion.com/p/38d35e218cf881c3ad63c02130d6ad2f
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration

> ⚠️ This document describes a candidate yOS Program Mode pattern extracted from ELYSIUM.
> It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.
> Do NOT reinvent yOS. Do NOT overwrite existing yOS architecture.

---

## Purpose

The GitHub Prompt Queue is the operational mechanism that allows Manus to execute the next validated task directly from the GitHub repository instead of relying on repeated copy-paste from Yannick.

It turns GitHub into the execution cockpit for semi-autonomous program work.

Core idea:
```
ChatGPT designs the next prompt
→ Yannick validates
→ Prompt is placed in GitHub
→ Manus fetches and executes it
→ Manus commits results
→ ChatGPT reviews
```

Supported contexts: ELYSIUM, FCS, yOS Program Mode, future books, websites, knowledge systems, complex multi-phase programs.

---

## Design Principles

- **One active prompt only** — `PROGRAM_QUEUE/NEXT_MANUS_PROMPT.md`
- **GitHub is operational source of truth**
- **Prompts are versioned** — every executed prompt archived with timestamp, phase, outcome
- **Human control remains explicit** — semi-autonomous, not full self-driving
- **No hidden scope expansion** — adjacent opportunities go to BACKLOG, not executed

---

## Required Folder Structure

```
PROGRAM_QUEUE/
├── NEXT_MANUS_PROMPT.md
├── ACTIVE_PHASE.md
├── EXECUTION_PROTOCOL.md
├── PROMPT_STATUS.md
├── COMPLETION_REPORT_TEMPLATE.md
├── ARCHIVED_PROMPTS/
├── RUN_LOGS/
└── BACKLOG/
```

---

## Key File Roles

### NEXT_MANUS_PROMPT.md

The only active prompt Manus should execute. Must be:

- Complete and self-contained
- One-click transferable
- Execution mode specified
- Source of truth specified
- Deliverables specified
- Git instructions included
- Mem0 instructions included when relevant
- Claude API rules included when relevant
- Strict do-not-list included

**Rule: If a task is not in NEXT_MANUS_PROMPT.md, Manus must not execute it.**

### ACTIVE_PHASE.md

Defines the current phase. Allowed statuses:

`PLANNED` | `READY_FOR_FOUNDER_REVIEW` | `READY_FOR_MANUS` | `IN_PROGRESS` | `COMPLETED_PENDING_REVIEW` | `CHANGES_REQUIRED` | `ACCEPTED` | `BLOCKED` | `ARCHIVED`

### EXECUTION_PROTOCOL.md

Standing execution rules:

1. Read ACTIVE_PHASE.md first
2. Read NEXT_MANUS_PROMPT.md second
3. Execute only the active prompt
4. Use the specified execution mode
5. Do not modify canonical facts unless explicitly instructed
6. Commit and push all changes
7. Produce a completion report
8. Update PROMPT_STATUS.md
9. Archive executed prompt
10. Report blockers honestly

Also: No silent Claude fallback. No untracked outputs. No scope expansion. No hidden state changes.

### PROMPT_STATUS.md

Allowed statuses: `DRAFT` | `READY_FOR_FOUNDER_REVIEW` | `APPROVED_BY_FOUNDER` | `READY_FOR_MANUS` | `IN_PROGRESS` | `EXECUTED` | `COMPLETED_PENDING_REVIEW` | `ACCEPTED` | `CHANGES_REQUIRED` | `FAILED` | `SUPERSEDED` | `ARCHIVED`

### ARCHIVED_PROMPTS/

Naming convention: `YYYYMMDD_PHASE_PROMPTID_STATUS.md`

### BACKLOG/

Manus may add to BACKLOG, but must not execute backlog items unless they become `NEXT_MANUS_PROMPT.md`.

---

## Manus Execution Instruction

When Yannick asks Manus to run the active prompt:

1. Go to: https://github.com/yj000018/elysium-civilizational-ontology
2. Read: `PROGRAM_QUEUE/ACTIVE_PHASE.md`
3. Read: `PROGRAM_QUEUE/NEXT_MANUS_PROMPT.md`
4. Execute the prompt fully in the specified execution mode
5. Commit and push results
6. Return: completion report + GitHub commit link + blockers + next recommended action

Do not execute archived or backlog prompts.

---

## Queue Safety Rules

Manus must NOT:

- Execute multiple prompts simultaneously
- Execute archived or backlog prompts
- Modify canonical facts without instruction
- Rewrite unrelated files
- Skip completion report
- Skip Git commit
- Claim Mem0 success if failed
- Claim Claude review if fallback used
- Create hidden outputs outside repo
- Leave unclear next state

---

## Git Rules

- Use dedicated branch when appropriate
- Commit all relevant changes
- Push to GitHub when possible
- Include commit hash in completion report
- Tag major milestones
- Avoid untracked outputs

---

## Mem0 Rules

Use Mem0 only when durable facts change.
If Mem0 fails, mark: `MEM0_PERSISTENCE_BLOCKED_RETRY_REQUIRED`

---

## Claude API Rules

- Preferred: `claude-sonnet-4-6` (normal), `claude-opus-4-8` (heavy architectural)
- No silent fallback to ChatGPT if Claude works
- Fallback must be labeled
- Blocked review must be marked as `CLAUDE_REVIEW_BLOCKED`
- No fake Claude review

---

*Extracted from ELYSIUM operational workflow — 2026-06-28*
