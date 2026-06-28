# 20 LLM Routing Matrix Protocol v0.2

## Program Mode / ELYSIUM-FCS Operational Patch

> **This is a Program Mode operational patch to the existing yOS Routing Matrix, not a new independent routing doctrine.**

---

## Metadata

| Field | Value |
|---|---|
| Status | Candidate yOS Program Mode Protocol |
| Source | ELYSIUM operational development |
| Version | v0.2 |
| Integration status | Pending yOS Notion reconciliation |
| Authority | Founder + ChatGPT Chief Architect review |
| Operational status | Active routing preflight for ELYSIUM/FCS |
| Inherits from | Y-OS / Procedural Memory / Routing Matrix |
| Notion URL (this page) | https://app.notion.com/p/38d35e218cf881738696d72e64a41ff1 |
| Notion URL (parent matrix) | https://app.notion.com/p/37635e218cf88134b709e095f6c6331f |

---

## Canonical Inheritance from Existing yOS Routing Matrix

This page does not replace the existing Y-OS / Procedural Memory / Routing Matrix.
It operationalizes and specializes it for yOS Program Mode, ELYSIUM, and FCS production.

**Inherited principles:**

- right task → right model → right cost → right output
- do not route every task to the most powerful model
- route according to task type, complexity, cost, latency, context requirements, output quality, implementation risk, and cognitive role
- Manus is reserved for implementation, orchestration, integration, multi-file work, packaging, debugging, and project-level build management
- Manus should not be used for simple drafting, repeated rewriting, early ideation, vague brainstorming, or tasks GPT/Claude can do well

**This Program Mode patch adds:**

- implicit preflight before every ELYSIUM/FCS task
- explicit writing-production routing
- completion gates for writing tasks
- cost-control rules for Manus Max
- fallback labels for blocked APIs
- Phase III-1A correction rule

---

## Core Rule

yOS applies routing implicitly before every task. The LLM Routing Matrix is not an optional instruction. It is a yOS Program Mode preflight rule.

---

## Universal Preflight (10-step)

1. Identify task type
2. Identify complexity
3. Identify risk
4. Identify whether writing is involved
5. Identify whether architecture/content reasoning is involved
6. Identify whether review/critique is involved
7. Identify required tools/models
8. Identify cheapest sufficient execution mode
9. Identify whether Manus Max is justified
10. Identify completion gates

---

## Agent Roles (ELYSIUM/FCS Specialization)

| Agent | Role | Use For |
|---|---|---|
| Manus | Executive orchestrator | FCS, repo, files, Git, Notion, Mem0, scripts, validation, packaging, reports |
| ChatGPT API | Structure/content/architecture | Structural design, content logic, coherence, ontology alignment, specs, prompts |
| Claude API | Primary writing/prose | Long-form prose, drafting, literary density, voice, flow, style, revision |
| Specialist tools | Domain-specific | PDF, slides, images, diagrams, code execution, search, data |

---

## Default Routing Matrix

| Task Classification | Primary | Secondary | Review / Gate |
|---|---|---|---|
| ORCHESTRATION | Manus | none | completion report |
| FILE/GIT/NOTION/MEM0 | Manus | specialist tools | QA |
| STRUCTURE_ARCHITECTURE | ChatGPT API | Manus orchestration | Claude critique if needed |
| CONTENT_LOGIC | ChatGPT API | Claude if prose-sensitive | Chief Architect |
| ONTOLOGY_COHERENCE | ChatGPT API | Claude critique | Chief Architect |
| WRITING / LONG_FORM_PROSE | Claude API | ChatGPT API brief | ChatGPT API + Claude revision |
| REVISION / PROSE STYLE | Claude API | ChatGPT API content notes | Chief Architect/Founder |
| CRITIQUE | Claude API | ChatGPT API if structural | Chief Architect |
| QA_VALIDATION | Manus/scripts | ChatGPT if interpretive | QA protocol |
| RELEASE_READINESS | ChatGPT API | Claude style/critique | Founder |
| CODING/SCRIPTING | Manus/tools | ChatGPT API if design needed | tests |
| RESEARCH | search/tools | ChatGPT synthesis | source citations |
| ARTIFACT_GENERATION | specialist tools | Manus orchestration | artifact QA |

---

## Mandatory Writing Routing

For any writing task (book, chapter, manifesto, essay, narrative, introduction, conclusion, reader-facing prose, FCS manuscript):

1. Manus orchestrates only
2. ChatGPT API creates/validates structure/content brief
3. Claude API writes primary prose
4. ChatGPT API reviews structure/content/coherence
5. Claude API revises prose
6. Manus saves, compiles, commits, reports

---

## Completion Gate

Writing cannot be marked COMPLETED unless routing was applied. If not satisfied, use: PROVISIONAL_MANUS_DRAFT, PROVISIONAL_DRAFT_NOT_FULLY_ROUTED, or PROVISIONAL_DRAFT_NOT_FULLY_REVIEWED.

---

## Fallback Rules

- Claude API unavailable → CLAUDE_API_BLOCKED
- ChatGPT API unavailable → CHATGPT_API_BLOCKED
- Manus writes internally → PROVISIONAL_MANUS_DRAFT → route through APIs later

---

## Cost-Control Rule

Manus Max is not the default. Use only when: complex repo/FCS orchestration, many files, multi-agent API workflow, Git branch/commit/tag/push + reports, failure recovery.

---

## Strategic Summary

The LLM Routing Matrix Protocol v0.2 is an operational patch to the existing Y-OS / Procedural Memory / Routing Matrix. It makes yOS the implicit routing brain for ELYSIUM/FCS production. Prompts describe the task. yOS decides the routing. Manus orchestrates. ChatGPT structures. Claude writes. Completion depends on correct routing, not just file creation.

---

## Commit Message Convention

```
yOS Program Mode docs — patch existing Routing Matrix for ELYSIUM FCS preflight v0.2
```
