# Source of Truth & Canonical Status Protocol — v0.1

**Status:** Candidate yOS Program Mode Protocol
**Source:** ELYSIUM operational development
**Version:** v0.1
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration

> ⚠️ This document defines a candidate yOS Program Mode protocol. It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.

---

## 1. Purpose

The Source of Truth & Canonical Status Protocol defines which system holds the authoritative version of each artifact in yOS Program Mode, and how canonical status is assigned and maintained.

---

## 2. Source of Truth Hierarchy

| Layer | System | Role |
|---|---|---|
| L1 — Canonical | GitHub (main branch) | Authoritative source for all code, scripts, and structured documents |
| L2 — Operational | Notion | Authoritative source for all documentation, protocols, and knowledge |
| L3 — Cross-session | Mem0 | Authoritative source for durable facts and cross-session memory |
| L4 — Working | Manus sandbox | Temporary working copies only — not canonical |
| L5 — Archive | GitHub (COMPLETED/) | Immutable archive of executed prompts |

---

## 3. Canonical Status Definitions

| Status | Meaning |
|---|---|
| CANONICAL | Authoritative, validated, approved by Founder + Chief Architect |
| CANDIDATE | Proposed, not yet validated — must not be treated as canonical |
| DRAFT | Work in progress — not ready for review |
| DEPRECATED | Superseded by a newer canonical version |
| ARCHIVED | No longer active, preserved for reference |

---

## 4. Promotion Protocol

A CANDIDATE artifact may only be promoted to CANONICAL after:

1. Founder review and approval
2. ChatGPT Chief Architect review and approval
3. Explicit promotion instruction in a signed MPM
4. Update of status label in all copies (GitHub, Notion, Mem0)

Manus may NOT promote CANDIDATE to CANONICAL autonomously.

---

## 5. Conflict Resolution Rules

When the same artifact exists in multiple systems with different content:

1. GitHub main branch takes precedence over Notion
2. Notion takes precedence over Mem0
3. Mem0 takes precedence over Manus sandbox
4. If conflict cannot be resolved automatically, escalate to Founder

---

## 6. Canonical Paths

### GitHub Canonical Paths

| Content Type | Canonical Path |
|---|---|
| yOS Pattern Library | `07_YOS_PATTERN_LIBRARY/` |
| Program Queue | `PROGRAM_QUEUE/` |
| Book content | `BOOK/` |
| Ontology | `02_ONTOLOGY_AND_KNOWLEDGE/` |
| Final reports | `99_FINAL_REPORTS/` |

### Notion Canonical Paths

| Content Type | Canonical Path |
|---|---|
| yOS protocols | yOS / [Protocol Name] |
| Program Mode docs | yOS / Program Mode / [Doc Number] |
| ELYSIUM | yOS / ELYSIUM / |
| Session archives | Manus Memory — Sessions |

---

## 7. Immutability Rules

The following must never be modified without explicit Founder authorization: any file tagged as CANONICAL in GitHub, any Notion page marked as CANONICAL, any Mem0 entry marked as CANONICAL, the SHA256SUMS.txt file in GitHub, and Git tags on canonical commits.

---

## 8. Drift Detection

Drift occurs when GitHub and Notion versions differ, Mem0 contains outdated facts, or a CANDIDATE was treated as CANONICAL.

Drift must be reported in the completion report and logged in the Reconciliation Backlog (Doc 98).

---

## 9. Notion Reference

Notion page: yOS / Program Mode / 13 Source of Truth & Canonical Status Protocol
