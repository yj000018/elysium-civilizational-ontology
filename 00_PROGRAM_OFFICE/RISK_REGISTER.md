# RISK REGISTER

**Date:** 2026-06-27

| ID | Risk | Severity | Mitigation | Status |
|---|---|---|---|---|
| R01 | 2 facet files were CDN-expired | MEDIUM | Regenerated from canonical corpus | MITIGATED |
| R02 | Claude API unavailable during Pass 0.1 | HIGH | GPT-4 fallback used, logged explicitly | MITIGATED |
| R03 | Stale claims persist in old files | HIGH | Full scan + correction in Pass 0.2 | RESOLVED |
| R04 | Zero-byte datasets in REPAIRED/ | MEDIUM | Reconstructed or moved to MISSING | RESOLVED |
| R05 | Multiple competing canonical roots | HIGH | Single ELYSIUM/ hierarchy enforced | RESOLVED |
