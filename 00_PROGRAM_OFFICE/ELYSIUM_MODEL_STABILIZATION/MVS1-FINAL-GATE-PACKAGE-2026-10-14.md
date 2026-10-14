# ELYSIUM — Paquet final de décision MVS‑1

**Date :** 2026-10-14
**Statut :** `MVS1_NEAR_PASS / MVS05_FINAL_GATE_REQUIRED`
**Mode :** proposition addition-only ; aucune modification source

## État des critères

| Critère | État consolidé | Preuve |
|---|---|---|
| `MVS-01` — échelles A/B | `QUALIFIED` | Founder Gate STAB-SEM-001 + ETF |
| `MVS-02` — fondations A/B | `QUALIFIED` | IDs/labels et séparation des définitions |
| `MVS-03` — facettes et portée B | `QUALIFIED_WITH_BOUNDARY` | 38 IDs A ; `B_FACETS_UNENUMERATED` |
| `MVS-04` — inventaire | `QUALIFIED_BY_RECEIPT` | 38 chemins physiques ; index historique 36/38 conservé et expliqué |
| `MVS-05` — matrice 12 étapes | `FINAL_GATE_REQUIRED` | 3 sources directes incomplètes ; dérivés v0.3-revised 12/12 QA-pending |
| `MVS-06` — DOC_06 | `QUALIFIED_QA_PENDING` | `INTEGRATED_DRAFT / QA_PENDING` confirmé |
| `MVS-07` — ETF | `RECONFIRMED` | hash distant `e1dbfa5e…0672023e`, statut relational-only |

## Blocage unique

Les trois matrices sources directes concernées sont :

- `F01_05_MOBILITE` ;
- `F02_03_BIODIVERSITE` ;
- `F02_04_ECOSYSTEMES`.

Leur structure source directe n’est pas 12/12. Les dérivés sont séparés, traçables et QA mécaniquement réussis, mais leur usage comme **baseline analytique de P02** n’a pas encore été explicitement autorisé.

## Décision Founder requise

### Option recommandée — `MVS-05 QUALIFIED_WITH_DERIVED_WORKING_BASELINE`

Autoriser le brief P02 diagnostique à utiliser la couche `v0.3-revised` comme **baseline de travail dérivée**, avec les contraintes suivantes :

1. les sources directes restent souveraines et inchangées ;
2. les dérivés restent explicitement `DERIVED_DRAFT_EDITORIAL_REVISED_QA_PENDING` ;
3. chaque usage P02 conserve le lien vers la source directe et le hash du dérivé ;
4. aucune affirmation ne peut être présentée comme canonique ;
5. les réserves et les quatre claims source-blocked restent visibles ;
6. le brief P02 est diagnostique et non prescriptif ;
7. aucune équivalence A/B n’est introduite.

### Option conservatrice

Maintenir `MVS-05` en `PENDING` jusqu’à une décision ultérieure de remplacement/versionnement des trois sources directes. Dans ce cas, P02 reste préparatoire mais non publiable comme brief diagnostique stabilisé.

## Effet de l’option recommandée

```text
MVS-1 = PASS_WITH_DERIVED_WORKING_BASELINE
        (not canonical; not source replacement)
```

Ce statut signifie que le modèle est suffisamment stable pour cadrer et diagnostiquer le brief P02, pas que les contenus des matrices sont définitivement validés.

## Interdictions maintenues

- aucune réécriture des trois sources directes ;
- aucune suppression de l’historique 36/38 ;
- aucune promotion `CANONICAL` ;
- aucune rédaction prescriptive avant revue P02 ;
- aucune fusion réductrice des taxonomies.
