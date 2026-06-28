# ELYSIUM — Opening Part Dynamic Binder

> **Requires:** Obsidian Dataview plugin
> **Filter:** `part = "OPENING"`
> **This page is the live Obsidian binder for the Opening Part.**
> **The static export is generated separately.**

---

## Opening Part Hierarchy

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  movement_id AS "Movement",
  movement_title AS "Movement Title",
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

## Movement I — Le Malaise du Présent

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  order AS "Order",
  operational_status AS "Op. Status",
  prose_status AS "Prose"
FROM "BOOK/manuscript"
WHERE fcs_role AND part = "OPENING" AND movement_id = "MOV-I"
SORT order ASC
```

---

## Movement II — L'Échec des Cartes Fragmentées

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  order AS "Order",
  operational_status AS "Op. Status",
  prose_status AS "Prose"
FROM "BOOK/manuscript"
WHERE fcs_role AND part = "OPENING" AND movement_id = "MOV-II"
SORT order ASC
```

---

## Movement III — La Civilisation comme Métabolisme

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  order AS "Order",
  operational_status AS "Op. Status",
  prose_status AS "Prose"
FROM "BOOK/manuscript"
WHERE fcs_role AND part = "OPENING" AND movement_id = "MOV-III"
SORT order ASC
```

---

## Movement IV — La Carte d'ELYSIUM

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  order AS "Order",
  operational_status AS "Op. Status",
  prose_status AS "Prose"
FROM "BOOK/manuscript"
WHERE fcs_role AND part = "OPENING" AND movement_id = "MOV-IV"
SORT order ASC
```

---

## Opening Provisional Drafts (raw material)

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  operational_status AS "Op. Status",
  raw_material_for AS "Raw Material For"
FROM "BOOK/manuscript"
WHERE fcs_role AND part = "OPENING" AND operational_status = "PROVISIONAL_MANUS_DRAFT"
SORT order ASC
```

---

## Opening Structure Drafts (Phase III-1A-S1)

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  movement_id AS "Movement",
  order AS "Order",
  operational_status AS "Op. Status"
FROM "BOOK/manuscript"
WHERE fcs_role AND part = "OPENING" AND operational_status = "STRUCTURE_DRAFT"
SORT order ASC
```

---

## Opening Modules Ready for Writing

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  movement_id AS "Movement",
  operational_status AS "Op. Status"
FROM "BOOK/manuscript"
WHERE fcs_role AND part = "OPENING" AND operational_status = "READY_FOR_ROUTED_WRITING"
SORT order ASC
```

---

## Opening Modules Needing Review

```dataview
TABLE WITHOUT ID
  module_id AS "ID",
  file.link AS "Module",
  movement_id AS "Movement",
  status AS "FCS Status"
FROM "BOOK/manuscript"
WHERE fcs_role AND part = "OPENING" AND (status = "REVIEW_PENDING" OR operational_status = "REVIEW_PENDING")
SORT order ASC
```

---

*Reader movement: sentir → comprendre l'échec → changer de métaphore → recevoir la carte*
*Static export: `BOOK/_fcs/binder_views/opening_binder_view.md`*
*Regenerate: `python scripts/generate_binder_view.py`*
