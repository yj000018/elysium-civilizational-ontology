---
id: MULTI_LLM_ORCHESTRATION_RUN_TEMPLATE
type: template
version: "0.1"
phase: yOS/FCS
status: ACTIVE
created_date: "2026-06-28"
---

# Multi-LLM Orchestration Run Template

> Copy this template for every multi-LLM orchestration run.
> Fill in all fields. Never leave routing fields blank.
> If an API is not called, state why explicitly.

---

## 1. Task

**Task ID:** [e.g., PHASE_III_1A_S4_OPN001_PROSE]

**Task description:** [One sentence]

**Phase:** [e.g., III-1A-S4]

**Part / Module:** [e.g., Opening / OPN-001]

---

## 2. Founder Intent

[What the Founder asked for — verbatim or paraphrased]

---

## 3. Routing Preflight

| Field | Value |
|---|---|
| Task classification | [PROSE_GENERATION / ARCHITECTURE_REVIEW / BRIEF_REVIEW / TRANSLATION / RESEARCH / FILE_OPERATION / ...] |
| Complexity | [LOW / MEDIUM / HIGH] |
| Risk | [LOW / MEDIUM / HIGH] |
| Selected mode | [Manus Normal / Manus Max] |
| Manus role | [Orchestration only / File operation / ...] |
| ChatGPT API required | [YES / NO — reason] |
| Claude API required | [YES / NO — reason] |
| Specialist tool required | [YES / NO — which tool] |
| Cost class | [LOW / MEDIUM / HIGH] |

---

## 4. Context Sources

| Source | Path | Used |
|---|---|---|
| Writing Brief | `BOOK/manuscript/.../writing_briefs/OPN-XXX_writing_brief.md` | [ ] |
| X-Ray Card | `BOOK/manuscript/.../xray_modules/OPN-XXX_xray_card.md` | [ ] |
| Prior report | `BOOK/_fcs/reports/...` | [ ] |
| Registry | `BOOK/_fcs/registries/...` | [ ] |
| Other | | [ ] |

---

## 5. API Calls Required

| Model / Tool | Purpose | Required | Status |
|---|---|---|---|
| ChatGPT API | Architecture / coherence review | YES / NO | NOT_CALLED / USED / FAILED |
| Claude API | Prose writing / revision | YES / NO | NOT_CALLED / USED / FAILED |
| Specialist tool | [specify] | YES / NO | NOT_CALLED / USED / FAILED |

**If any API is NOT_CALLED, state reason:**

```text
[API_NOT_CALLED reason — e.g., "ChatGPT API not available in sandbox; manual paste payload created"]
```

---

## 6. Execution Sequence

| Step | Action | Model | Status |
|---|---|---|---|
| 1 | Manus reads context sources | Manus | [ ] |
| 2 | Manus prepares context pack | Manus | [ ] |
| 3 | ChatGPT API architecture/review pass | ChatGPT API | [ ] |
| 4 | Manus applies structural result | Manus | [ ] |
| 5 | Claude API prose pass | Claude API | [ ] |
| 6 | ChatGPT API coherence/review pass | ChatGPT API | [ ] |
| 7 | Claude API revision pass | Claude API | [ ] |
| 8 | Manus validates | Manus | [ ] |
| 9 | Manus commits/pushes/tags | Manus | [ ] |
| 10 | Manus writes completion report | Manus | [ ] |

> Skip steps not required. Mark skipped steps as N/A with reason.

---

## 7. Fallback Rules

| Scenario | Response |
|---|---|
| ChatGPT API unavailable | Create manual paste payload, mark SCAFFOLD_ONLY |
| Claude API unavailable | Mark NOT_CALLED, do not write prose, report BLOCKED |
| API returned unusable output | Mark FAILED, log, escalate |
| Context too large | Split into sub-tasks |

---

## 8. Files to Create / Modify

| File | Action | Status |
|---|---|---|
| `BOOK/manuscript/.../...` | CREATE / MODIFY | [ ] |
| `BOOK/_fcs/registries/...` | UPDATE | [ ] |
| `BOOK/_fcs/reports/...` | CREATE | [ ] |

---

## 9. Validation

```bash
python3 scripts/validate.py BOOK
python3 scripts/status.py BOOK
```

| Check | Result |
|---|---|
| Errors | 0 / [n] |
| Warnings | 0 / [n] |
| Status distribution | SCAFFOLDED: X, DRAFT: X, PLANNED: X |

---

## 10. Decision Gates

| Gate | Required | Status |
|---|---|---|
| Architecture lock | YES / NO | OPEN / CLOSED / PENDING |
| Founder taste/voice | YES / NO | OPEN / CLOSED / PENDING |
| S4 prose authorization | YES / NO | OPEN / CLOSED / PENDING |
| Publication readiness | YES / NO | OPEN / CLOSED / PENDING |

---

## 11. Completion Report Format

```yaml
run_id: [TASK_ID]
run_status: COMPLETED / PARTIAL / BLOCKED / FAILED
manus_role: ORCHESTRATION_ONLY
chatgpt_api_status: NOT_REQUIRED / USED / FAILED / NOT_CALLED_SCAFFOLD_ONLY
claude_api_status: NOT_REQUIRED / USED / FAILED / NOT_CALLED
specialist_tool_status: NOT_REQUIRED / USED / FAILED / NOT_CALLED
routing_status: COMPLETE / PARTIAL / BLOCKED
fallback_status: NONE / PROVISIONAL_MANUS_OUTPUT / SCAFFOLD_ONLY / BLOCKED
approval_status: PENDING / APPROVED / REJECTED
cost_class: LOW / MEDIUM / HIGH
api_calls:
  chatgpt: 0 / n
  claude: 0 / n
  specialist: 0 / n
git_commit: [hash]
git_tag: [tag]
mem0_status: SUCCESS / FAILED / SKIPPED
```
