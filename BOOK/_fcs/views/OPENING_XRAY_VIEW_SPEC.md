---
id: OPENING_XRAY_VIEW_SPEC
title: "Opening X-Ray View Spec"
type: view_spec
status: SCAFFOLDED
parent: FCS_VIEWS
created_by: "Manus"
phase: "Phase III-1A-S2X"
---

# Opening X-Ray View Spec

## 1. Purpose

Define how the FCS app/Obsidian workflow should display and edit the Opening X-Ray layer.

## 2. Principle

The app should support **architectural writing before prose writing**.

The X-Ray view is the primary Founder interface for:
- reading the book structurally
- iterating the architecture
- adding notes, resources, quotes, cross-links
- approving modules for writing brief generation
- later: triggering routed prose writing

## 3. Ideal interface layout

### Left panel — Binder Tree

- Part / Movement / Module / Beat hierarchy
- Status indicators (XRAY_DRAFT / XRAY_REVIEW / XRAY_APPROVED / READY_FOR_WRITING_BRIEF)
- Language toggle: EN / FR for structural metadata
- Collapse/expand movements
- Filter by status, movement, readiness

### Center panel — Module X-Ray Card

Selected module displays:
- Executive summary (EN + FR)
- Binder highlight (EN + FR)
- Reader state in / out (EN + FR)
- Key points to develop (EN + FR)
- Beats (EN + FR)
- Semantic positioning (EN + FR)
- Transformational role (EN + FR)
- Systemic relevance (EN + FR)

### Right panel — Founder Workspace

- Founder notes (OPEN / RESOLVED / INTEGRATED)
- Resources to use (placeholders + confirmed)
- Quotes to include (PLACEHOLDER / APPROVED)
- Cross-module links (with relation type + reason)
- AI actions (see Section 4)

### Bottom panel — Status Bar

- Status
- Routing status
- Readiness
- Next action
- Prose status

## 4. Actions

Available per module:
- Refine summary
- Add key point
- Add resource
- Add quote
- Add Founder note
- Add cross-link
- Split module
- Merge module
- Move module
- Rename module
- Generate writing brief
- Export X-Ray reader
- Later: write this module (triggers routed prose via ChatGPT + Claude routing)

## 5. Export / print

The X-Ray Reader export (`OPENING_XRAY_READER_EN.md` / `OPENING_XRAY_READER_FR.md`) should:
- Read like a condensed book map, not a database dump
- Let the Founder "read the book" structurally without long prose
- Be suitable for print / PDF / sharing with collaborators
- No module prose longer than the executive summary

## 6. Obsidian implementation notes

Current implementation uses:
- Sidecar X-Ray cards in `BOOK/manuscript/01_opening/xray_modules/`
- Dataview queries in `BOOK/_fcs/binder_views/OPENING_DYNAMIC_BINDER.md`
- Static exports: `OPENING_XRAY_READER_EN.md` / `OPENING_XRAY_READER_FR.md`
- Registry sidecar: `BOOK/_fcs/registries/opening_xray_registry.yaml`

Future FCS app should replace Obsidian Dataview with a native X-Ray editor.

## 7. Language toggle spec

EN view: shows `_en` fields
FR view: shows `_fr` fields
Default: EN
Toggle: per-session preference stored in user settings

## 8. Readiness workflow

```
XRAY_DRAFT → XRAY_REVIEW → XRAY_APPROVED → READY_FOR_WRITING_BRIEF → READY_FOR_ROUTED_PROSE
```

Only Founder can advance a module from XRAY_APPROVED to READY_FOR_WRITING_BRIEF.
Only Founder can trigger READY_FOR_ROUTED_PROSE.
