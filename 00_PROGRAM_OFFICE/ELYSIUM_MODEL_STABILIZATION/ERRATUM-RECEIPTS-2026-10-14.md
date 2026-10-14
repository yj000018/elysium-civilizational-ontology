# ELYSIUM — Erratum des reçus du 14 octobre 2026

**Date :** 2026-10-14

**Base revérifiée :** `main` à `e14269e1c4fe9eba992cb652f21694a3116a9253`

**Portée :** rectification documentaire ; reçus historiques conservés à l’identique. Les matrices, sources créatives, manifestes, empreintes et décisions éditoriales ne sont pas modifiés.

## Reçus concernés et continuité

Lire les trois reçus avec les rectifications ci-dessous :

1. [Réconciliation technique MVS-1 — PR 5](MVS1-TECHNICAL-RECONCILIATION-2026-10-14.md) : présence physique et état des sources ; le candidat v0.2 mentionné possède déjà un enfant v0.3, qui doit être inclus dans la lecture du gate.
2. [QA comparative des candidats v0.2 — PR 6](CANDIDATE-COMPARATIVE-QA-2026-10-14.md) : comparaison structurelle source → v0.2 ; les références `REV-*` et la décision Founder citée sont qualifiées ci-dessous.
3. [QA mécanique v0.3 — PR 7](V03-CITATION-MECHANICS-QA-2026-10-14.md) : continuité v0.2 → v0.3 ; rectification des ensembles de références et des étapes modifiées.

Les PR 5, 6 et 7 sont fusionnées. Leurs six observations de revue `COMMENTED` étaient non résolues à la revérification ; cet erratum n’en change pas l’état GitHub.

Les 38 matrices `Fnn_nn_*.md` sont présentes dans [FACET_MATRICES](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES). La déclaration historique `present=36` et les deux absences indiquées dans l’index sont une dérive d’index, pas une absence physique actuelle. Aucune perte n’est constatée dans ce périmètre vérifié.

## Chaîne de dérivation conservée

Source récupérée → candidat structurel v0.2 → enfant v0.3-cited. Les trois liens de parenté sont confirmés par `derived_from_sha256`, le pied de statut v0.3 et le [manifeste de dérivation](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES_DERIVED_V03/DERIVATION-MANIFEST.json).

| Facette | Source récupérée | Parent v0.2 | Enfant v0.3-cited |
|---|---|---|---|
| Mobilité | [source](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES/F01_05_MOBILITE.md) | [v0.2](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES_DERIVED_V02/F01_05_MOBILITE_v0.2.md) | [v0.3](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES_DERIVED_V03/F01_05_MOBILITE_v0.3-cited.md) |
| Biodiversité | [source](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES/F02_03_BIODIVERSITE.md) | [v0.2](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES_DERIVED_V02/F02_03_BIODIVERSITE_v0.2.md) | [v0.3](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES_DERIVED_V03/F02_03_BIODIVERSITE_v0.3-cited.md) |
| Écosystèmes | [source](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES/F02_04_ECOSYSTEMES.md) | [v0.2](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES_DERIVED_V02/F02_04_ECOSYSTEMES_v0.2.md) | [v0.3](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES_DERIVED_V03/F02_04_ECOSYSTEMES_v0.3-cited.md) |

Les six dérivés ont chacun les étapes 1–12. Les sources récupérées restent courtes : Mobilité 1–4, Biodiversité 1–5, Écosystèmes 1–4. En particulier, l’indication source Écosystèmes `matrix_status: 12-step complete` reste en contradiction avec ses seuls en-têtes 1–4 ; cette revue de structure reste ouverte.

Les SHA-256 des six dérivés concordent avec les entrées correspondantes des [preuves v0.2](../ELYSIUM_V02_STABILIZATION/V02_EVIDENCE.sha256) et des [preuves v0.3](../../02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES_DERIVED_V03/V03-EVIDENCE.sha256). Le manifeste v0.3 et le [registre de citations](../ELYSIUM_V02_STABILIZATION/CITATION-PATCH-001.md) concordent aussi avec leurs reçus. Cela établit une provenance mécanique, sans acceptation sémantique.

## Rectifications du reçu v0.3

| Facette | Références utilisées dans le corps | Définitions URL | Étapes effectivement modifiées de v0.2 à v0.3 |
|---|---|---|---|
| Mobilité | `{4}` | `{4}` | 4 |
| Biodiversité | `{1,2,3,8}` | `{1,2,3,8}` | 4 et 5 |
| Écosystèmes | `{6,10}` | `{6,9,10}` | 4 |

