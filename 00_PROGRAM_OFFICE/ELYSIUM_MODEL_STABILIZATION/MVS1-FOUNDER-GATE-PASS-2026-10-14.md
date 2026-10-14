# ELYSIUM — MVS‑1 Founder Gate PASS

**Date :** 2026-10-14
**Décideur :** Yannick
**Décision :** autoriser la baseline de travail dérivée `v0.3-revised`
**Statut accordé :** `PASS_WITH_DERIVED_WORKING_BASELINE`

## Portée

Le modèle ELYSIUM est suffisamment stabilisé pour préparer un brief P02 **diagnostique et sourcé** à partir de la couche dérivée `v0.3-revised`.

Ce passage ne signifie pas :

- que les trois sources directes sont structurellement complètes ;
- que les matrices dérivées sont canoniques ;
- que les contenus sont définitivement validés ;
- que les taxonomies A et B sont fusionnées ;
- que le brief P02 peut être prescriptif sans revue séparée.

## Critères MVS‑1

| Critère | Verdict final | Réserve |
|---|---|---|
| `MVS-01` | `QUALIFIED` | Labels A provisoires ; portée B distincte. |
| `MVS-02` | `QUALIFIED` | IDs/labels A de référence ; définitions non fusionnées. |
| `MVS-03` | `QUALIFIED_WITH_BOUNDARY` | 38 IDs A ; `B_FACETS_UNENUMERATED`. |
| `MVS-04` | `QUALIFIED_BY_RECEIPT` | 38 chemins physiques ; index historique 36/38 conservé. |
| `MVS-05` | `PASS_WITH_DERIVED_WORKING_BASELINE` | `v0.3-revised` utilisable pour P02, non canonique. |
| `MVS-06` | `QUALIFIED_QA_PENDING` | DOC_06 reste `INTEGRATED_DRAFT / QA_PENDING`. |
| `MVS-07` | `RECONFIRMED` | ETF hash et frontière relationnelle vérifiés. |

## Contraintes obligatoires pour P02

1. Chaque matrice utilisée doit pointer vers sa source directe et ses hashes.
2. Le statut `DERIVED_DRAFT_EDITORIAL_REVISED_QA_PENDING` doit rester visible.
3. Les quatre claims bloqués restent explicitement marqués : PIB, zoonoses, Natural Capital Protocol, « sixième extinction ».
4. Les relations ETF sont des correspondances proposées, jamais des synonymies.
5. Le brief P02 est diagnostique : il décrit, qualifie, compare et expose les réserves.
6. Toute prescription, canonisation ou décision de remplacement est exclue de ce gate.
7. Les matrices sources et les dérivés précédents restent inchangés.

## Verdict

```text
MVS-1 = PASS_WITH_DERIVED_WORKING_BASELINE
P02 diagnostic preparation = AUTHORIZED
P02 prescriptive publication = NOT_AUTHORIZED
CANONICAL promotion         = NOT_AUTHORIZED
SOURCE replacement          = NOT_AUTHORIZED
TAXONOMY fusion             = NOT_AUTHORIZED
```
