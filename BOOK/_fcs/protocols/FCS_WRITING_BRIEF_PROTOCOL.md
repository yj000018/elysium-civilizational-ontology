---
id: FCS_WRITING_BRIEF_PROTOCOL
artifact_type: protocol
phase: III-1A-S3
status: ACTIVE
version: v0.1
created_by: "Manus — Phase III-1A-S3"
created_date: "2026-06-28"
---

# FCS Writing Brief Protocol v0.1

## 1. Definition

A Writing Brief is a precise module-level instruction artifact for later routed prose generation.

It is **not prose**. It is the architectural-to-prose instruction card that guides Claude (or another prose model) in S4.

A Writing Brief must be generated **before** any prose is written. It must be reviewed and approved by Founder + ChatGPT Chief Architect before S4 begins.

## 2. Lifecycle

```
X-Ray Card (S2X) → Writing Brief (S3) → Founder/CA Approval → Prose Draft (S4, Claude) → Review → Final
```

## 3. Routing

| Role | Responsibility |
|---|---|
| Manus | Scaffold briefs, populate from X-Ray cards, commit/push/report |
| ChatGPT API | Architectural generation/review of brief content |
| Claude | NOT used in S3. Used only in S4 for prose generation. |
| Founder | Final approval before S4 |

## 4. Status Values

| Status | Meaning |
|---|---|
| `BRIEF_SCAFFOLD_ONLY` | Scaffolded by Manus only, no LLM API used |
| `BRIEF_DRAFT` | Populated with architectural content |
| `BRIEF_REVIEWED` | Reviewed by ChatGPT Chief Architect |
| `BRIEF_APPROVED` | Approved by Founder — ready for S4 |
| `BRIEF_REJECTED` | Needs revision |

## 5. Required Fields

Every Writing Brief must include:

1. Module identity
2. Source X-Ray reference
3. Chief Architect decision
4. Readiness status
5. Exact word target (target, min, max)
6. Purpose of the module
7. Reader state in
8. Reader state out
9. Opening direction (directional, not finished sentence)
10. Closing direction (directional, not finished sentence)
11. 3 key concepts to deploy
12. 2 traps to avoid
13. Tone/register note
14. Depth/density note
15. Narrative beats (5)
16. Required cross-references
17. Forbidden moves
18. Source material to mine
19. Resources/quotes placeholders
20. Founder notes placeholder
21. Claude prompt seed for S4
22. ChatGPT review checklist
23. Approval status

## 6. Forbidden Actions

- Do NOT write finished prose
- Do NOT write final opening/closing sentences
- Do NOT call Claude during S3
- Do NOT start S4 before Founder approval
- Do NOT modify 7 Foundations, 38 Facets, 12-Step Matrix

## 7. Validation

Writing briefs use `artifact_type: writing_brief` in frontmatter.
If validate.py rejects `BRIEF_DRAFT` status, use `operational_status: BRIEF_DRAFT` as workaround.

## 8. File Naming

```
BOOK/manuscript/01_opening/writing_briefs/OPN-XXX_writing_brief.md
```

## 9. Registry

All briefs are registered in:
```
BOOK/_fcs/registries/opening_writing_brief_registry.yaml
```

## 10. Review Request

After all briefs are created, create:
```
BOOK/_fcs/action_requests/active/PHASE_III_1A_S3_OPENING_WRITING_BRIEFS_REVIEW_REQUEST.md
```
