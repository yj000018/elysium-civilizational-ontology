---
id: FCS_FSD_CONTROLLED_MODE_PROTOCOL
artifact_type: protocol
version: 0.1
status: INSTALLED_PENDING_FOUNDER_APPROVAL
created_at: "2026-06-28"
extends:
  - BOOK/_fcs/protocols/FCS_MULTI_LLM_ORCHESTRATION_PROTOCOL.md
  - BOOK/_fcs/registries/llm_orchestration_registry.yaml
---

# FCS FSD Controlled Mode Protocol

## 1. Purpose

FSD Controlled Mode is the canonical semi-autonomous execution mode for yOS/FCS. It allows Manus to proceed inside an explicitly approved scope without requiring step-by-step Founder approval, while preserving Founder co-pilot authority at defined gates and maintaining ChatGPT as Chief Architect / control tower.

## 2. Definition

> FSD Controlled Mode is a semi-autonomous execution mode in which Manus may proceed inside an explicitly approved scope, but must stop at predefined gates and return a decision-ready report to the Founder and ChatGPT Chief Architect before continuing.

## 3. Relation to Multi-LLM Orchestration Protocol

This protocol extends the Multi-LLM Orchestration Protocol. The core rule remains unchanged:

> Manus is the orchestration layer, not the authoring layer.

FSD Controlled Mode adds:

> Manus may proceed autonomously inside an explicitly approved scope, but must stop at predefined gates and return with a decision-ready report before continuing.

## 4. Roles

| Role | Responsibility |
|---|---|
| **Founder** | Co-pilot. Sets scope. Approves gates. Validates taste. Authorizes next scope. |
| **Manus** | Autonomous executor inside scope. No authorship. No scope expansion. Stops at gates. |
| **ChatGPT API** | Chief Architect. Review / coherence / structure / ontology alignment. |
| **Claude API** | Prose engine. Revision engine. |

## 5. Autonomy Levels

### Level 0 — Manual

One instruction, one action, stop.

Use for: unclear tasks, high-risk changes, first-time protocols, architecture changes.

### Level 1 — Module-by-module supervised

One module at a time. Stop after each module.

Use for: first prose drafts, style calibration, critical module testing.

*S4-001 to S4-003 used Level 1.*

### Level 2 — Movement-level FSD Controlled

Manus may process all modules in one approved movement, one module at a time internally, using Claude API + ChatGPT API review for each module.

Stop after the movement.

Use for: MOV-II OPN-004 to OPN-006, non-critical movement batches after style is stable.

### Level 3 — Non-critical batch FSD Controlled

Manus may process an approved non-critical batch across a movement boundary only if no critical modules are included.

Stop at any critical module.

### Level 4 — Full FSD Auto

**NOT AUTHORIZED.**

Only allowed after repeated clean Level 2 and Level 3 runs, explicit Founder approval, and stable validation / style / routing.

## 6. Scope Types

```yaml
scope_types:
  - one_module
  - one_movement
  - non_critical_batch
  - whole_part_with_critical_gates
```

## 7. Proceed Conditions

Within an approved FSD Controlled scope, Manus may continue to the next module only if all are true:

```yaml
continue_conditions:
  claude_api_status: SUCCESS
  chatgpt_api_review: PASS
  validation_status: CLEAN
  git_status: CLEAN_OR_COMMITTABLE
  secret_safety: PASS
  module_not_critical: true
  no_architecture_drift: true
  no_tone_drift: true
  word_count_in_range: true
  previous_module_saved_as_DRAFT_0: true
```

If any condition is false: **STOP.**

## 8. Mandatory Stop Gates

Manus must stop immediately and return to Founder + ChatGPT Chief Architect if any of these occur:

### Review gates
- ChatGPT API review = REVISE (after one revision attempt)
- ChatGPT API review = FAIL
- ChatGPT API unavailable
- Claude API unavailable
- Claude output unusable

### Architecture gates
- Module split/merge/move suggested
- Title change suggested
- Movement assignment uncertainty
- Conflict with X-Ray / Writing Brief / Registry
- Critical module reached

### Critical module gates

