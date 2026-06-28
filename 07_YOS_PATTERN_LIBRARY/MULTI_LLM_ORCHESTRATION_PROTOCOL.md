# 21 — Multi-LLM Orchestration Protocol
**yOS Program Mode | Version 0.1 | 2026-06-28**
**Status:** CANDIDATE_YOS_CORE_PATTERN_PENDING_NOTION_RECONCILIATION

---

## Core Principle

> **Manus is the orchestration layer, not the authoring layer.**

> Founder gives intent once.
> Manus routes tasks between LLMs via API.
> Founder is consulted only at decision gates, approval gates, risk gates, or ambiguity gates.

---

## Purpose

Remove Founder copy-paste loops between Manus, ChatGPT, Claude, and future specialist models.

The intended workflow:
1. Founder gives intent once
2. Manus decomposes the task
3. Manus routes subtasks to the right LLM VIA API
4. ChatGPT API handles architecture, coherence, ontology alignment, structural review
5. Claude API handles prose generation, literary density, voice, flow, and revision
6. Specialist tools/models handle specialized outputs when needed
7. Manus collects outputs, validates, updates files, commits, reports
8. Founder is asked only at real decision gates

---

## Role Matrix

| Role | Responsibilities |
|---|---|
| **Founder** | Intent, taste, constraints, approvals, decision gates |
| **Manus** | Orchestration, files, Git, validation, reports — NOT authoring |
| **ChatGPT API** | Architecture, ontology alignment, coherence, writing brief review |
| **Claude API** | Prose writing, voice, flow, literary density, revision |
| **Specialist tools** | Diagrams, research, formatting, translation, data |

---

## API Invocation Rule

When using another model, Manus must explicitly call the model **VIA API**.

If Manus cannot call the API, it must mark output:
```
API_NOT_CALLED
SCAFFOLD_ONLY
PROVISIONAL_MANUS_OUTPUT
```

**Silent fallback is forbidden.**

---

## Standard Orchestration Loop

1. Founder intent
2. Manus task decomposition
3. Routing preflight
4. Manus prepares context pack
5. ChatGPT API architecture/review pass
6. Manus applies structural result
7. Claude API prose pass (if writing authorized)
8. ChatGPT API coherence/review pass
9. Claude API revision pass (if required)
10. Manus validates
11. Manus commits/pushes/tags
12. Manus writes completion report
13. Founder receives decision-ready output

---

## Gate Model

**Stop and ask Founder at:**
- Architecture lock gate
- Founder taste/voice gate
- Major split/merge/remove decision
- Factual uncertainty gate
- Risk gate
- Cost escalation gate
- Publication readiness gate
- S4 prose authorization gate

**Do NOT ask Founder for:**
- Routine file paths
- Mechanical registry updates
- Known branch names if inferable
- Repeated copy-paste
- Reports readable from repo
- Obvious validation reruns

---

## Output Labeling (required on every routed artifact)

```yaml
manus_role:
chatgpt_api_status: NOT_REQUIRED | USED | FAILED | NOT_CALLED_SCAFFOLD_ONLY
claude_api_status: NOT_REQUIRED | USED | FAILED | NOT_CALLED
routing_status:
fallback_status: NONE | PROVISIONAL_MANUS_OUTPUT | SCAFFOLD_ONLY | BLOCKED
approval_status: PENDING | APPROVED | REJECTED
```

---

## Founder Burden Minimization Rule

- If input exists in repo → Manus reads it
- If prior report exists → Manus reads it
- If ChatGPT output can be passed via API → Manus passes it
- If Claude can be called via API → Manus calls it
- If manual handoff unavoidable → Manus creates **single copy-paste payload**

---

## Inheritance

This protocol extends:
- yOS Routing Matrix v0.2 (Procedural Memory)
- yOS Program Mode Doc 11 — Model Routing & Agent Roles Protocol
- FCS LLM Routing Matrix Protocol v0.2

It does NOT replace the existing yOS Routing Matrix.
It is a **FCS/ELYSIUM operational specialization**.

---

## FCS Files

- Protocol: `BOOK/_fcs/protocols/FCS_MULTI_LLM_ORCHESTRATION_PROTOCOL.md`
- Registry: `BOOK/_fcs/registries/llm_orchestration_registry.yaml`
- Run Template: `BOOK/_fcs/templates/MULTI_LLM_ORCHESTRATION_RUN_TEMPLATE.md`
- GitHub: `07_YOS_PATTERN_LIBRARY/MULTI_LLM_ORCHESTRATION_PROTOCOL.md`
