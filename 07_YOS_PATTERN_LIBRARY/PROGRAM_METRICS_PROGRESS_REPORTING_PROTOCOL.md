# Program Metrics & Progress Reporting Protocol — v0.1

**Status:** Candidate yOS Program Mode Protocol
**Source:** ELYSIUM operational development
**Version:** v0.1
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration

> ⚠️ This document defines a candidate yOS Program Mode protocol. It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.

---

## 1. Purpose

The Program Metrics & Progress Reporting Protocol defines how yOS Program Mode reports progress across complex programs without confusing activity with completion.

Core principle: Progress means accepted movement through gates, not just more output.

---

## 2. Progress Status Labels

NOT_STARTED, READY_FOR_PROMPT, READY_FOR_MANUS, IN_PROGRESS, COMPLETED_PENDING_REVIEW, REVIEWED_WITH_ISSUES, CHANGES_REQUIRED, ACCEPTED, BLOCKED, PAUSED, ARCHIVED, SUPERSEDED.

---

## 3. Completion vs Acceptance

Completion means Manus finished a run. Acceptance means the output passed review and can be used downstream. Never report a phase as accepted only because a run completed.

---

## 4. Progress Report Template

```markdown
# Program Progress Report

## 1. Executive Summary

Project:
Current phase:
Overall status:
Main blocker:
Next action:

## 2. Accepted Milestones

## 3. Work Completed Since Last Report

## 4. Work Pending Review

## 5. Blockers / Dependencies

## 6. Risk Items

## 7. Git / Notion / Mem0 / Claude Status

## 8. Decisions Needed

## 9. Next 3 Actions

## 10. Recommended Mode for Next Execution
```

---

## 5. ELYSIUM Current Reporting Example

Project: ELYSIUM
Last accepted milestone: Pass 0.2C
Current work: Phase III preparation
Book drafting: WAITING_ON_FCS
FCS: in external Manus/session development
Allowed work: yOS Program Mode protocols, strategic roadmap, prompt standards
Blocked work: major book drafting
Next action: review FCS output when available; continue yOS Program Mode protocol capture meanwhile

---

## 6. Notion Reference

Notion page: yOS / Program Mode / 18 Program Metrics & Progress Reporting Protocol
