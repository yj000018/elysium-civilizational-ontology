# ELYSIUM Binder View — Phase III-1A-R

---

## 0. Repository / FCS Roots

| Item | Path |
|---|---|
| Repository | `github.com/yj000018/elysium-civilizational-ontology` |
| Branch | `phase-iii/1A-R-opening-context-binder-extraction` |
| Book root | `BOOK/` |
| FCS root | `BOOK/_fcs/` |
| Manuscript root | `BOOK/manuscript/` |
| Scripts | `scripts/` |

---

## 1. Book System / Architecture Files

| File | Role |
|---|---|
| `BOOK/_fcs/FCS_ARCHITECTURE.md` | FCS system design |
| `BOOK/_fcs/BOOK_PART_ARCHITECTURE.md` | 5-part book structure |
| `BOOK/_fcs/BOOK_NARRATIVE_SPINE.md` | Central argument + narrative arc |
| `BOOK/_fcs/BOOK_READER_JOURNEY.md` | Reader transformation map |
| `BOOK/_fcs/BOOK_DRAFTING_SEQUENCE.md` | Iterative drafting phase order |
| `BOOK/_fcs/BOOK_STYLE_AND_VOICE_GUIDE.md` | Voice/tone constraints |
| `BOOK/_fcs/BOOK_AI_PRODUCTION_STRATEGY.md` | AI role routing for production |
| `BOOK/_fcs/BOOK_MODULE_MODEL.md` | Module schema definition |
| `BOOK/_fcs/BOOK_CHAPTER_MODEL.md` | Chapter schema definition |
| `BOOK/_fcs/BOOK_CONCEPT_GRAPH_PLAN.md` | Concept graph strategy |
| `BOOK/_fcs/BOOK_RESOURCE_EXTRACTION_PLAN.md` | Resource management plan |
| `BOOK/_fcs/BOOK_REVIEW_STRATEGY.md` | Review workflow |
| `BOOK/_fcs/MASTER_CONTENT_LAYER.md` | Master content layer definition |
| `BOOK/_fcs/BOOK_MASTER_CONTENT_PLAN.md` | Master content plan |
| `BOOK/_fcs/AI_ROLE_ROUTER.md` | AI agent role definitions |
| `BOOK/_fcs/STATUS_MODEL.md` | Status lifecycle definitions |

---

## 2. FCS Infrastructure

| Directory | Role |
|---|---|
| `BOOK/_fcs/action_requests/active/` | Current active tasks (7 files) |
| `BOOK/_fcs/reports/` | Execution reports |
| `BOOK/_fcs/context_packs/` | Context packs for handoff (this phase) |
| `BOOK/_fcs/binder_views/` | Binder views (this phase) |
| `BOOK/_fcs/templates/` | Module/concept/resource templates |
| `BOOK/_fcs/test_fixtures/` | Validation test data |
| `BOOK/views/dashboards/` | Generated status dashboards |
| `BOOK/views/graph/` | Concept/content graphs |
| `BOOK/reviews/` | Review slots (chatgpt_chief_architect, claude, founder, ai, integration) |
| `BOOK/resources/` | Resource slots by type |
| `BOOK/output/` | Compiled outputs |

---

## 3. Current Opening Part

### Part 01 — Opening

| Module | Path | Words | Status |
|---|---|---|---|
| 01 The Pathology of the Present | `BOOK/manuscript/01_opening/modules/01_pathology_of_present.md` | 1302 | PROVISIONAL_MANUS_DRAFT |
| 02 The Illusion of Silos | `BOOK/manuscript/01_opening/modules/02_illusion_of_silos.md` | 1194 | PROVISIONAL_MANUS_DRAFT |
| 03 Civilization as a Metabolic Entity | `BOOK/manuscript/01_opening/modules/03_metabolic_entity.md` | 1475 | PROVISIONAL_MANUS_DRAFT |
| 04 The Seven Foundations | `BOOK/manuscript/01_opening/modules/04_the_seven_foundations.md` | 1681 | PROVISIONAL_MANUS_DRAFT |
| **TOTAL** | | **5652** | |

Supporting files:
- `BOOK/manuscript/01_opening/manifest.md` — Production plan/manifest

---

## 4. Proposed Refinement Workspace

```
Opening Part (Part 01)
├── Movement 1: [TO_BE_DEFINED_BY_CHATGPT_CHIEF_ARCHITECT_AND_FOUNDER]
│   ├── Module 1.1: [TO_BE_DEFINED]
│   │   ├── Beat 1.1.1: [TO_BE_DEFINED]
│   │   └── Beat 1.1.2: [TO_BE_DEFINED]
│   └── Module 1.2: [TO_BE_DEFINED]
│       ├── Beat 1.2.1: [TO_BE_DEFINED]
│       └── Beat 1.2.2: [TO_BE_DEFINED]
├── Movement 2: [TO_BE_DEFINED_BY_CHATGPT_CHIEF_ARCHITECT_AND_FOUNDER]
│   ├── Module 2.1: [TO_BE_DEFINED]
│   └── Module 2.2: [TO_BE_DEFINED]
├── Movement 3: [TO_BE_DEFINED_BY_CHATGPT_CHIEF_ARCHITECT_AND_FOUNDER]
│   ├── Module 3.1: [TO_BE_DEFINED]
│   └── Module 3.2: [TO_BE_DEFINED]
└── [Additional movements as needed]
```

All structure above is placeholder. The actual architecture will be determined by the Founder + ChatGPT Chief Architect session.

---

## 5. Status Legend

| Status | Meaning |
|---|---|
| `PROVISIONAL_MANUS_DRAFT` | Written by Manus internally; not routed through ChatGPT/Claude; cannot be promoted without routing |
| `STRUCTURE_DRAFT` | Structure proposed but not yet validated by Founder |
| `STRUCTURE_VALIDATED` | Structure validated by Founder + Chief Architect |
| `READY_FOR_MATERIALIZATION` | Validated structure ready for Manus to create FCS files |
| `SCAFFOLDED` | FCS file created with frontmatter but no prose |
| `DRAFT_0` | First prose draft written via proper routing (ChatGPT structure + Claude prose) |
| `REVIEW_PENDING` | Draft awaiting review |
| `DRAFT` | Reviewed and accepted draft |
| `FINAL` | Publication-ready |

---

## 6. Drill-Down Method

The Founder and ChatGPT Chief Architect should refine **one layer at a time**:

```
Book
  → Part (5 parts defined)
    → Movement (emotional/intellectual arc segments)
      → Chapter (if needed)
        → Module (atomic writing unit)
          → Submodule / Beat (paragraph-level structure)
            → Executive Summary (one paragraph: purpose + reader state transition)
              → Writing Brief (voice, pacing, length, references, constraints)
```

**Rules:**
- Validate each layer before drilling deeper
- Do not write prose until the deepest layer is validated
- Each module must have an executive summary before writing begins
- Each module must have a writing brief before Claude receives it
- The Founder has final validation authority at every layer

---

## 7. Book Parts Overview (for context)

| Part | Title | Modules | Status |
|---|---|---|---|
| 01 | Opening | 4 provisional | PROVISIONAL_MANUS_DRAFT |
| 02 | Foundations (F01-F07) | 38 facets scaffolded | SCAFFOLDED |
| 03 | Transition Dynamics | 4 modules scaffolded | SCAFFOLDED |
| 04 | Implementation | 5 modules scaffolded | SCAFFOLDED |
| 05 | Appendices | 4 modules scaffolded | SCAFFOLDED |
