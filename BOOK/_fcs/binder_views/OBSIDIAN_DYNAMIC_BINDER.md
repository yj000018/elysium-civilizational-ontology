# ELYSIUM — Obsidian Dynamic Binder

> **Requires:** Obsidian Dataview plugin
> **Source of truth:** module frontmatter + `BOOK/_fcs/registries/book_module_registry.yaml`
> **This file:** live dynamic view — do not edit manually

---

## All Manuscript Modules

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  type AS "Type",
  part AS "Part",
  movement_id AS "Movement",
  order AS "Order",
  status AS "FCS Status",
  operational_status AS "Op. Status",
  prose_status AS "Prose",
  routing_status AS "Routing"
FROM "BOOK/manuscript"
WHERE fcs_role
SORT part ASC, order ASC
```

---

## Opening Part — All Modules

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  movement_id AS "Movement",
  order AS "Order",
  status AS "FCS Status",
  operational_status AS "Op. Status",
  prose_status AS "Prose",
  routing_status AS "Routing"
FROM "BOOK/manuscript"
WHERE fcs_role AND part = "OPENING"
SORT order ASC
```

---

## Provisional Manus Drafts

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  part AS "Part",
  operational_status AS "Op. Status",
  routing_status AS "Routing"
FROM "BOOK/manuscript"
WHERE operational_status = "PROVISIONAL_MANUS_DRAFT"
SORT part ASC, order ASC
```

---

## Structure Drafts (Phase III-1A-S1)

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  movement_id AS "Movement",
  order AS "Order",
  operational_status AS "Op. Status"
FROM "BOOK/manuscript"
WHERE operational_status = "STRUCTURE_DRAFT"
SORT order ASC
```

---

## Ready for Routed Writing

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  part AS "Part",
  movement_id AS "Movement",
  operational_status AS "Op. Status"
FROM "BOOK/manuscript"
WHERE operational_status = "READY_FOR_ROUTED_WRITING"
SORT part ASC, order ASC
```

---

## Review Pending

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  part AS "Part",
  status AS "FCS Status",
  operational_status AS "Op. Status"
FROM "BOOK/manuscript"
WHERE status = "REVIEW_PENDING" OR operational_status = "REVIEW_PENDING"
SORT part ASC, order ASC
```

---

## Full Status Distribution

```dataview
TABLE WITHOUT ID
  status AS "FCS Status",
  count(rows) AS "Count"
FROM "BOOK/manuscript"
WHERE fcs_role
GROUP BY status
```

---

## By Foundation (Part 02)

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  foundation AS "Foundation",
  facet AS "Facet",
  status AS "Status"
FROM "BOOK/manuscript"
WHERE fcs_role AND part = "FOUNDATIONS"
SORT foundation ASC, order ASC
```

---

*Static export: `BOOK/_fcs/binder_views/current_binder_view.md`*
*Regenerate: `python scripts/generate_binder_view.py`*
*Protocol: `BOOK/_fcs/protocols/FCS_DYNAMIC_BINDER_PROTOCOL.md`*
