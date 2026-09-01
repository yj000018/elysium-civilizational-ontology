# ELYSIUM Taxonomy Federation

**Status:** Active relational layer — v0.1
**Scope:** ELYSIUM only
**Rule:** This directory contains **relations and provenance**, never replacement copies of ELYSIUM source taxonomies.

## Purpose

ELYSIUM contains two valid ontological taxonomies. They are preserved as autonomous source models and connected through explicit, versioned, and reviewable relationships. The Federation makes their correspondence, divergence, scope boundaries, and authority domains navigable without turning either source into a subordinate or a duplicate.

> The Federation is **not** a third taxonomy. It is a governed map between taxonomies.

## Source models

| ID | Source | Role | Source status |
|---|---|---|---|
| `ELY-TAX-A-METABOLIC` | [`elysium-book@master:00-meta/ontology-map.md`](https://github.com/yj000018/elysium-book/blob/master/00-meta/ontology-map.md) | Civilizational metabolic and regenerative model | Provisional; Founder confirmation remains pending. |
| `ELY-TAX-B-OPEN-INFRASTRUCTURE` | [`elysium-civilizational-ontology@main:03_BOOK_AND_PUBLICATION/06_ONTOLOGY_SPECIFICATION.md`](../../03_BOOK_AND_PUBLICATION/06_ONTOLOGY_SPECIFICATION.md) | Open civilizational infrastructure model | `DRAFT_INTEGRATED_QA_PENDING`. |

## Contents

| File | Function | Authority |
|---|---|---|
| [`FEDERATION-CHARTER.md`](FEDERATION-CHARTER.md) | Non-loss, non-equivalence and governance rules. | Yannick |
| [`TAXONOMY-REGISTRY.yaml`](TAXONOMY-REGISTRY.yaml) | Source identities, anchors and structural nodes. | Relational record |
| [`RELATION-REGISTRY.yaml`](RELATION-REGISTRY.yaml) | Approved and deferred relations between source nodes. | Yannick-approved relations |
| [`DECISION-LOG.md`](DECISION-LOG.md) | Append-only human decisions. | Yannick |
| [`PROVENANCE-LEDGER.jsonl`](PROVENANCE-LEDGER.jsonl) | Append-only observation and derivation receipts. | Evidence log |

## Safety boundary

No file in this directory may change, duplicate as a replacement, or silently supersede a source document. A future source change requires a new observation receipt and a targeted review of only the affected relations. Any source mutation requires a separate, explicitly approved pull request.

## First implementation state

The initial release registers two models and eleven approved primary relationships. Six secondary relationships are intentionally deferred. In particular, **Consciousness** remains a distinct transverse dimension in the metabolic model and **Environment** remains an autonomous foundation in the open-infrastructure model.
