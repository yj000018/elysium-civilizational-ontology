# Views and Rendering Model

FCS must support four working view modes: brief, expanded, review, and clean.

## Brief View
Displays only the node itself (`index.md` or module file). This is the architectural card / node brief.

## Expanded View
Displays continuous content of children according to `manifest.md`. For example, a chapter folder can be viewed as a chapter index brief or a complete flowing chapter assembled from all child modules.

## Review View
Displays content plus useful metadata: status, word count, warnings, missing sources, related resources, review notes, and unsupported claims warnings.

## Clean View
Displays clean content for downstream handoff. No internal frontmatter, no AI notes, no internal review blocks. This is still a source/handoff output, not a final designed publication.
