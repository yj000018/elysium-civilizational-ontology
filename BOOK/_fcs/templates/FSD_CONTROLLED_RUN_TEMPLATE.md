---
id: FSD_CONTROLLED_RUN_TEMPLATE
artifact_type: template
version: 0.1
---

# FSD Controlled Run Template

## 1. Approved Scope

```yaml
scope_name: "[e.g., MOV-II Controlled Auto]"
authorized_by: "[Founder name + date]"
autonomy_level: 2
```

## 2. Autonomy Level

Level: [0 / 1 / 2 / 3]
Rationale: [Why this level was chosen]

## 3. Included Modules

```yaml
modules:
  - [MOD-ID-1]
  - [MOD-ID-2]
  - [MOD-ID-3]
```

## 4. Excluded Modules

```yaml
excluded:
  - [MOD-ID]: [reason]
```

## 5. Critical Modules

```yaml
critical_modules_in_scope:
  - [MOD-ID]: [reason — e.g., OPN-008 metabolic pivot]
critical_module_authorization_required: true/false
```

## 6. Proceed Conditions

All must be true before continuing to next module:

- [ ] claude_api_status: SUCCESS
- [ ] chatgpt_api_review: PASS
- [ ] validation_status: CLEAN
- [ ] git_status: CLEAN_OR_COMMITTABLE
- [ ] secret_safety: PASS
- [ ] module_not_critical: true
- [ ] no_architecture_drift: true
- [ ] no_tone_drift: true
- [ ] word_count_in_range: true
- [ ] previous_module_saved_as_DRAFT_0: true

## 7. Stop Gates

Active for this run:

- [ ] chatgpt_review_revise
- [ ] chatgpt_review_fail
- [ ] api_failure
- [ ] critical_module
- [ ] architecture_drift
- [ ] tone_drift
- [ ] validation_error
- [ ] validation_warning
- [ ] secret_safety_issue
- [ ] git_conflict
- [ ] movement_boundary
- [ ] founder_decision_required

## 8. Module Loop

For each module:

1. Preflight
2. Read previous module draft
3. Read current writing brief + X-Ray
4. Build context pack
5. Call Claude API
6. Call ChatGPT API for review
7. Handle PASS / REVISE / FAIL
8. Save DRAFT_0
9. Update registries
10. Validate
11. Commit

## 9. API Routing

| Task | Model | API |
|---|---|---|
| Prose generation | claude-opus-4-5 | Anthropic API |
| Prose review | gpt-4o-2024-08-06 | OpenAI API (direct) |

## 10. Validation

Target: 0 errors, 0 warnings

Run after each module:
```bash
python3 scripts/validate.py BOOK
```

## 11. Commit Strategy

```yaml
commit_strategy:
  per_module: true
  per_scope_end: true
  tag: at_scope_end
  tag_format: "phase-xxx-mov-x-controlled-auto"
```

## 12. Scope Completion Report

Path: `BOOK/_fcs/reports/[PHASE_ID]_[SCOPE_NAME]_CONSOLIDATED_REPORT.md`

Required sections:
- Run status
- Modules completed
- Modules failed/stopped
- API token summary
- Validation status
- Git status
- Mem0 status
- Next recommended action

## 13. Founder Decision Request

Path: `BOOK/_fcs/action_requests/active/[PHASE_ID]_[SCOPE_NAME]_FOUNDER_REVIEW_REQUEST.md`

Required decisions:
- Approve all DRAFT_0 modules
- Authorize next scope
- OR: request revisions / hold
