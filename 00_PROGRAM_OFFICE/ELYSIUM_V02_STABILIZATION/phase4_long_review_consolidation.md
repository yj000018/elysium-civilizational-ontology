# ELYSIUM — Consolidation du long run v0.2

## Verdict consolidé

Les trois dérivés v0.2 sont mécaniquement valides : chacun contient douze étapes, un hash parent correct et un statut non canonique. La revue longue distingue toutefois la validité de structure de la maturité éditoriale. Aucune promotion `CANONICAL` n’est autorisée à ce stade.

| Facette | Revue sémantique | Revue factuelle | Disposition |
|---|---|---|---|
| `F01_05_MOBILITE` | `REVIEW` : complétion plus concise que le parent ; références à ajouter. | Claims hérités sourçables, mais contexte temporel du 23 % CO₂ à préciser. | Publier seulement comme dérivé QA pending ; expansion éditoriale ultérieure. |
| `F02_03_BIODIVERSITE` | `REVIEW` : profondeur asymétrique ; crosswalk ETF explicite à ajouter. | IPBES 2019 et WWF 2020 sourçables ; « sixième extinction » à qualifier. | Publier seulement comme dérivé QA pending ; ne pas canoniser. |
| `F02_04_ECOSYSTEMES` | `PASS` avec réserve P2 : sections 5–11 encore en résumé. | Claim IMF sur les subventions doit préciser année et définition explicite/implicite. | Publier comme dérivé QA pending ; revue factuelle nécessaire. |

## Corrections interdites automatiquement

Le long run ne réécrit pas les fragments hérités et ne transforme pas les complétions en prétendue récupération historique. Il ne met pas à jour silencieusement les statistiques 68 % vers 73 %, car ces valeurs correspondent à deux éditions et périodes distinctes du Living Planet Index. Il ne remplace pas non plus la formule « sixième extinction de masse » sans arbitrage éditorial et source scientifique dédiée.

## Provenance et publication

Tout paquet publiable doit contenir les trois dérivés, leur registre de parenté, le rapport de revue sémantique, la revue factuelle et les empreintes SHA-256. Le répertoire cible doit être explicitement dérivé, ne doit pas être confondu avec les matrices canoniques et ne doit modifier aucun fichier source existant.

## Gate

**PR addition-only : autorisable sous statut `DERIVED_DRAFT_QA_PENDING`.**  
**Merge vers le canon : non autorisable avant revue humaine des points P1 et des citations.**

Le prochain paquet doit donc être une PR de conservation et de traçabilité, pas une PR de canonisation. Les décisions sémantiques restent séparées des corrections de registre et des mises à jour factuelles.

## Sources factuelles préservées

[1]: https://www.un.org/sustainabledevelopment/blog/2019/05/nature-decline-unprecedented-report/ "United Nations — IPBES Global Assessment summary"
[2]: https://files.ipbes.net/ipbes-web-prod-public-files/downloads/spm_unedited_advance_for_posting_htn.pdf "IPBES — Summary for policymakers, 2019"
[3]: https://www.worldwildlife.org/news/press-releases/68-average-decline-in-species-population-sizes-since-1970-says-new-wwf-report/ "WWF — Living Planet Report 2020, 68%"
[4]: https://www.worldwildlife.org/news/press-releases/catastrophic-73-decline-in-the-average-size-of-global-wildlife-populations-in-just-50-years-reveals-a-system-in-peril/ "WWF — Living Planet Report 2024, 73%"
[5]: https://unece.org/transport/climate-change-and-sustainable-transport "UNECE — Climate Change and Sustainable Transport"
[6]: https://www.imf.org/en/publications/wp/issues/2019/05/02/global-fossil-fuel-subsidies-remain-large-an-update-based-on-country-level-estimates-46509 "IMF — Global fossil fuel subsidies update"
[7]: https://www.decadeonrestoration.org/publications/principles-ecosystem-restoration-guide-united-nations-decade-2021-2030 "UN Decade — Principles for ecosystem restoration"
