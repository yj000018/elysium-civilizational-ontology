# Graph & Resource Dashboard

*This dashboard is designed to be rendered by Dataview in Obsidian.*

## Unverified Resources

```dataview
TABLE 
  resource.category as "Category", 
  resource.relevance as "Relevance"
FROM "BOOK/resources/_pending"
WHERE status = "TO_VERIFY"
```

## Concept Index

```dataview
TABLE 
  length(file.inlinks) as "Mentions"
FROM "BOOK/resources/concepts"
SORT length(file.inlinks) DESC
```
