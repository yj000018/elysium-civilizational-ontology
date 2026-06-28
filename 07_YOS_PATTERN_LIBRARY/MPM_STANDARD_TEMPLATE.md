# MPM Standard Template — v0.1

**Status:** Candidate yOS Program Mode Pattern
**Source:** ELYSIUM operational development
**Version:** v0.1
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration

> ⚠️ This document is a candidate MPM Standard Template for yOS Program Mode. It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.

---

## 1. Purpose

The MPM (Manus Mega Prompt) Standard Template defines the required structure for every one-click Manus execution prompt in yOS Program Mode.

It ensures that all Manus execution tasks are clear and scoped, versionable and auditable, one-click transferable, GitHub-compatible, Mem0-aware, Claude API-aware, aligned with yOS Program Mode, and safe against scope drift.

---

## 2. Core Rule

Every MPM must be a single transferable object: one file or one complete copy-paste block.

No fragmented prompts. No instructions split across chat and file. No hidden context outside the MPM unless explicitly listed as input.

---

## 3. Required Header

```
# ONE-CLICK MANUS MEGA PROMPT
# [PROJECT] — [PHASE / TASK NAME]

Target system: Manus
Execution mode: Manus Max / Manus Normal / Manus Light
Input source: [GitHub repo / ZIP / Notion / attached files]
Expected output: [files / commit / ZIP / Notion pages / report]
```

---

## 4. Execution Mode Selection

**Manus Max** — architecture, canonicalization, audits, GitHub / Mem0 / API workflows, Claude review, complex writing batches, FCS, book production systems, major yOS protocols, multi-file / multi-phase tasks.

**Manus Normal** — Notion sync, structured documentation insertion, small packaging tasks, controlled report generation, narrow GitHub updates, small repair passes.

**Manus Light / Quick** — small renaming, simple file edits, short verification, micro-corrections, single-document cleanup.

Default for ELYSIUM / FCS / major yOS work: **Manus Max**

---

## 5. Standard MPM Skeleton

```
## 0. Mission
## 1. Context
## 2. Source of Truth
## 3. Authority Hierarchy
## 4. Scope
## 5. Tasks (PART A, B, C...)
## 6. Deliverables
## 7. Git Instructions
## 8. Mem0 Instructions
## 9. Claude API Instructions
## 10. Validation Gates
## 11. Strict Do-Not-List
## 12. Final Response Format
```

---

## 6. Authority Hierarchy

1. Founder / Yannick — final strategic authority
2. ChatGPT Chief Architect — architectural coherence authority
3. Manus — executive orchestrator
4. Claude API — review officer
5. Other tools — specialist support

Manus must not promote candidate ideas to canonical status without Founder / Chief Architect validation.

---

## 7. Validation Gates

This run is complete only if all required files exist, no zero-byte files in canonical paths, Git commit exists, push succeeded, completion report exists, scope was respected, canonical facts were not changed, Mem0 was handled honestly, and Claude API status was logged if used.

If gates fail: Status must be PARTIAL or BLOCKED, not COMPLETE.

---

## 8. MPM Quality Checklist

- One-click transferable
- Execution mode specified
- Source of truth specified
- Scope clear
- Do-not-list present
- Deliverables explicit
- Git instructions present
- Mem0 instructions present
- Claude API rules present if relevant
- Final response format present
- No hidden assumptions
- No conflicting instructions

---

## 9. Prohibition List

Every MPM that touches yOS must include:

```
Do NOT redesign yOS.
Do NOT reinvent yOS.
Do NOT create new yOS architecture.
Do NOT promote candidate patterns into yOS Core.
Do NOT use WYS. Use only yOS.
```

---

## 10. Notion Reference

Notion page: yOS / Program Mode / 03 MPM Standard Template
