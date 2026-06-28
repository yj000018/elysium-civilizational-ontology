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

## QA/QC Governance

> **Canonical authority protocol:** [`BOOK/_fcs/protocols/FCS_QA_QC_GOVERNANCE_PROTOCOL.md`](../../_fcs/protocols/FCS_QA_QC_GOVERNANCE_PROTOCOL.md)
>
> Defines QA/QC layers (L0–L4), stop conditions, approval semantics, and F02 gate conditions. ChatGPT API PASS ≠ Chief Architect approval. DRAFT_0 complete ≠ publication-ready.
