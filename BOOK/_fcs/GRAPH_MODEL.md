# Graph Model

FCS must support three interconnected graphs: Content Graph, Concept Graph, and Resource Graph.

## Content Graph
Tracks: book, part, chapter, foundation, facet, module, parent/child relationships, manifest order, depends_on, supports, contrasts_with, and avoid_duplicate_with.

## Concept Graph
Tracks: concepts, themes, recurring ideas, cross-chapter echoes, semantic clusters, and concept dependencies.

## Resource Graph
Tracks: people, institutions, organizations, books, websites, movements, technologies, places, datasets, frameworks, sources, case studies, mentions, relationships, and verification status.

## Required Graph Outputs
Generate or scaffold:
- `BOOK/views/graph/fcs_graph.json`
- `BOOK/views/graph/content_graph.json`
- `BOOK/views/graph/concept_graph.json`
- `BOOK/views/graph/resource_graph.json`
- `BOOK/views/graph/fcs_graph.mmd`
- `BOOK/views/graph/fcs_graph.md`
- `BOOK/views/graph/fcs_adjacency.md`
- `BOOK/views/graph/fcs_graph_readme.md`

Also prepare output copies under `BOOK/output/graphs/` and `BOOK/output/json/`. Graph outputs are both internal architecture aids and future public navigation deliverables (though a public website is not built in this pass).
