# ELYSIUM — Paquet d’application éditoriale contrôlée

**Date :** 2026-10-14  
**Mode :** proposition uniquement ; addition-only  
**Founder Gate préalable :** 7/7 décisions validées `A/A/A/A/A/A/A`  
**Invariants :** matrices sources et dérivées inchangées ; aucune promotion `CANONICAL`

## Règle d’application

Ce document sépare :

1. les formulations déjà défendables avec les références présentes ;
2. les claims nécessitant encore une source dédiée ;
3. les formulations qui relèvent du cadre interne ELYSIUM et non d’une mesure empirique.

Aucune ligne de ce paquet ne modifie les matrices. Toute application dans un fichier v0.3-cited devra faire l’objet d’un gate éditorial distinct et conserver le hash du parent v0.2.

## A. Reformulations prêtes pour revue éditoriale

| ID | Matrice / étape | Claim | Reformulation proposée | Source | État |
|---|---|---|---|---|---|
| `RF-MOB-001` | Mobilité / 4 | Transport ≈23 % CO₂ | « La CEE-ONU indique, dans sa fiche de référence sur le transport et le climat, que le transport représente environ 23 % des émissions anthropiques mondiales de CO₂ ; cette proportion doit être lue avec le périmètre et la date de la source. » | UNECE [4] | `READY_FOR_EDITORIAL_GATE` |
| `RF-BIO-001` | Biodiversité / 4 | Un million d’espèces | « Selon l’évaluation mondiale de l’IPBES publiée en 2019, environ un million d’espèces sont menacées d’extinction, dont beaucoup dans les prochaines décennies. » | IPBES [1][2] | `READY_FOR_EDITORIAL_GATE` |
| `RF-BIO-002` | Biodiversité / 4 | Déclin de 68 % | « Le Living Planet Report 2020 du WWF estimait une baisse moyenne de 68 % de la taille des populations de vertébrés suivies entre 1970 et 2016. » | WWF [3] | `READY_FOR_EDITORIAL_GATE` |
| `RF-BIO-003` | Biodiversité / 5 | Droits de la nature en Équateur | Présenter la Constitution équatorienne de 2008 comme exemple juridiquement situé de reconnaissance de droits de la nature, avec référence aux articles pertinents ; ne pas généraliser à un standard mondial. | Constitution Équateur [8] | `READY_FOR_EDITORIAL_GATE` |
| `RF-ECO-001` | Écosystèmes / 4 | Objectifs d’Aichi | « Le Global Biodiversity Outlook 5 concluait que les objectifs d’Aichi n’avaient pas été atteints à l’horizon 2020. » | CBD GBO‑5 [10] | `READY_FOR_EDITORIAL_GATE` |
| `RF-ECO-002` | Écosystèmes / 4 | Subventions fossiles | « Une estimation du FMI projetait pour 2017 des subventions fossiles mondiales de 5,2 milliers de milliards de dollars, en incluant des composantes implicites liées notamment aux externalités. » | FMI [6] | `READY_FOR_EDITORIAL_GATE` |

## B. Claims encore bloqués par source ou qualification

| ID | Claim | Décision appliquée | Action requise | État |
|---|---|---|---|---|
| `REV-MOB-001` | Pertes en points de PIB mondial | Ne pas publier le chiffre comme fait mondial établi ; conserver un ordre de grandeur analytique seulement si la source exacte est attachée. | Source économique précise, périmètre et année. | `SOURCE_REQUIRED` |
| `REV-BIO-001` | Biodiversité et zoonoses | Ne pas renforcer la causalité ; conserver une formulation prudente ou retirer le passage assertif. | Source scientifique dédiée. | `SOURCE_REQUIRED` |
| `REV-BIO-002` | Natural Capital Protocol | Le présenter comme cadre/initiative, jamais comme norme universelle. | Référence institutionnelle directe au protocole. | `SOURCE_REQUIRED` |
| `REV-ECO-003` | « Sixième extinction » | Préférer « crise contemporaine de l’extinction » tant qu’une source scientifique contextualisée n’est pas attachée. | Source scientifique explicite et débat de qualification. | `SOURCE_OR_REFORMULATION_REQUIRED` |

## C. Claims à traiter comme cadre interne ELYSIUM

| ID | Domaine | Traitement obligatoire |
|---|---|---|
| `REV-ECO-001` | Limites planétaires | La référence [9] peut documenter le cadre scientifique, mais ELYSIUM ne doit pas transformer les limites en seuils binaires absolus. |
| `REV-ECO-002` | Axes de transition | Les formulations prescriptives ou structurantes doivent être marquées comme cadre interne ELYSIUM lorsqu’elles ne décrivent pas une mesure empirique. |
| `REV-FED-001` | ETF | Les relations A/B restent des correspondances proposées avec scope delta ; aucune synonymie ni équivalence forte. |

## D. Décision proposée pour le prochain gate

Le prochain gate éditorial peut porter uniquement sur les six reformulations de la section A :

- validation de leur insertion dans une future version dérivée v0.3 révisée ; ou
- maintien en proposition sans insertion.

Les quatre claims de la section B restent bloqués sans nouveau paquet probant. La section C est une contrainte de rédaction, non une autorisation de canonisation.

## État global

```text
Founder gate 7/7                  = RECORDED
Ready-to-review reformulations    = 6
Claims requiring new evidence     = 4
Internal-framework boundaries     = 3
Matrix modification               = NOT_EXECUTED
Canonical promotion               = NOT_AUTHORIZED
```

**Statut :** `EDITORIAL_APPLICATION_PROPOSAL_READY_FOR_GATE`.
