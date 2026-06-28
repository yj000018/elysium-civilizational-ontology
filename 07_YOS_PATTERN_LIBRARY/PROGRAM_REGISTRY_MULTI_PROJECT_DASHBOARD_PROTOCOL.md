# Program Registry & Multi-Project Dashboard Protocol — v0.1

**Status:** Candidate yOS Program Mode Protocol
**Source:** ELYSIUM operational development
**Version:** v0.1
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration

> ⚠️ This document defines a candidate yOS Program Mode protocol. It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.

---

## 1. Purpose

The Program Registry & Multi-Project Dashboard Protocol defines how yOS Program Mode tracks, monitors, and reports on multiple concurrent programs.

---

## 2. Program Registry Fields

| Field | Description |
|---|---|
| Program ID | Unique identifier (e.g., ELYSIUM, FCS, YOS-PM) |
| Program Name | Human-readable name |
| Phase | Current phase (e.g., Phase III-0B) |
| Status | ACTIVE / PAUSED / BLOCKED / ARCHIVED |
| Owner | Founder / Yannick |
| GitHub Branch | Active branch URL |
| Notion Root | Root Notion page URL |
| Last Updated | Date of last action |
| Next Action | Next required step |
| Blockers | Current blockers if any |

---

## 3. Registry Location

- **Notion:** yOS / Program Mode / Program Registry
- **GitHub:** `PROGRAM_QUEUE/PROGRAM_REGISTRY.md`
- **Backup:** `07_YOS_PATTERN_LIBRARY/PROGRAM_REGISTRY_MULTI_PROJECT_DASHBOARD_PROTOCOL.md`

---

## 4. Program Status Transitions

| Transition | Trigger |
|---|---|
| NEW → ACTIVE | First MPM executed |
| ACTIVE → PAUSED | Founder decision or resource constraint |
| ACTIVE → BLOCKED | Unresolved blocker for more than 48h |
| BLOCKED → ACTIVE | Blocker resolved |
| PAUSED → ACTIVE | Founder resumes |
| ACTIVE → ARCHIVED | Phase completion + Founder sign-off |

---

## 5. Dashboard Update Protocol

The dashboard must be updated after every MPM execution, after every phase transition, after every blocker resolution, and at minimum once per week for ACTIVE programs.

---

## 6. Current Program Registry (as of v0.1)

| Program | Phase | Status | GitHub Branch |
|---|---|---|---|
| ELYSIUM | Phase III-0B | ACTIVE | phase-iii/fcs-book-architecture-master-plan |
| yOS Program Mode | Documentation repair | ACTIVE | main |

---

## 7. Notion Reference

Notion page: yOS / Program Mode / 09 Program Registry & Multi-Project Dashboard Protocol
