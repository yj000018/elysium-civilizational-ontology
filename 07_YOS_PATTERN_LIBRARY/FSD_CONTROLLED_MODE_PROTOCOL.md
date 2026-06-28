---
id: FSD_CONTROLLED_MODE_PROTOCOL
artifact_type: yos_pattern_library
version: 0.1
notion_page_number: 22
status: INSTALLED_PENDING_FOUNDER_APPROVAL
created_at: "2026-06-28"
---

# FSD Controlled Mode Protocol
*yOS Pattern Library — Pattern 22*

---

## Definition

> FSD Controlled Mode is a semi-autonomous execution mode in which Manus may proceed inside an explicitly approved scope, but must stop at predefined gates and return a decision-ready report to the Founder and ChatGPT Chief Architect before continuing.

---

## Why It Exists

Full autonomy (Level 4) is not yet authorized for ELYSIUM. It requires repeated clean runs and explicit Founder approval.

Level 1 (module-by-module supervised) is safe but slow — one Manus session per module.

FSD Controlled Mode (Level 2) allows Manus to process an entire movement (e.g., MOV-II: 3 modules) in one session, while preserving Founder co-pilot authority at movement boundaries and mandatory stop gates.

---

## When to Use

Use FSD Controlled Mode when:

- The scope is explicitly approved by the Founder
- The modules are non-critical (not OPN-008, OPN-012)
- Style and tone are stable (at least one clean Level 1 run completed)
- All proceed conditions are met before each module

---

## When NOT to Use

Do NOT use FSD Controlled Mode when:

- Scope has not been explicitly approved
- A critical module (OPN-008, OPN-012) is in the batch without explicit critical-module authorization
- Style or tone is not yet stable
- Validation is not clean
- Any mandatory stop gate condition is active

---

## Autonomy Levels

| Level | Name | Scope | Status |
|---|---|---|---|
| 0 | Manual | One action | Allowed |
| 1 | Module-by-module supervised | One module | Active (S4-001 to S4-003) |
| 2 | Movement-level FSD Controlled | One movement | Proposed next |
| 3 | Non-critical batch FSD Controlled | Non-critical batch | Future |
| 4 | Full FSD Auto | Broad | **NOT AUTHORIZED** |

---

## Stop Gates

Manus must stop immediately and return to Founder + ChatGPT Chief Architect if any of these occur:

- ChatGPT API review = REVISE (after one revision attempt)
- ChatGPT API review = FAIL
- Any API unavailable
- Critical module reached (OPN-008, OPN-012)
- Architecture drift (split/merge/move/title change)
- Tone drift or style drift
- Validation error or warning
- Git conflict or branch uncertainty
- Secret/API key risk
- Movement boundary reached
- Founder decision requested

---

## Example: ELYSIUM MOV-II

Approved scope: MOV-II OPN-004 to OPN-006

```yaml
scope_name: MOV-II Controlled Auto
modules: [OPN-004, OPN-005, OPN-006]
autonomy_level: 2
stop_after: OPN-006
gate_before_mov_iii: Founder + ChatGPT Chief Architect review required
critical_modules_in_scope: none
```

Manus processes OPN-004, OPN-005, OPN-006 in sequence. Commits after each module. Tags at OPN-006. Returns consolidated report to Founder. Does not enter MOV-III automatically.

---

## Exact Instruction Phrase for Manus

```text
Operate in FSD Controlled Mode.

You may proceed autonomously inside the approved scope only.
You must not exceed the scope.
You must stop at every defined gate.
You must return to Founder + ChatGPT Chief Architect with a decision-ready report before continuing.
No silent fallback.
No prose outside routed Claude API.
No promotion without ChatGPT API review.
No WYS.
```

---

## Related Files

| File | Purpose |
|---|---|
| `BOOK/_fcs/protocols/FCS_FSD_CONTROLLED_MODE_PROTOCOL.md` | Full protocol definition |
| `BOOK/_fcs/registries/fsd_controlled_mode_registry.yaml` | Registry and current application |
| `BOOK/_fcs/templates/FSD_CONTROLLED_RUN_TEMPLATE.md` | Run template |
| `BOOK/_fcs/protocols/FCS_MULTI_LLM_ORCHESTRATION_PROTOCOL.md` | Parent protocol |
| `07_YOS_PATTERN_LIBRARY/MULTI_LLM_ORCHESTRATION_PROTOCOL.md` | yOS pattern library parent |
