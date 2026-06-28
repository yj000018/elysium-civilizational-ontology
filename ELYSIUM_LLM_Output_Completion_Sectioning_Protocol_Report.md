---
id: ELYSIUM_LLM_Output_Completion_Sectioning_Protocol_Report
title: "ELYSIUM — LLM Output Completion & Sectioning Protocol: Implementation Report"
date: "2026-06-28"
branch: phase-iii/1A-S4-llm-output-completion-protocol
tag: phase-iii-1A-S4-llm-output-completion-protocol
status: COMPLETE
f02_started: false
new_book_prose_generated: false
validation_errors: 0
validation_warnings: 0
---

# ELYSIUM — LLM Output Completion & Sectioning Protocol: Implementation Report

**Date:** 2026-06-28
**Branch:** `phase-iii/1A-S4-llm-output-completion-protocol`
**Tag:** `phase-iii-1A-S4-llm-output-completion-protocol`
**Validation:** 0 errors / 0 warnings
**F02 started:** NO
**New book prose generated:** NO

---

## 1. Protocol Created

**File:** `BOOK/_fcs/protocols/LLM_OUTPUT_COMPLETION_AND_SECTIONING_PROTOCOL.md`

The protocol covers 12 sections (as specified in the brief):

| Section | Title | Key Content |
|---------|-------|-------------|
| 1 | Core Distinction | Context window ≠ output limit; no output trusted on context size alone |
| 2 | Universal Output Completion Checks | 11 TRUNCATED/INVALID conditions; mandatory metadata fields per call |
| 3 | No Promotion Rule | Hard rule: TRUNCATED/INCOMPLETE/OUTPUT_UNVERIFIED → cannot be promoted to DRAFT_0 |
| 4 | Auto-Rerun Rule | Rerun once with higher max_tokens; if still truncated → stop and report |
| 5 | Structured Section Generation | Triggers (>2,500w prose, >4,000w report, prior max_tokens hit); semantic split examples |
| 6 | Sectioned Generation Workflow | 8-step workflow: section plan → generate → validate → store → assemble → coherence → QA → promote |
| 7 | Provider Finish Reason Mapping | Normalized `llm_completion_status` field; Anthropic/OpenAI/Google mapping table |
| 8 | QA/QC A Posteriori | Post-generation audit checklists for prose, compiled reader, and QA/QC reports |
| 9 | LLM Matrix Integration | Cross-reference to `LLM_MATRIX.md`; default policy per provider |
| 10 | Script Improvements | `llm_output_guard.py` created; `call_claude_prose.py` and `call_chatgpt_review.py` updated |
| 11 | Reporting Requirements | Module completion report must include 10 LLM completion fields |
| 12 | Stop Conditions | 7 new global stop conditions added |

---

## 2. Files Changed

| File | Action | Change Summary |
|------|--------|----------------|
| `BOOK/_fcs/protocols/LLM_OUTPUT_COMPLETION_AND_SECTIONING_PROTOCOL.md` | **CREATED** | Full protocol, 12 sections |
| `BOOK/_fcs/registries/LLM_MATRIX.md` | **CREATED** | Provider matrix, capability matrix, output limit risk register, finish reason mapping, default policy |
| `scripts/llm_output_guard.py` | **CREATED** | Shared utility: `validate_llm_output_completion()`, `build_llm_metadata()`, `format_completion_block()`, `normalize_finish_reason()`, CLI mode |
| `scripts/call_claude_prose.py` | **UPDATED** | `llm_output_guard` import; `save_output()` now accepts `stop_reason` and `max_tokens`; records `llm_completion_status` in output frontmatter; `CLAUDE_MAX_TOKENS` raised 4,096→6,000; `--max_tokens` arg added; `COMPLETION_STATUS=` printed |
| `scripts/call_chatgpt_review.py` | **UPDATED** | `llm_output_guard` import; `finish_reason` captured from API response; `llm_completion_status` recorded in output frontmatter; `--max_tokens` arg added; `CHATGPT_MODEL` constant defined |
| `scripts/validate.py` | **UPDATED** | `validate_elysium_llm_completion_status()` added — checks all API output files for `llm_completion_status != COMPLETE`; wired into `main()` |
| `BOOK/_fcs/protocols/FCS_QA_QC_GOVERNANCE_PROTOCOL.md` | **UPDATED** | 4 new stop conditions added (prose completion_status, review TRUNCATED, promotion without verification, uncertainty) |
| `BOOK/_fcs/README.md` | **UPDATED** | Links to new protocol and LLM Matrix added |

