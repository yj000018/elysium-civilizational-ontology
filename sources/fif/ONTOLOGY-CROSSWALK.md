# FiF to ELYSIUM ontology crosswalk

Reading aid from FiF source material onto ELYSIUM facet identifiers. This file does not accept FiF as canon and does not change facet matrices. Identifiers come from [CANONICAL_FACET_ID_MAP.md](../../02_ONTOLOGY_AND_KNOWLEDGE/CANONICAL_FACET_ID_MAP.md). Foundation names come from [ELYSIUM_CORE_ONTOLOGY.json](../../04_DATASETS_AND_MATRICES/ELYSIUM_CORE_ONTOLOGY.json). Machine-readable copy: [ontology-crosswalk.json](data/ontology-crosswalk.json).

## Where the practice sits

FiF is a personal futures-literacy practice: ten civilization-scale transformations, explored through a guide called the Navigator. That practice corresponds to **F06_03 Prospective** (Foresight), the Vision facet for exploring possible futures. The ten domains are what the practice looks at. They do not replace the 38 facets.

The publication draft [Future Observatory Framework](../../03_BOOK_AND_PUBLICATION/14_FUTURE_OBSERVATORY_FRAMEWORK.md) describes an institutional monitoring observatory mapped onto the seven foundations. FiF's Observatory is a conversation screen. The shared word is historical flavor, not an identity merge.

## Scales

ELYSIUM scales are Human, Society, and Civilization. FiF writes three implication lenses on every domain:

| FiF lens | ELYSIUM reading |
|---|---|
| Individual | Human |
| Society | Society |
| Economy | Agency (F03), at Society and Civilization scales. Not a fourth scale. |

## Categories and foundations

| FiF category | ELYSIUM foundation | Relation |
|---|---|---|
| cognitive | F06 Vision | partial_overlap |
| physical | F01 Foundation | partial_overlap |
| life | F02 Vitality | partial_overlap |
| systems | F05 Governance and F03 Agency | split |
| perception | — none single — | no_single_foundation |
| meaning | F07 Consciousness | partial_overlap |

- **cognitive.** Intelligence and coordination of knowing. Vision also holds education, science, foresight, systems thinking, and technology, which this category does not enumerate.
- **physical.** Energy and materials sit in Foundation. Robotics is filed here by FiF and also overlaps Agency (work, production) and Vision (technology).
- **life.** Biotechnology touches health and food. FiF does not carry water, biodiversity, ecosystems, or regeneration as domains.
- **systems.** Institutions overlap Governance. Programmable finance overlaps Agency / Finance. One FiF category covers two foundations.
- **perception.** Spatial computing spreads across technology (F06), media (F04), and communication (F05).
- **meaning.** Identity and purpose sit in Consciousness. Ethics and civilizational direction are sibling facets, not this one domain.

## Thesis

> Humanity is moving from a scarcity-driven, labor-based civilization to an intelligence-abundant, meaning-driven one.

Read as a source claim about civilizational direction (`F07_05_DIRECTION_CIVILISATIONNELLE`) and about work (`F03_02_TRAVAIL`). It is FiF's thesis.

## Domain to facet

| # | FiF domain | Primary facet | Related facets |
|---|---|---|---|
| 1 | Artificial General Intelligence | `F06_05_TECHNOLOGIE` | `F06_01_EDUCATION`, `F03_02_TRAVAIL`, `F06_04_PENSEE_SYSTEMIQUE` |
| 2 | Energy Revolution | `F01_01_ENERGIE` | `F03_06_PRODUCTION` |
| 3 | Biotechnology & Synthetic Life | `F02_01_SANTE` | `F02_02_ALIMENTATION_AGRICULTURE`, `F07_01_ETHIQUE` |
| 4 | Robotics & Automation | `F03_06_PRODUCTION` | `F03_02_TRAVAIL`, `F06_05_TECHNOLOGIE` |
| 5 | Collective Intelligence | `F06_04_PENSEE_SYSTEMIQUE` | `F04_01_COMMUNAUTE`, `F05_05_COMMUNICATION` |
| 6 | Digital Money & Programmable Finance | `F03_03_FINANCE` | `F03_01_ECONOMIE` |
| 7 | Institutional Collapse & Rebuild | `F05_03_INSTITUTIONS` | `F05_02_DEMOCRATIE`, `F07_05_DIRECTION_CIVILISATIONNELLE` |
| 8 | Spatial Computing | `F06_05_TECHNOLOGIE` | `F04_05_MEDIAS`, `F05_05_COMMUNICATION` |
| 9 | Materials Science | `F01_06_MATERIAUX` | `F03_06_PRODUCTION` |
| 10 | Human Identity & Meaning | `F07_03_SENS_FINALITE` | `F04_06_APPARTENANCE_IDENTITE`, `F07_04_VISION_DU_MONDE`, `F07_02_SPIRITUALITE` |

