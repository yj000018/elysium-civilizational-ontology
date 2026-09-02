# ELYSIUM v0.2 — Citation and Reformulation Patch Proposal

**Status:** proposed, addition-only, not canonical.  
**Scope:** citation registry and wording proposals for the three merged `DERIVED_DRAFT_QA_PENDING` matrices.  
**Non-goal:** no alteration of the v0.2 files, no promotion, no deletion of inherited prose.

## Governing rule

This patch treats the v0.2 matrices as derived drafts. It does not convert a source-backed claim into recovered historical material. Each proposed wording retains the source's date, scope and methodological limits. Claims without sufficient evidence remain marked `REVIEW` rather than being silently strengthened.

## Citation registry

| ID | Matrix | Claim class | Proposed disposition | Source |
|---|---|---|---|---|
| CIT-BIO-001 | Biodiversity | About one million species threatened with extinction | Accept with IPBES 2019 qualifier; do not write « one million species extinct ». | [1] [2] |
| CIT-BIO-002 | Biodiversity | 68% decline in vertebrate populations | Accept only as monitored population sizes, 1970–2016, WWF LPR 2020. | [3] |
| CIT-BIO-003 | Biodiversity | Ecuador constitutional rights of nature | Accept with direct reference to the 2008 Constitution and relevant articles. | [8] |
| CIT-ECO-001 | Ecosystems | Planetary boundaries / Johan Rockström | Accept as a scientific framework first proposed in 2009; cite the original paper in a later scholarly pass. | [9] |
| CIT-ECO-002 | Ecosystems | GBO-5 and Aichi targets | Narrow wording to « the Aichi Biodiversity Targets were not met »; do not generalize to every biodiversity objective. | [10] |
| CIT-ECO-003 | Ecosystems | Fossil-fuel subsidies above USD 5 trillion | State year and methodology: IMF projection of USD 5.2 trillion for 2017, including implicit/externality-related components. | [6] |
| CIT-MOB-001 | Mobility | Transport around 23% of anthropogenic CO2 | Qualify source scope and date; UNECE reports approximately 23% of total man-made CO2 emissions worldwide on its reference page. | [4] |

## Claims requiring further evidence before citation

The following claims are not sufficiently supported by the current source set: global dominance of individual thermal vehicles, lobbying influence by automotive/oil multinationals, economic losses measured in percentage points of world GDP, and claims about current deployment of low-emission zones, shared mobility and electrification. They remain `REVIEW`; no numerical or causal strengthening is proposed.

The phrase « sixth mass extinction » remains `QUALIFY`. A scientific source should be added or the wording should be changed to « contemporary extinction crisis » to avoid presenting an interpretive label as an uncontested measurement.

## Proposed reformulations

| ID | Current risk | Safer proposed wording |
|---|---|---|
| RF-BIO-001 | Confuses threatened species with extinctions | « Selon l’évaluation mondiale de l’IPBES publiée en 2019, environ un million d’espèces sont menacées d’extinction, dont beaucoup dans les prochaines décennies. » [1] [2] |
| RF-BIO-002 | Confuses populations with species | « Le Living Planet Report 2020 du WWF estimait une baisse moyenne de 68 % de la taille des populations de vertébrés suivies entre 1970 et 2016. » [3] |
| RF-ECO-001 | Omits IMF year and methodology | « Une estimation du FMI projetait pour 2017 des subventions fossiles mondiales de 5,2 milliers de milliards de dollars, en incluant des composantes implicites liées notamment aux externalités. » [6] |
| RF-ECO-002 | Overgeneralizes GBO-5 | « Le Global Biodiversity Outlook 5 concluait que les objectifs d’Aichi n’avaient pas été atteints à l’horizon 2020. » [10] |
| RF-MOB-001 | Presents an undated ratio as universal | « La CEE-ONU indique, dans sa fiche de référence sur le transport et le climat, que le transport représente environ 23 % des émissions anthropiques mondiales de CO₂ ; cette proportion doit être lue avec le périmètre et la date de la source. » [4] |
| RF-BIO-003 | Presents a contested label as settled fact | « La période actuelle est décrite par plusieurs travaux comme une crise contemporaine de l’extinction ; la qualification de “sixième extinction de masse” doit être référencée et contextualisée. » |

## Release gate

**Citation patch status: READY FOR REVIEW, not ready for merge.** The patch may be added to a separate PR as a registry of proposed citations and reformulations. It must not edit the three v0.2 matrices until the wording and source placement are approved. A later v0.3 may apply the approved patch while preserving parent hashes and recording every change.

## References

[1]: https://www.un.org/sustainabledevelopment/blog/2019/05/nature-decline-unprecedented-report/ "United Nations — IPBES Global Assessment summary"

[2]: https://files.ipbes.net/ipbes-web-prod-public-files/downloads/spm_unedited_advance_for_posting_htn.pdf "IPBES — Summary for policymakers, 2019"

[3]: https://www.worldwildlife.org/news/press-releases/68-average-decline-in-species-population-sizes-since-1970-says-new-wwf-report/ "WWF — Living Planet Report 2020, 68%"

[4]: https://unece.org/transport/climate-change-and-sustainable-transport "UNECE — Climate Change and Sustainable Transport"

[5]: https://www.worldwildlife.org/news/press-releases/catastrophic-73-decline-in-the-average-size-of-global-wildlife-populations-in-just-50-years-reveals-a-system-in-peril/ "WWF — Living Planet Report 2024, 73%"

[6]: https://www.imf.org/en/publications/wp/issues/2019/05/02/global-fossil-fuel-subsidies-remain-large-an-update-based-on-country-level-estimates-46509 "IMF — Global fossil fuel subsidies update"

[7]: https://www.decadeonrestoration.org/publications/principles-ecosystem-restoration-guide-united-nations-decade-2021-2030 "UN Decade — Principles for ecosystem restoration"

[8]: https://pdba.georgetown.edu/Constitutions/Ecuador/english08.html "Ecuador — Constitution of 2008"

[9]: https://www.stockholmresilience.org/research/planetary-boundaries.html "Stockholm Resilience Centre — Planetary Boundaries"

[10]: https://www.cbd.int/gbo/gbo5/publication/gbo-5-en.pdf "Convention on Biological Diversity — Global Biodiversity Outlook 5"