Always stop before:
- **OPN-008** — metabolic pivot
- **OPN-012** — Seven Foundations FULL_REVEAL_LIGHT

Do not process OPN-008 or OPN-012 inside FSD batch without explicit critical-module authorization.

### Quality gates
- Tone drift
- Style drift
- Word count outside allowed range after revision
- Excessive abstraction
- Over-explanation
- Forbidden content appears
- Continuity failure with previous module
- Next-module leakage

### Operational gates
- Validation error
- Validation warning
- Git conflict
- Branch uncertainty
- Secret/API key risk
- Untracked secret-like file
- Mem0 failure if memory is required
- Cost threshold exceeded

### Founder gates
- Founder decision requested by prompt
- Founder approval status missing when required
- Publication-readiness decision
- Movement boundary reached

## 9. Module Loop

For each module inside an approved scope:

1. Preflight
2. Read previous module draft
3. Read current writing brief
4. Read current X-Ray
5. Build context pack
6. Call Claude API VIA API
7. Save raw Claude output
8. Call ChatGPT API VIA API for review
9. If PASS: save DRAFT_0 → update registries → validate → commit → continue if scope allows
10. If REVISE: perform one Claude revision → final ChatGPT review → if PASS save DRAFT_0; if not PASS STOP
11. If FAIL: STOP
12. At scope end: create consolidated movement report → create Founder review request → commit/tag/push → return decision-ready summary

## 10. Movement-Level Loop

For Level 2 (movement-level FSD Controlled):

1. Receive Founder authorization for scope (e.g., MOV-II OPN-004 to OPN-006)
2. Run module loop for each module in sequence
3. Commit after each successful module
4. At movement end: create consolidated movement report
5. Tag at movement end
6. Return decision-ready summary to Founder + ChatGPT Chief Architect
7. STOP — do not enter next movement automatically

## 11. Critical Module Handling

Critical modules require explicit authorization before processing:

| Module | Reason |
|---|---|
| OPN-008 | Metabolic pivot — major ontological shift |
| OPN-012 | Seven Foundations FULL_REVEAL_LIGHT — core architecture reveal |

When a critical module is reached inside a batch:
1. STOP
2. Report progress to date
3. Request explicit critical-module authorization from Founder
4. Do not proceed until authorization is received

## 12. Reporting Requirements

Every FSD Controlled run must produce:

1. Module-level reports
2. Consolidated scope report
3. Founder review request
4. Updated registry
5. Validation output
6. Git status
7. Mem0 status
8. Stop/continue decision

Required final decision labels:

```yaml
scope_status:
  - COMPLETED_SCOPE
  - PARTIAL_STOPPED_AT_GATE
  - BLOCKED_PRECHECK
  - FAILED

next_decision_required:
  - APPROVE_SCOPE
  - REQUEST_REVISIONS
  - CONTINUE_NEXT_SCOPE
  - HOLD
```

## 13. Git / Validation / Memory Requirements

- Validation: 0 errors, 0 warnings before and after each run
- Git: commit after each successful module; tag at scope end
- Mem0: persist completion fact after each scope
- No secret files tracked or staged

## 14. Current ELYSIUM Application

| Field | Value |
|---|---|
| MOV-I status | DRAFT_0 coverage complete — OPN-001, OPN-002, OPN-003 — pending Founder approval |
| S4-003 operational status | COMPLETED — commit 2588759 |
| Next recommended controlled scope | MOV-II OPN-004 to OPN-006 |
| Autonomy level for MOV-II | Level 2 |
| Stop after | OPN-006 |
| Critical modules in MOV-II | None (OPN-008 is MOV-III) |
| Gate before MOV-III | Founder + ChatGPT Chief Architect review required |

MOV-II may be processed under Level 2 after Founder approves FSD Controlled Mode v0.1.

## 15. Forbidden Moves

- No WYS
- No Manus prose
- No prose without Claude API
- No DRAFT_0 without ChatGPT API PASS
- No silent fallback
- No whole-book auto
- No critical module auto
- No architecture modification during prose batch
- No branch drift
- No secret leakage
