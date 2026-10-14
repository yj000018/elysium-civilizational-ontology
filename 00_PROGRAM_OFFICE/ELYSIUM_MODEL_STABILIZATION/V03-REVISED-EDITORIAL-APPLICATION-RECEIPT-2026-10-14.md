# ELYSIUM — Receipt d’application éditoriale v0.3-revised

**Date :** 2026-10-14
**Autorisation :** Founder Gate éditorial — six reformulations validées
**Mode :** nouvelle couche dérivée, addition-only
**Statut :** `DERIVED_DRAFT_EDITORIAL_REVISED_QA_PENDING`

## Périmètre

Création du répertoire :

```text
02_ONTOLOGY_AND_KNOWLEDGE/FACET_MATRICES_DERIVED_V03_REVISED/
```

Les trois parents `v0.3-cited` restent inchangés. Les trois parents `v0.2` restent inchangés.

## Applications

| ID | Facette | Traitement |
|---|---|---|
| `RF-MOB-001` | Mobilité | Reformulation précise du ratio UNECE et suppression du doublon « environ environ ». |
| `RF-BIO-001` | Biodiversité | Formulation IPBES 2019 « environ un million d’espèces menacées ». Déjà présente, conservée et versionnée. |
| `RF-BIO-002` | Biodiversité | Précision WWF : taille des populations de vertébrés suivies, 1970–2016. Déjà présente, conservée et versionnée. |
| `RF-BIO-003` | Biodiversité | Qualification de la Constitution équatorienne comme exemple juridiquement situé, sans généralisation mondiale. |
| `RF-ECO-001` | Écosystèmes | Limitation aux objectifs d’Aichi à l’horizon 2020. Déjà présente, conservée et versionnée. |
| `RF-ECO-002` | Écosystèmes | Précision FMI : estimation 2017, 5,2 milliers de milliards, composantes implicites/externalités. Déjà présente, conservée et versionnée. |

## Protections

- Aucun fichier existant n’est écrasé.
- Aucun claim bloqué n’est renforcé : PIB, zoonoses, Natural Capital Protocol et « sixième extinction » restent hors application.
- Aucun statut `CANONICAL` n’est attribué.
- Les références restent celles déjà présentes ; aucune source nouvelle n’est inventée.
- Le manifeste JSON lie chaque révisé à son parent immédiat `v0.3-cited` et au parent v0.2 déclaré.

## Gate suivant

La couche nécessite encore :

1. QA structurelle 12 étapes ;
2. QA des hashes et de la chaîne parent-enfant ;
3. revue de diff limitée aux six IDs autorisés ;
4. décision séparée sur une éventuelle promotion éditoriale du statut dérivé.
