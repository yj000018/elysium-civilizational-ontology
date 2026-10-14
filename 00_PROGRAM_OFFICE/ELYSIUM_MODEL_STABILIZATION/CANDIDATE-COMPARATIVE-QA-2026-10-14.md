# ELYSIUM — QA comparative des trois candidats de restauration

**Date :** 2026-10-14  
**Mode :** analyse addition-only ; aucune modification de source  
**Sources comparées :** `main` distant de `elysium-civilizational-ontology` vs dérivés locaux v0.2  
**Décision Founder préalable :** `A/A/A`

## Méthode

Contrôles exécutés :

1. hash SHA-256 de la source distante ;
2. lecture de `derived_from_sha256` dans le candidat ;
3. égalité du hash parent déclaré et du hash source ;
4. détection des étapes par en-têtes ;
5. comparaison normalisée du contenu de chaque étape existante ;
6. séparation stricte entre contenu source conservé et sections dérivées ajoutées.

Cette QA ne juge pas la vérité empirique de chaque claim. La QA de citations et l’arbitrage sémantique restent des couches distinctes.

## Résultats

| Facette | Source | Candidat | Hash parent | Étapes source | Étapes candidat | Étapes source conservées exactement | Verdict |
|---|---|---|---|---:|---:|---|---|
| `F01_05_MOBILITE` | `c0055fb4…4982b7d2` | `ece50663…571bd96f5` | Oui | 1–4 | 1–12 | 1–4 | `CANDIDATE_PASS` |
| `F02_03_BIODIVERSITE` | `98f550e2…f5c8cc6f` | `d100eb72…44a1f92` | Oui | 1–5 | 1–12 | 1–5 | `CANDIDATE_PASS` |
| `F02_04_ECOSYSTEMES` | `db742765…6817501b` | `e72102af…ffadeedb` | Oui | 1–4 | 1–12 | 1–4 | `CANDIDATE_PASS` |

## Résultat détaillé

### `F01_05_MOBILITE`

- La source distante contient les étapes 1–4.
- Le candidat contient les étapes 1–12.
- Les étapes 1–4 sont conservées exactement après normalisation des niveaux de titre et des espaces.
- Les étapes 5–12 sont des ajouts dérivés.
- L’assertion sur plusieurs points de PIB mondial reste soumise à `REV-MOB-001` et ne doit pas être publiée comme claim mondial non qualifié.

**Verdict :** candidat structurellement recevable ; `QA_CITATION_PENDING`.

### `F02_03_BIODIVERSITE`

- La source distante contient les étapes 1–5.
- Le candidat contient les étapes 1–12.
- Les étapes 1–5 sont conservées exactement après normalisation.
- Les étapes 6–12 sont des ajouts dérivés.
- Les formulations sur zoonoses, Natural Capital Protocol et sixième extinction restent encadrées par les décisions `REV-BIO-001`, `REV-BIO-002` et `REV-ECO-003`.

**Verdict :** candidat structurellement recevable ; `QA_CITATION_PENDING`.

### `F02_04_ECOSYSTEMES`

- La source distante contient les étapes 1–4.
- Le candidat contient les étapes 1–12.
- Les étapes 1–4 sont conservées exactement après normalisation.
- Les étapes 5–12 sont des ajouts dérivés.
- Les formulations sur limites planétaires, subventions fossiles et sixième extinction restent soumises à la qualification `REV-ECO-001` et `REV-ECO-003`.

**Verdict :** candidat structurellement recevable ; `QA_CITATION_PENDING`.

## Conclusion de la QA

Les trois candidats satisfont les invariants suivants :

- parent identifié par hash ;
- parent retrouvé dans `main` ;
- contenu parent conservé ;
- couverture 12 étapes ;
- additions séparables du parent ;
- statut dérivé explicitement non canonique.

Ils peuvent donc être classés :

```text
CANDIDATE_RESTORATION = STRUCTURE_PASS
CANONICAL_PROMOTION   = NOT_AUTHORIZED
SOURCE_REPLACEMENT    = NOT_EXECUTED
CITATION_QA           = PENDING
```

## Effet sur MVS‑05

Le critère peut désormais être qualifié comme suit :

> **L’instrument 12 étapes est implémenté dans trois candidats dérivés dont la provenance parentale et la conservation du contenu source sont démontrées. Les sources récupérées restent structurellement courtes ; elles ne sont pas remplacées.**

Statut recommandé :

```text
MVS-05 = CANDIDATE_STRUCTURE_PASS
         / SOURCE_BASELINE_SHORT_RETAINED
         / CITATION_QA_PENDING
```

Cela réduit le blocage MVS‑1, mais ne constitue pas automatiquement un `MVS-1 PASS` tant que le registre canonique ne référence pas explicitement les candidats et que la QA de citations n’est pas classée.

## Prochaine action recommandée

Préparer une seconde PR addition-only, séparée de toute modification source, qui :

1. ajoute ce rapport de QA comparative au registre programme ;
2. référence les trois candidats par hash ;
3. distingue `source baseline short` et `derived candidate 12-step` ;
4. conserve `QA_CITATION_PENDING` ;
5. ne modifie aucune matrice ni aucun index historique.

**Statut :** `COMPARATIVE_QA_PASS — CANDIDATES_NOT_CANONICAL`.