Pour Écosystèmes, l’égalité annoncée dans le reçu historique est fausse : la propriété vérifiée est l’inclusion des références utilisées dans les références définies. `[9]` est définie mais inutilisée ; aucune citation utilisée n’est orpheline dans les trois dérivés. La présence d’une URL ne valide ni son contenu ni sa suffisance pour un claim.

L’étape 12, en-tête et prose, est inchangée dans les trois matrices. Le pied de statut global v0.3 et la section `References`, ajoutés après cette étape, sont exclus de la comparaison des étapes. Ils ne constituent pas une reformulation de l’étape 12.

## Rectifications du reçu comparatif v0.2

Les identifiants `REV-*` du reçu PR 6 ne sont pas des décisions retrouvées dans le registre. Le registre réel est [CITATION-PATCH-001](../ELYSIUM_V02_STABILIZATION/CITATION-PATCH-001.md), dont le statut est une proposition additionnelle non canonique. La correspondance est établie par sujet, sans substitution mécanique de préfixes :

| Sujet | Entrée effectivement établie dans le registre |
|---|---|
| Limites planétaires | `CIT-ECO-001` |
| Subventions fossiles | `CIT-ECO-003` / `RF-ECO-001` ; année et méthodologie à conserver |
| GBO-5 / objectifs d’Aichi | `CIT-ECO-002` / `RF-ECO-002` |
| Sixième extinction | `RF-BIO-003` ; qualification et contextualisation requises |
| Pertes en points de PIB mondial | Réserve non numérotée dans « Claims requiring further evidence before citation » ; reste `REVIEW` |
| Zoonoses | Aucune décision correspondante établie dans ce registre ; revue ouverte |
| Natural Capital Protocol | Aucune décision correspondante établie dans ce registre ; revue ouverte |

La « décision Founder préalable `A/A/A` » est **citée mais non vérifiée** : aucune preuve authentifiée disponible n’en établit le sens, le périmètre ou l’autorité. Aucune approbation n’est ajoutée au [registre des décisions](../../docs/decisions/DECISION-LEDGER.md). L’autorisation du présent correctif documentaire n’authentifie pas cette décision citée.

## Validations ouvertes et limites

- Revue sémantique et suffisance des sources : `PENDING` ; les contrôles de références ci-dessus restent mécaniques.
- Candidats v0.2 : `DERIVED_DRAFT_QA_PENDING` ; enfants v0.3 : `DERIVED_DRAFT_CITATION_QA_PENDING` (statut du pied v0.3, distinct du bloc de métadonnées hérité).
- `DOC_06` : `DRAFT_INTEGRATED_QA_PENDING`, `qa_state: PENDING`, selon la [matrice QA documentaire](../DOCUMENT_QA_MATRIX.json).
- MVS-05 : structure des candidats et provenance vérifiées, revue de structure source et QA sémantique/citations ouvertes. MVS-1 reste `NOT_YET_PASSED` ; aucun `MVS-1 PASS` n’est établi.
- Aucune promotion au canon ni substitution de source. ETF conserve `execution_state: relational_only` dans le [registre des relations](../ELYSIUM_TAXONOMY_FEDERATION/RELATION-REGISTRY.yaml), avec non-équivalence et périmètres distincts.
- Contrôle élargi des sommes : les 206 charges utiles du [manifeste historique racine](../../SHA256SUMS.txt) et les 8 entrées hors auto-référence de `V02_EVIDENCE.sha256` concordent. Les deux entrées qui prétendent hacher leur propre manifeste ne concordent pas, déjà à la base vérifiée ; les reçus restent intacts. Cette limite ne concerne pas les six empreintes de dérivés.

## Observations de revue sources

- PR 5 : [raccorder v0.3](https://github.com/yj000018/elysium-civilizational-ontology/pull/5#discussion_r4267777816) ; [rendre le gate découvrable](https://github.com/yj000018/elysium-civilizational-ontology/pull/5#discussion_r4267777827).
- PR 6 : [preuve de la décision citée](https://github.com/yj000018/elysium-civilizational-ontology/pull/6#discussion_r4267833299) ; [identifiants inexistants](https://github.com/yj000018/elysium-civilizational-ontology/pull/6#discussion_r4267833305).
- PR 7 : [ensembles de références](https://github.com/yj000018/elysium-civilizational-ontology/pull/7#discussion_r4267847201) ; [étape 12 inchangée](https://github.com/yj000018/elysium-civilizational-ontology/pull/7#discussion_r4267847204).
