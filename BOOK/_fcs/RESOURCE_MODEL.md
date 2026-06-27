# Resource Model

FCS must support resource/entity extraction and navigation.

Resources include: people, institutions, organizations, books, websites, movements, concepts, technologies, places, datasets, frameworks, sources, and case studies.

## Resource Statuses
Allowed statuses:
- `IDENTIFIED`
- `TO_VERIFY`
- `VERIFIED`
- `CANONICAL_SOURCE`
- `NON_CANONICAL_TEXTURE`
- `MENTION_ONLY`
- `REJECTED`
- `ARCHIVED`

## Resource Extraction Workflow
1. AI extracts candidate resources from a module or node.
2. Candidate resource cards are written to `BOOK/resources/_pending/`.
3. Module YAML is updated or proposed with references to pending resources.
4. Status = `TO_VERIFY`.
5. Later source/review pass verifies and promotes resources.

Do not perform full real resource extraction in Phase III-0A. Create the system, folders, templates, scripts, and a tiny test example only if needed.
