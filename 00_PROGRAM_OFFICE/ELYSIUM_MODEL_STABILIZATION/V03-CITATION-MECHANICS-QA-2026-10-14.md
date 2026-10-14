# ELYSIUM — QA mécanique des dérivés v0.3-cited

**Date :** 2026-10-14  
**Mode :** addition-only ; aucune promotion canonique  
**Périmètre :** `F01_05_MOBILITE`, `F02_03_BIODIVERSITE`, `F02_04_ECOSYSTEMES`

## Contrôles

Pour chaque matrice :

1. hash SHA-256 du parent v0.2 ;
2. hash `Parent SHA-256` déclaré dans le v0.3 ;
3. couverture des 12 étapes ;
4. résolution de toutes les références utilisées ;
5. présence d’une définition URL pour chaque référence ;
6. identification des étapes reformulées entre v0.2 et v0.3.

## Résultats

| Facette | Parent v0.2 | v0.3-cited | Hash parent cohérent | Étapes | Références utilisées = définies | Étapes reformulées | Verdict mécanique |
|---|---|---|---|---:|---|---|---|
| `F01_05_MOBILITE` | `ece50663…571bd96f5` | `a7a20cec…de1687b` | Oui | 1–12 | `[4] = [4]` | 4, 12 | `PASS` |
| `F02_03_BIODIVERSITE` | `d100eb72…44a1f92` | `813a2239…e6df43e` | Oui | 1–12 | `[1,2,3,8] = [1,2,3,8]` | 4, 5, 12 | `PASS` |
| `F02_04_ECOSYSTEMES` | `e72102af…ffadeedb` | `a3e21799…482fb2e8` | Oui | 1–12 | `[6,9,10] = [6,9,10]` | 4, 12 | `PASS` |

## Interprétation

### Provenance

Les trois fichiers v0.3-cited pointent correctement vers le hash du parent v0.2 correspondant. La chaîne de dérivation est donc traçable :

```text
source récupérée
  → v0.2 structural completion draft
    → v0.3 citation-aware derived draft
```

### Structure

Les trois dérivés v0.3 contiennent les 12 étapes attendues.

### Citations

Toutes les références appelées dans le corps des matrices disposent d’une définition URL dans leur propre section `References`. Aucun identifiant de citation orphelin n’a été détecté.

### Reformulations

Les étapes reformulées sont concentrées sur les passages ayant reçu une qualification ou une citation. Elles ne doivent donc pas être considérées comme du texte source récupéré. Elles constituent une couche dérivée éditoriale et probatoire.

## Verdict

```text
V03_CITATION_MECHANICS = PASS
V03_PROVENANCE          = PASS
V03_STRUCTURE           = PASS
V03_SEMANTIC_REVIEW    = PENDING
V03_CANONICAL_PROMOTION = NOT_AUTHORIZED
```

Le statut reste :

```text
DERIVED_DRAFT_CITATION_QA_PENDING
```

La QA mécanique ne valide pas encore :

- la suffisance des sources pour chaque claim ;
- la portée exacte des chiffres et dates ;
- les claims `REVIEW` déjà enregistrés ;
- la valeur canonique des reformulations ;
- le remplacement des matrices sources.

## Effet sur MVS‑1

MVS‑05 peut être décrit comme :

```text
12-step candidate structure       = PASS
parental provenance               = PASS
citation reference integrity      = PASS
semantic/citation sufficiency     = PENDING
source baseline replacement       = NOT_EXECUTED
```

**Conclusion :** la couche dérivée v0.3 est techniquement propre et traçable, mais elle reste une proposition éditoriale dérivée. Aucun passage automatique à `CANONICAL` n’est autorisé.
