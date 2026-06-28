# ELYSIUM Book Resource Extraction Plan

**Status:** CANONICAL
**Phase:** Phase III-0B
**Last Updated:** 2026-06-27

## Purpose
This document defines how external entities (people, books, institutions, etc.) mentioned in the manuscript are extracted, tracked, and managed as structured data.

## Why Extract Resources?
ELYSIUM is not just a book; it is an ontology. The entities cited within the text form a valuable database for the reader (and for the author's future work). By extracting them into structured markdown files, we can generate a "Resource Graph" and automated bibliographies.

## Resource Categories
The `resources` field in the frontmatter of any node supports the following categories:
- `people`: Key thinkers, authors, historical figures.
- `institutions`: Universities, government bodies, international organizations.
- `organizations`: Companies, NGOs, specific projects.
- `books`: Core texts cited or recommended.
- `websites`: Key digital resources or databases.
- `movements`: Social, political, or philosophical movements.
- `technologies`: Specific technological systems or paradigms.
- `places`: Significant geographic locations or case study sites.
- `datasets`: Specific data sources (e.g., IPCC reports, World Bank data).
- `frameworks`: Analytical models (other than the core 126 ELYSIUM models).
- `sources`: General academic papers or articles.
- `case_studies`: Specific real-world examples analyzed in depth.

## Extraction Workflow
1. **Drafting:** Claude writes a module and naturally cites a book (e.g., *Thinking in Systems* by Donella Meadows).
2. **Identification:** The Chief Architect or a specific Claude extraction prompt identifies "Donella Meadows" and "Thinking in Systems" as valuable resources.
3. **Scaffolding:** Manus creates `BOOK/resources/people/donella_meadows.md` and `BOOK/resources/books/thinking_in_systems.md`.
4. **Linking:** The module's frontmatter is updated to include these IDs under `resources.people` and `resources.books`.
5. **Generation:** `resources.py` and `graph.py` automatically compile these links into indexes and visualizations.

## Phase III-0B Status
Currently, the resource directories are scaffolded but empty. Extraction will occur *after* the initial drafting phases (Phase III-1 and beyond) once actual prose exists to mine.

## Next Actions
- During Phase III-1, test the extraction workflow on the Opening Draft to ensure the pipeline functions correctly.
