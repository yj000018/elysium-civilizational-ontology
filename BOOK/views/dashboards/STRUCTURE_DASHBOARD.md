# Structure Dashboard

*This dashboard is designed to be rendered by Dataview in Obsidian.*

## Manuscript Overview

```dataview
TABLE 
  status as "Status", 
  type as "Type", 
  length(children) as "Children", 
  review.review_unit as "Review Unit"
FROM "BOOK/manuscript"
WHERE type = "book" OR type = "part" OR type = "chapter" OR type = "foundation" OR type = "facet"
SORT file.name ASC
```

## Modules Needing Attention

```dataview
TABLE 
  status as "Status", 
  summary as "Summary"
FROM "BOOK/manuscript"
WHERE type = "module" AND status = "SCAFFOLDED"
SORT file.name ASC
```