---

## 3. Script Changes Applied or Deferred

All script changes were applied directly. No changes were deferred.

**Applied:**
- `llm_output_guard.py` created and tested (COMPLETE detection on F01-000, TRUNCATED detection on CLAUDE_REVISED).
- `call_claude_prose.py` updated: `llm_output_guard` integration, `max_tokens` raised to 6,000, `stop_reason` recorded.
- `call_chatgpt_review.py` updated: `llm_output_guard` integration, `finish_reason` captured, `llm_completion_status` in output.
- `validate.py` updated: `validate_elysium_llm_completion_status()` checks all existing API output files.

**Deferred (none):** All changes were low-risk additions. No existing logic was removed.

**Backward compatibility:** All changes are additive. Older API output files without `llm_completion_status` in frontmatter are skipped by the new validator (graceful degradation).

---

## 4. New Stop Conditions Added

**In `FCS_QA_QC_GOVERNANCE_PROTOCOL.md`** (4 new):
- Any prose output with `llm_completion_status != COMPLETE`
- Any review output with `llm_completion_status == TRUNCATED_MAX_TOKENS`
- Any LLM output promoted to DRAFT_0 without verified completion status
- Any uncertainty about whether a text is complete

**In `LLM_OUTPUT_COMPLETION_AND_SECTIONING_PROTOCOL.md`** (7 new global stop conditions, Section 12):
- Any prose output with `completion_status != COMPLETE`
- Any review output with `completion_status == TRUNCATED_MAX_TOKENS`
- Any compiled reader mismatch
- Any missing required section after sectioned generation
- Any model response that says continuation is needed
- Any output where source and compiled version differ unexpectedly
- Any uncertainty about whether a text is complete

**Total stop conditions in `FCS_QA_QC_GOVERNANCE_PROTOCOL.md`:** 21 (was 10, then 17, now 21)

---

## 5. LLM Matrix Integration Status

**File created:** `BOOK/_fcs/registries/LLM_MATRIX.md`

The matrix includes:
- Provider matrix: safe one-shot prose word target, max output tokens, output limit risk, sectioning recommendation, finish_reason availability, retry strategy, review model
- Capability matrix: which LLM is authorized for which task (prose, revision, review, architecture, QA, compilation)
- Output limit risk register: known truncation incidents (F01-000 confirmed), mitigations
- Finish reason mapping: Anthropic/OpenAI/Google raw fields → normalized `llm_completion_status`
- Default policy: 6 rules applying to all ELYSIUM LLM calls

---

## 6. Validation Result

```
FCS VALIDATION REPORT: BOOK
============================================================
Errors: 0
Warnings: 0
Total: 0 errors, 0 warnings
```

All 9 validation functions pass:
- `validate_ids` ✓
- `validate_statuses` ✓
- `validate_manifests` ✓
- `validate_elysium_draft_frontmatter` ✓
- `validate_elysium_canonical_counts` ✓
- `validate_elysium_registries_exist` ✓
- `validate_elysium_f01_seven_flows` ✓
- `validate_elysium_terminal_punctuation` ✓
- `validate_elysium_no_four_flows` ✓
- `validate_elysium_founder_reader_view` ✓
- `validate_elysium_llm_completion_status` ✓ (NEW — all existing API outputs without guard field are skipped gracefully)

---

## 7. Confirmation: F02 Not Started

**F02 has NOT been started.** No F02 branch, no F02 context pack, no F02 modules, no F02 writing briefs created or modified.

---

## 8. Confirmation: No Book Prose Generated

No new book prose was generated in this run. All changes are:
- Protocol and registry files (Markdown)
- Python scripts (utility and production scripts)
- validate.py additions
- FCS README update

---

## 9. Recommended Next Step

**F02 gate remains: HOLD.**

Before F02 can start, the following remain open:

| Condition | Status |
|-----------|--------|
| End-of-F01 hardening complete | ✅ DONE |
| F01-000 truncation repaired + re-reviewed | ✅ DONE |
| OPN-013 terminology patched | ✅ DONE |
| F01 metadata/registries standardized | ✅ DONE |
| validate.py 0 errors / 0 warnings | ✅ DONE |
| Founder Reader Draft regenerated | ✅ DONE |
| Compiled reader totals match registry | ✅ DONE |
| LLM Output Completion Protocol in place | ✅ DONE |
| Chief Architect explicit F01 approval | ⏳ **PENDING** |

**Recommended action:** Submit F01 package to Chief Architect for explicit approval decision. Only after explicit approval can F02 begin.