- **Artificial General Intelligence.** The technology facet already treats artificial intelligence as civilizational exoskeleton. FiF's 'who thinks' claim also touches education, knowledge work, and systems thinking.
- **Energy Revolution.** Direct name overlap with Foundation / Energy. The abundance claim also feeds production.
- **Biotechnology & Synthetic Life.** Healthspan, disease, and genetic intervention land in Health. The schema names a food revolution and ethical frontiers, which point at Food & Agriculture and Ethics. Ecological regeneration is a different facet and is not this domain.
- **Robotics & Automation.** FiF frames machines that act: manufacturing and labor first, technology as the means.
- **Collective Intelligence.** Networked sense-making is systems thinking at collective scale, with community and communication as the social channels.
- **Digital Money & Programmable Finance.** Programmable money is the Finance facet, inside the Economy.
- **Institutional Collapse & Rebuild.** Trust, legitimacy, and governance models are Institutions, with democracy and civilizational direction as the neighboring questions the schema raises.
- **Spatial Computing.** A perception technology. Media and communication carry the social side of a blended interface. It shares its primary facet with AGI and is distinguished by the 'how we perceive' claim.
- **Materials Science.** Direct name overlap with Foundation / Materials, with production as the making system.
- **Human Identity & Meaning.** FiF's 'why we exist' claim is Meaning & Purpose. Identity, worldview, and spirituality are the adjacent Consciousness and Cohesion facets named by the schema's cultural and identity implications.

AGI and spatial computing share `F06_05_TECHNOLOGIE` as primary facet. FiF separates them by the claims "who thinks" and "how we perceive".

## Exploration modes and the twelve matrix steps

A finding aid. FiF modes are guide prompts. The twelve steps are the ELYSIUM analysis worksheet.

| FiF mode | Matrix steps |
|---|---|
| `essential_insight` | 1, 2 — What Is It? (Ontology); Why It Matters (Teleology) |
| `deep_dive` | 3, 4, 5, 6 — Today's Paradigm (Status Quo); Current Crisis / Limitations; Key Transitions Underway; Technology / AI Disruption |
| `systems_weave` | 5 — Key Transitions Underway |
| `strategic_questions` | 7, 8 — Consciousness / Cultural Shift; The Future Paradigm |
| `action_gateway` | 9, 10, 11, 12 — Transition Pathways; Projects / Experiments; Risks / Shadows; Resources (The Library) |

Systems weave is also the habit of reading across facets, which is the ongoing role of `F06_04_PENSEE_SYSTEMIQUE`.

## Facets with no FiF domain

These canonical facets have no counterpart among the ten domains: `F01_02_EAU`, `F01_03_HABITAT`, `F01_04_INFRASTRUCTURE`, `F01_05_MOBILITE`, `F02_03_BIODIVERSITE`, `F02_04_ECOSYSTEMES`, `F02_05_REGENERATION`, `F03_04_ENTREPRENEURIAT`, `F03_05_INNOVATION`, `F04_02_RELATIONS`, `F04_03_CULTURE`, `F04_04_ART`, `F05_01_DROIT_JUSTICE`, `F05_04_SECURITE`, `F06_02_SCIENCE`.

Education, ethics, spirituality, democracy, community, media, identity, communication, worldview, civilizational direction, economy, and work appear only as related facets, where a domain's implication text touches them.

