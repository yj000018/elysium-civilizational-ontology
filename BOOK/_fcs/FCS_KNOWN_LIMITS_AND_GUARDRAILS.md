# FCS Known Limits & Guardrails

## 1. Architectural Guardrails
- **Not a Final Publisher:** FCS is an authoring and architectural environment. It is not designed to directly generate the final PDF/EPUB. Pandoc or similar tools will be needed later.
- **Not Scrivener:** FCS relies on plain text, YAML, and scripts. It lacks a GUI binder, relying instead on Obsidian for visualization.
- **Repo-Native:** FCS currently lives entirely within the GitHub repository. It is not a standalone web app or heavy application.
- **Obsidian is UX Only:** Obsidian provides the visual interface (Dataview, Graph). It is not the source of truth; the Markdown files and Python scripts are.

## 2. Content Guardrails
- **Review Required:** Claude output must ALWAYS be reviewed before source lock. AI hallucination remains a risk.
- **Resource Verification:** Resources extracted by scripts start as `TO_VERIFY`. They must be manually or semi-manually validated before becoming canonical.
- **Candidate Models:** The 10 proposed candidate models remain non-canonical. Only the original 126 analyzed models are integrated. We do NOT claim 136 integrated models.

## 3. System Guardrails
- **No yOS Core Integration:** FCS is currently standalone for ELYSIUM. It is not yet integrated into yOS Core.
- **Script Fragility:** The validation scripts rely on strict YAML formatting. Malformed frontmatter will cause script failures.
