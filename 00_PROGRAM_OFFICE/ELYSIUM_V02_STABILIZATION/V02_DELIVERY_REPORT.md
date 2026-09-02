# ELYSIUM — Livraison des trois matrices dérivées v0.2

**Date de contrôle :** 2026-09-02  
**Statut global :** `DERIVED_DRAFT_QA_PENDING`  
**Mode :** production locale de proposition ; aucun dépôt canonique modifié.

## Résultat

Les trois matrices dérivées v0.2 ont été produites à partir des fragments originaux actuellement présents. Les originaux sont conservés séparément et leur hash parent est inscrit dans chaque dérivé.

| Facette | Original | Dérivé | Étapes du dérivé | Contrôle |
|---|---|---|---:|---|
| `F01_05_MOBILITE` | 1–4 | `F01_05_MOBILITE_v0.2.md` | 12/12 | PASS |
| `F02_03_BIODIVERSITE` | 1–5 | `F02_03_BIODIVERSITE_v0.2.md` | 12/12 | PASS |
| `F02_04_ECOSYSTEMES` | 1–4 | `F02_04_ECOSYSTEMES_v0.2.md` | 12/12 | PASS |

## Garanties contrôlées

Le contrôle déterministe confirme pour les trois fichiers : présence du dérivé, hash parent correct, statut `DERIVED_DRAFT_QA_PENDING`, déclaration `NO_RECOVERY_EVIDENCE_IN_GIT_PORTFOLIO`, douze étapes uniques numérotées de 1 à 12 et invariance du hash de l’original.

Les sections héritées proviennent des fragments actuels. Les sections nouvellement ajoutées sont des **complétions dérivées**, non des verbatims récupérés. Les références externes, données chiffrées et affirmations nécessitant une validation documentaire ne sont pas réputées validées par cette livraison.

## Gate de promotion

**MVS-1 n’est pas franchi par cette livraison.** La complétude mécanique des trois fichiers dérivés est établie, mais leur contenu doit encore passer une revue sémantique, une revue factuelle et une validation d’alignement avec les deux taxonomies coexistantes.

Aucune modification des index canoniques, aucune substitution des originaux et aucune promotion `CANONICAL` ne doit être effectuée avant ces revues. La prochaine PR éventuelle devra être addition-only et ajouter les trois dérivés dans un espace explicitement marqué `derived`, ou suivre une convention de version approuvée.

## Prochaines décisions

| ID | Décision | Responsable |
|---|---|---|
| `V02-DEC-001` | Valider ou réviser les complétions conceptuelles des trois facettes. | Yannick / revue sémantique |
| `V02-DEC-002` | Ajouter les sources externes nécessaires aux passages factuels. | Recherche documentaire |
| `V02-DEC-003` | Décider l’emplacement Git des dérivés v0.2 et leur statut de publication. | Founder Gate |
| `V02-DEC-004` | Après revue, corriger les index sans écraser leur historique. | Mainteneur Git |

## Références internes

[1]: https://github.com/yj000018/elysium-civilizational-ontology/tree/main/02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES "ELYSIUM Facet Matrices"
[2]: https://github.com/yj000018/elysium-civilizational-ontology/blob/main/02_ONTOLOGY_AND_KNOWLEDGE/CANONICAL_FACET_ID_MAP.md "Canonical Facet ID Map"
