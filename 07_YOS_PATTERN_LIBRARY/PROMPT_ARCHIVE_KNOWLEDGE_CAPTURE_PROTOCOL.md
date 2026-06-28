# Prompt Archive & Knowledge Capture Protocol — v0.1

## Status

**Status:** Candidate yOS Program Mode Protocol
**Source:** ELYSIUM operational development
**Version:** v0.1
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration
**Label:** CANDIDATE_YOS_CORE_PATTERN_PENDING_NOTION_RECONCILIATION

> ⚠️ This document defines a candidate Prompt Archive & Knowledge Capture Protocol for yOS Program Mode. It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.

**Notion page:** https://app.notion.com/p/38d35e218cf881c4b3adc773e086d0a9

---

## 1. Purpose

The Prompt Archive & Knowledge Capture Protocol defines how yOS Program Mode preserves executed prompts, completion reports, lessons learned, reusable patterns, and failure knowledge.

It prevents: losing good prompts, repeating failed approaches, unclear prompt lineage, inability to audit decisions, loss of operational lessons, messy prompt clutter, hidden drift between versions.

Core principle: Every significant execution should leave behind reusable knowledge.

---

## 2. What Must Be Archived

Archive: executed MPMs, superseded MPMs, failed prompts, repair prompts, completion reports, recovery reports, QA reports, Claude review summaries, important handoff prompts, reusable templates, prompt improvements, lessons learned.

Do not archive every tiny micro-edit unless useful.

---

## 3. Archive Locations

**GitHub:**

```
PROGRAM_QUEUE/ARCHIVED_PROMPTS/
PROGRAM_QUEUE/FAILED_RUNS/
PROGRAM_QUEUE/RUN_LOGS/
PROGRAM_QUEUE/BACKLOG/FUTURE_PROMPTS.md
PROGRAM_QUEUE/BACKLOG/FUTURE_REPAIR_PROMPTS.md
07_YOS_PATTERN_LIBRARY/
99_FINAL_REPORTS/
```

**Notion:**

- yOS / Program Mode / Prompt Archive
- yOS / Program Mode / Lessons Learned
- yOS / Program Mode / Reusable MPM Patterns

---

## 4. Prompt Archive Naming

Format: `YYYYMMDD_PROGRAM_PHASE_PROMPTID_STATUS.md`

Examples:
```
20260628_ELYSIUM_PHASE_III_0A_ELY-P3-0A-FCS-001_EXECUTED.md
20260628_YOS_PM_PROTOCOL_YOS-PM-014_EXECUTED.md
20260628_ELYSIUM_PHASE_III_0A_ELY-P3-0A-FCS-001_FAILED.md
```

Each archived prompt should include: original prompt, prompt ID, date, program, phase, execution mode, risk level, final status, related commit, completion report path, lessons if any.

---

## 5. Knowledge Capture Types

- **Operational lesson:** Mem0 failures may require telemetry mitigation before retry.
- **Prompt design lesson:** Always specify Manus execution mode.
- **Source-of-truth lesson:** Candidate models must not be counted as integrated models.
- **Workflow lesson:** Book drafting should wait for FCS.
- **Tool-routing lesson:** Claude critique must use Claude API and cannot be simulated by ChatGPT.
- **Recovery lesson:** Wrong packages must be rejected before downstream work.

---

## 6. Lessons Learned Entry Template

```
# Lesson Learned

Date:
Program:
Phase:
Source run:
Category:
Summary:
What happened:
What worked:
What failed:
Rule added:
Affected protocols:
Should persist to Mem0: yes/no
Should update template: yes/no
Next action:
```

---

## 7. Reusable Pattern Capture

When a prompt or workflow proves reusable, extract it into: a template, a checklist, a protocol update, a prompt snippet, a Notion page, a GitHub pattern library file.

---

## 8. What Goes to Mem0

Persist only durable lessons: Future MPMs must specify execution mode, Use only yOS not WYS, FCS is the renamed Fractal Content Studio, Book drafting waits for FCS, Claude review must be real Claude API review if claimed.

Do not persist: every archived prompt, every completion report, temporary wording, failed experiments unless they create a durable rule.

---

## 9. What Goes to Notion

Human-readable: protocols, summaries, lessons learned, pattern library, strategic workflows, program dashboards.

Do not overload Notion with every low-level log.

---

## 10. What Goes to GitHub

Exact: prompt files, reports, artifacts, run logs, templates, machine-readable records, version history.

GitHub is the best layer for auditability.

---

## 11. After Each Significant Run

Manus should ask internally:

- should this prompt be archived?
- did this run create a reusable pattern?
- did this run create a durable rule?
- should Mem0 be updated?
- should a template be updated?
- should a backlog item be added?
- did a failure lesson emerge?
- did a protocol need refinement?

---

## 12. Prompt Lineage

```
Original prompt
→ executed prompt
→ completion report
→ review report
→ repair prompt if any
→ accepted output
→ lessons learned
```

---

## 13. Archive Status Labels

EXECUTED, ACCEPTED, CHANGES_REQUIRED, FAILED, BLOCKED, REJECTED, SUPERSEDED, REPAIR, TEMPLATE, LESSON, ARCHIVED

---

## 14. Current ELYSIUM Examples

- Public GitHub is acceptable for ELYSIUM when useful.
- Mem0 failures must be retried and not ignored.
- Claude review must be through Claude API if claimed.
- FCS is prerequisite for major book drafting.
- yOS Program Mode docs are candidate patterns pending reconciliation.
- One-click MPMs are effective for Manus handoffs.
- Execution mode must be explicit in each MPM.

---

## 15. Acceptance Criteria

This protocol is useful if it enables future users to answer: what prompt was run? what did it produce? was it accepted? what commit contains it? what failed? what lesson was learned? what should we do differently next time? is there a reusable template?

---

## 16. Strategic Summary

The Prompt Archive & Knowledge Capture Protocol makes yOS Program Mode cumulative.

It turns each run into: an artifact, a record, a lesson, a reusable pattern, a safer next run.

This is essential for scaling from isolated prompts to a mature operating system.
