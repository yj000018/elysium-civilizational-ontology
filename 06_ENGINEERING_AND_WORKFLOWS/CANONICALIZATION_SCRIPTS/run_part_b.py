#!/usr/bin/env python3
import json
from pathlib import Path

BASE = Path("/home/ubuntu/ELYSIUM_CANON")
DATE = "2026-06-27"

canonical_md = f"""# ELYSIUM CANONICAL FACTS

**Date:** {DATE}
**Status:** CANONICAL_LOCKED
**Owner:** Founder / Chief Architect

---

## 1. Program Identity
- **Program Name:** ELYSIUM
- **Nature:** Open civilizational infrastructure + book + ontology + future observatory seed
- **Status:** Alpha generated package under canonicalization

## 2. Ontology Kernel
**ELYSIUM's current validated ontology kernel is 3 Scales x 7 Foundations x 38 Facets x 12-Step Universal Analysis Matrix.**

*Caution: This ontology kernel is the core backbone, not the complete infrastructure. The complete ELYSIUM system also includes dynamic axes, model corpus, datasets, book architecture, observatory seed, and the yOS Program Operating System extraction layer.*

## 3. Scale Definitions
1. **Human:** The individual scale (body, mind, personal agency, direct relationships).
2. **Society:** The collective scale (institutions, cities, networks, economies, cultures).
3. **Civilization:** The planetary scale (biosphere, global governance, species-level trajectory).

## 4. Foundation Definitions
1. **FOUNDATION** - Material Base
2. **VITALITY** - Life and Ecology
3. **AGENCY** - Economy and Production
4. **COHESION** - Community and Culture
5. **GOVERNANCE** - Coordination and Law
6. **VISION** - Knowledge and Foresight
7. **CONSCIOUSNESS** - Meaning and Purpose

## 5. Facet Count
- **Canonical Count:** 38 Facets.
- *(Note: Earlier drafts claiming 35 facets are deprecated).*

## 6. Universal Matrix
- **Canonical Definition:** 12-Step Universal Analysis Matrix applied to each facet.

## 7. Dynamic Axes
The ontology is traversed by cross-cutting dynamic axes, including at minimum:
- Digital / Cyber dynamics
- Evolutionary dynamics
- Complexity / systems dynamics
- Temporal / transition dynamics

## 8. Model Corpus Status
- **Analyzed Models:** 126 confirmed and fully integrated.
- **Candidate Models:** 10 proposed (not yet canonical until full integration).
- *(Note: Do not claim 136 models integrated until the 10 candidates pass all QA gates).*

## 9. Document Status
- **Count:** 26 institutional documents.
- **Status:** DRAFT_INTEGRATED_QA_PENDING. (None are publication-final).

## 10. Dataset Status
- **Status:** QA pending. Datasets exist but require repair/verification.

## 11. yOS Program OS Status
- **Status:** Program OS pattern discovered through ELYSIUM. Not mature enough for yOS Core integration yet. Extraction pending.

## 12. Open Uncertainties & Blockers
- Exact alignment of the 38 facets across all matrices.
- Verification of local archive for all facet files.
- API routing protocol implementation.

## 13. Explicitly Downgraded Claims
- Claims of "Program Complete" are downgraded to "Phase II Complete / Canonicalization Pending".
- Claims of "136 Models" are downgraded to "126 + 10 candidates".
- Claims of "Final Documents" are downgraded to "Draft Integrated".

## 14. Claims Requiring Founder Validation
- Final approval of the 10 candidate models.
- Approval of the yOS Program OS extraction pattern.
"""

canonical_json = {
    "program_identity": {
        "name": "ELYSIUM",
        "nature": "open civilizational infrastructure + book + ontology + future observatory seed",
        "status": "Alpha generated package under canonicalization"
    },
    "ontology_kernel": {
        "formula": "3 Scales x 7 Foundations x 38 Facets x 12-Step Universal Analysis Matrix",
        "scales": ["Human", "Society", "Civilization"],
        "foundations": [
            "FOUNDATION - Material Base",
            "VITALITY - Life and Ecology",
            "AGENCY - Economy and Production",
            "COHESION - Community and Culture",
            "GOVERNANCE - Coordination and Law",
            "VISION - Knowledge and Foresight",
            "CONSCIOUSNESS - Meaning and Purpose"
        ],
        "facet_count": 38,
        "matrix_steps": 12,
        "dynamic_axes": [
            "Digital / Cyber dynamics",
            "Evolutionary dynamics",
            "Complexity / systems dynamics",
            "Temporal / transition dynamics"
        ]
    },
    "model_corpus": {
        "analyzed_count": 126,
        "candidate_count": 10,
        "status": "126 confirmed, 10 pending integration"
    },
    "document_status": {
        "count": 26,
        "status": "DRAFT_INTEGRATED_QA_PENDING"
    },
    "yos_program_os": {
        "status": "Pattern discovered, extraction pending, not yet in yOS Core"
    },
    "downgraded_claims": [
        "Program Complete -> Phase II Complete / Canonicalization Pending",
        "136 Models -> 126 + 10 candidates",
        "Final Documents -> Draft Integrated",
        "35 Facets -> 38 Facets"
    ]
}

# Save to 01_CANONICAL_FACTS
(BASE / "01_CANONICAL_FACTS" / "ELYSIUM_CANONICAL_FACTS.md").write_text(canonical_md)
(BASE / "01_CANONICAL_FACTS" / "ELYSIUM_CANONICAL_FACTS.json").write_text(json.dumps(canonical_json, indent=2))

# Save cross-copies to 00_PROGRAM_OFFICE
(BASE / "00_PROGRAM_OFFICE" / "ELYSIUM_CANONICAL_FACTS.md").write_text(canonical_md)
(BASE / "00_PROGRAM_OFFICE" / "ELYSIUM_CANONICAL_FACTS.json").write_text(json.dumps(canonical_json, indent=2))

print("PART B COMPLETE ✓")
