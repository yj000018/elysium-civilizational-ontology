# Review Dashboard

*This dashboard is designed to be rendered by Dataview in Obsidian.*

## Modules in REVIEW_PENDING

```dataview
TABLE 
  type as "Type", 
  review.last_reviewed_by as "Last Reviewer"
FROM "BOOK/manuscript"
WHERE status = "REVIEW_PENDING"
```

## Missing Summaries

```dataview
TABLE 
  type as "Type"
FROM "BOOK/manuscript"
WHERE !summary OR summary = ""
```

## Missing Reader Promise

```dataview
TABLE 
  type as "Type"
FROM "BOOK/manuscript"
WHERE !reader_promise OR reader_promise = ""
```
