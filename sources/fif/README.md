# FiF – Futures in Focus

Source material from Yannick's Replit app **FiF – Futures in Focus** (styled F·U·T·U·R·E·S in Focus). The in-app credit line is "Developed by Ynot (YJ). 2026." `replit.md` calls the export version 0.9, a release candidate.

This folder holds the intellectual content of that app: ten future-of-civilisation transformations, the prompts used to explore them, and a reading of how those domains sit on the ELYSIUM ontology. The React app, server, database, and Replit integrations are not reconstructed here.

Acceptance status: **source material**. A file in this folder does not become accepted canon, and it is not part of the existing `SHA256SUMS.txt` inventory.

## What the app was

FiF is a personal futures-literacy practice. Its specification states the thesis in one line: humanity is moving from a scarcity-driven, labor-based civilization to an intelligence-abundant, meaning-driven one.

The app offered six spaces. The Observatory talked with a guide called the Navigator. The Archive held the ten domains. The Lab ran multi-day journeys. The Think Tank was for scenarios. The Journal stored insights. The Profile tracked expertise. Those spaces explain where the texts below lived. They are context, not a product to run from this repository.

The sanitized archive was already image-stripped. Its `.replit` file contains the placeholder `OPENAI_API_KEY = "REDACTED"`. No secret values were copied. Receipt, file hashes, and the list of omitted runtime files are in [data/SOURCE-MANIFEST.json](data/SOURCE-MANIFEST.json).

## What was imported

| Material | Structured data | Reading copy |
|---|---|---|
| 10 domains, 6 categories, EN/FR/IT labels, implication lenses | [data/domains.json](data/domains.json) | [DOMAINS.md](DOMAINS.md) |
| Navigator prompts, exploration-mode prompts, 31 daily reflections, 32 signals, journey-day prompt | [data/prompts.json](data/prompts.json) | [PROMPTS.md](PROMPTS.md) |
| Facet crosswalk | [data/ontology-crosswalk.json](data/ontology-crosswalk.json) | [ONTOLOGY-CROSSWALK.md](ONTOLOGY-CROSSWALK.md) |

Two prompt generations are both preserved. `FUTURES_SPEC.md` writes a futures Navigator and five exploration modes (deep dive, systems weave, essential insight, strategic questions, action gateway). `server/routes.ts` runs a Navigator opening with that same domain list, then still appends instructions from the earlier spiritual WIP app (seeker, traditions, retreat days). The Archive starts a domain exploration without the theme id the server requires before it injects a mode prompt, so the five futures mode texts are specification, and the live mode prompts still belong to the older theme library. That split is recorded in [PROMPTS.md](PROMPTS.md) rather than smoothed over.

English names in the data follow `shared/schema.ts`. The UI dictionary shortens two of them: "Digital Money & Programmable Finance" appears as "Digital Money & Finance", and "Institutional Collapse & Rebuild" appears as "Institutional Evolution". French and Italian use shorter labels. Subtitles exist in English only. Perception and Meaning category colors are swapped in `Archive.tsx` relative to the specification and to each domain's accent.

Signal attributions are the strings the app stored.

## How it maps onto the ELYSIUM ontology

The full table is [ONTOLOGY-CROSSWALK.md](ONTOLOGY-CROSSWALK.md). The short version:

The **practice** — a guide, scenarios, signals, and reflection prompts for possible futures — corresponds to **F06_03 Prospective** (Foresight), inside Foundation F06 Vision. The ten domains are the objects of that practice. They do not replace the 38 facets.

ELYSIUM scales are Human, Society, and Civilization. FiF writes three lenses on every domain. Individual reads as Human. Society reads as Society. Economy reads as Agency (F03) at Society and Civilization scales, not as a fourth scale.

FiF categories overlap foundations only in part. Cognitive sits near Vision, physical near Foundation, life near Vitality, meaning near Consciousness. Systems splits across Governance and Agency. Perception has no single foundation.

| # | FiF domain | Primary ELYSIUM facet |
|---|---|---|
| 1 | Artificial General Intelligence | `F06_05_TECHNOLOGIE` |
| 2 | Energy Revolution | `F01_01_ENERGIE` |
| 3 | Biotechnology & Synthetic Life | `F02_01_SANTE` |
| 4 | Robotics & Automation | `F03_06_PRODUCTION` |
| 5 | Collective Intelligence | `F06_04_PENSEE_SYSTEMIQUE` |
| 6 | Digital Money & Programmable Finance | `F03_03_FINANCE` |
| 7 | Institutional Collapse & Rebuild | `F05_03_INSTITUTIONS` |
| 8 | Spatial Computing | `F06_05_TECHNOLOGIE` |
| 9 | Materials Science | `F01_06_MATERIAUX` |
| 10 | Human Identity & Meaning | `F07_03_SENS_FINALITE` |

AGI and spatial computing share the technology facet and are separated by FiF's own claims: "who thinks" and "how we perceive". Related facets, the twelve-step matrix reading of the exploration modes, and the facets with no FiF domain are in the crosswalk. Facet identifiers follow [CANONICAL_FACET_ID_MAP.md](../../02_ONTOLOGY_AND_KNOWLEDGE/CANONICAL_FACET_ID_MAP.md). Foundation names follow [ELYSIUM_CORE_ONTOLOGY.json](../../04_DATASETS_AND_MATRICES/ELYSIUM_CORE_ONTOLOGY.json).

The publication draft [Future Observatory Framework](../../03_BOOK_AND_PUBLICATION/14_FUTURE_OBSERVATORY_FRAMEWORK.md) describes an institutional monitoring observatory. FiF's Observatory is a conversation screen in a personal app. The shared word is not an identity merge.
