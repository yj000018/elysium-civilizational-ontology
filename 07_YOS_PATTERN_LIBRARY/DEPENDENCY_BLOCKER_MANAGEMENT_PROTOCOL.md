# Dependency & Blocker Management Protocol — v0.1

**Status:** Candidate yOS Program Mode Protocol
**Source:** ELYSIUM operational development
**Version:** v0.1
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration

> ⚠️ This document defines a candidate yOS Program Mode protocol. It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.

---

## 1. Purpose

The Dependency & Blocker Management Protocol defines how yOS Program Mode identifies, tracks, classifies, escalates, and resolves dependencies and blockers across complex programs.

Core principle: A blocked program must say exactly what it is waiting for and who can unblock it.

---

## 2. Blocker States

Allowed blocker states: NO_BLOCKER, WAITING_ON_FOUNDER, WAITING_ON_CHIEF_ARCHITECT, WAITING_ON_MANUS, WAITING_ON_FCS, WAITING_ON_NOTION, WAITING_ON_GITHUB, WAITING_ON_MEM0, WAITING_ON_CLAUDE_API, WAITING_ON_REVIEW, WAITING_ON_SOURCE_OF_TRUTH, WAITING_ON_RECONCILIATION, SOURCE_OF_TRUTH_CONFLICT, MISSING_INPUT, EXECUTION_MODE_NOT_SPECIFIED, MODE_INSUFFICIENT_FOR_SCOPE, VALIDATION_FAILED.

---

## 3. Severity Levels

| Level | Description |
|---|---|
| Low | Minor delay or clarification needed |
| Medium | Blocks a specific deliverable but not the whole program |
| High | Blocks a major phase or risks downstream rework |
| Critical | Blocks safe execution or could cause irreversible harm |

---

## 4. Dependency Record Template

```
Dependency ID:
Program:
Phase:
Dependency:
Required for:
Current state:
Owner:
Risk if ignored:
Can work continue partially: yes/no
Allowed parallel work:
Blocked work:
Next action:
Due / sequence priority:
Last updated:
```

---

## 5. Blocker Record Template

```
Blocker ID:
Program:
Phase:
Blocker state:
Description:
Blocking:
Not blocking:
Owner:
Severity:
Required action:
Recovery option:
Next actor:
Date detected:
Status:
```

---

## 6. Current ELYSIUM Dependency Map

- Major ELYSIUM Book drafting waits for FCS.
- Phase III-0B depends on FCS review.
- yOS Program Mode canonical integration waits for yOS Notion reconciliation.
- Future FSD waits for stable Program Queue, State Schema, Risk Gates, Recovery Protocol, QA Protocol, and Founder approval.
- Candidate model integration is not required before writing and remains non-canonical unless separately integrated.

---

## 7. Notion Reference

Notion page: yOS / Program Mode / 17 Dependency & Blocker Management Protocol
