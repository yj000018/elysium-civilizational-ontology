---
id: FIX_IT_BOOK_TEMPLATE
title: "FIX IT Book Template"
type: series_template
series: FIX_IT
version: "0.1"
status: ACTIVE
created_by: "Manus — Phase III FCS Publication Family Architecture"
created_date: "2026-06-28"
---

# FIX IT Book Template

## Series Identity

FIX IT is a practical transformation series derived from the ELYSIUM Civilizational Ontology.

Each volume focuses on one societal pillar, domain, or problem and translates the larger ontology into a simple, practical, accessible transformation guide.

FIX IT books are independently readable. They do not require prior knowledge of the ELYSIUM core book or the Great Ontological Synthesis.

## Tone

| Dimension | Guidance |
|---|---|
| Register | Practical, clear, direct |
| Intellectual level | Accessible — less demanding than the ELYSIUM core book |
| Grounding | Fully grounded in the ELYSIUM ontology — but not explicitly cited |
| Reader posture | The reader is a citizen, not a scholar |
| Emotional register | Transformational — moves from diagnosis to agency |
| What to avoid | Jargon, academic hedging, excessive complexity, despair |

## Stable Macro-Template

Every FIX IT volume follows this five-part structure:

---

### Part 1 — See It

**Subtitle:** What feels broken

**Purpose:** Start from lived experience and obvious dysfunction. The reader recognizes the problem immediately. No abstraction yet. No diagnosis. Just the felt reality.

**Tone:** Grounded, empathetic, observational.

---

### Part 2 — Name It

**Subtitle:** What is actually broken

**Purpose:** Move from surface symptoms to the real structural problem. Name the dysfunction precisely. Distinguish symptoms from causes. The reader begins to understand that the problem is not what they thought.

**Tone:** Clear, analytical, revelatory.

---

### Part 3 — Map It

**Subtitle:** The hidden system behind the problem

**Purpose:** Reveal the systemic pattern, dependencies, feedback loops, incentives, culture, and hidden architecture behind the dysfunction. Show why the problem persists despite good intentions and partial solutions.

**Tone:** Systemic, illuminating, non-blaming.

---

### Part 4 — Fix It

**Subtitle:** What must change and how

**Purpose:** Describe repair pathways, leverage points, practical interventions, and actions at different scales. Distinguish between what individuals can do, what communities can do, and what institutions must change.

**Tone:** Practical, actionable, scale-aware.

---

### Part 5 — Transform It

**Subtitle:** What a healthy version could become

**Purpose:** Move beyond repair into regeneration. Describe new institutions, new habits, new imaginaries, and future scenarios. The reader leaves with a vision, not just a diagnosis.

**Tone:** Generative, hopeful, grounded.

---

## Expanded 10-Part Internal Structure

Each macro-part may be further structured into the following internal sections:

| # | Section | Macro-Part |
|---|---|---|
| 1 | What feels broken | See It |
| 2 | What is actually broken | Name It |
| 3 | Why current solutions fail | Name It |
| 4 | The hidden system behind the problem | Map It |
| 5 | What a healthy version would look like | Map It / Transform It |
| 6 | What must change at each scale | Fix It |
| 7 | Practical pathways | Fix It |
| 8 | Individual / community / institutional actions | Fix It |
| 9 | Future scenarios | Transform It |
| 10 | Repair map | Transform It |

## Metadata Requirements

Every FIX IT volume must be registered with the following metadata before production begins:

```yaml
publication_id:
title:                                   # e.g. "FIX IT: Energy"
subtitle:                                # e.g. "How to Repair and Regenerate Our Energy Systems"
publication_type: practical_guide
series: FIX_IT
collection: ELYSIUM_PRACTICAL_TRANSFORMATION
family_id: ELYSIUM_FAMILY
canonical_role:                          # One sentence: what is the unique role of this volume?
source_model: ELYSIUM_CIVILIZATIONAL_ONTOLOGY
related_core_book: ELYSIUM_CORE_BOOK
related_atlas: ELYSIUM_ONTOLOGY_ATLAS
primary_foundation:                      # e.g. F01_ENERGY
secondary_foundations:
  -
related_facets:
  -
target_reader: general_public
tone: practical_transformational
complexity: accessible
format_template: FIX_IT_TEMPLATE
status: CONCEPT
source_language: en
translation_targets: [fr, it, es, de]
prose_status: NOT_WRITTEN
xray_status: NOT_CREATED
routing_status: NOT_ROUTED
```

## Potential Volumes

The following volumes are candidates. Do not create them until explicitly requested.

| # | Title | Primary Foundation |
|---|---|---|
| 1 | FIX IT: Energy | F01_ENERGY |
| 2 | FIX IT: Water | F01_ENERGY |
| 3 | FIX IT: Food | F01_ENERGY |
| 4 | FIX IT: Housing | F02_MATTER |
| 5 | FIX IT: Work | F03_INSTITUTIONS |
| 6 | FIX IT: Education | F04_NARRATIVES |
| 7 | FIX IT: Health | F01_ENERGY |
| 8 | FIX IT: Media | F04_NARRATIVES |
| 9 | FIX IT: Money | F03_INSTITUTIONS |
| 10 | FIX IT: Technology | F02_MATTER |
| 11 | FIX IT: Democracy | F03_INSTITUTIONS |
| 12 | FIX IT: Community | F05_CONSCIOUSNESS |
| 13 | FIX IT: Meaning | F05_CONSCIOUSNESS |
| 14 | FIX IT: Governance | F03_INSTITUTIONS |
| 15 | FIX IT: AI | F02_MATTER |
| 16 | FIX IT: Cities | F02_MATTER |

## Production Rules

1. No FIX IT volume may enter production before its metadata is registered and status is ACTIVE.
2. No prose may be written before the X-Ray structural layer is created and approved.
3. All volumes follow the stable macro-template (See It / Name It / Map It / Fix It / Transform It).
4. Routing rule applies: ChatGPT for structure/content review, Claude for prose writing.
5. Do not modify the 7 Foundations, 38 Facets, or 12-Step Matrix when writing FIX IT volumes.
