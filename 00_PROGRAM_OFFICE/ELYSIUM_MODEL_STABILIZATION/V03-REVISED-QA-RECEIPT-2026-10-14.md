# ELYSIUM — QA de la couche v0.3-revised

**Date :** 2026-10-14
**Statut :** `DERIVED_DRAFT_EDITORIAL_REVISED_QA_PENDING`
**Mode :** contrôle addition-only avant fusion
**Autorisation :** Founder Gate des six reformulations

## Résultats mécaniques

| Contrôle | Mobilité | Biodiversité | Écosystèmes |
|---|---:|---:|---:|
| Hash parent immédiat v0.3-cited concordant | PASS | PASS | PASS |
| Étapes uniques 1–12 | PASS | PASS | PASS |
| Références utilisées toutes définies | PASS | PASS | PASS |
| Sources/parents existants écrasés | NON | NON | NON |
| Promotion `CANONICAL` | NON | NON | NON |

## Diff autorisé

- `RF-MOB-001` : reformulation précise du ratio UNECE et suppression du doublon textuel « environ environ ».
- `RF-BIO-001` : formulation IPBES déjà présente dans le parent, conservée et versionnée.
- `RF-BIO-002` : précision WWF déjà présente dans le parent, conservée et versionnée.
- `RF-BIO-003` : qualification de l’exemple constitutionnel équatorien et interdiction de généralisation mondiale.
- `RF-ECO-001` : formulation Aichi déjà présente dans le parent, conservée et versionnée.
- `RF-ECO-002` : formulation FMI déjà présente dans le parent, conservée et versionnée.

Les quatre reformulations déjà présentes dans `v0.3-cited` ne sont pas comptées comme de nouvelles modifications : elles sont héritées explicitement et leur présence est documentée dans le manifeste.

## Claims non touchés

Les claims suivants demeurent bloqués comme prévu :

- pertes économiques en points de PIB mondial ;
- zoonoses ;
- Natural Capital Protocol ;
- qualification « sixième extinction ».

## Verdict

```text
V03_REVISED_PARENT_CHAIN = PASS
V03_REVISED_STRUCTURE    = PASS (3/3 × 12/12)
V03_REVISED_REFERENCES   = PASS
AUTHORIZED_DIFF_SCOPE    = PASS
SOURCE_PRESERVATION      = PASS
CANONICAL_PROMOTION      = NOT_EXECUTED
SEMANTIC_FINALITY        = PENDING
```

La couche est fusionnable comme **dérivé révisé QA-pending**, pas comme corpus canonique.
