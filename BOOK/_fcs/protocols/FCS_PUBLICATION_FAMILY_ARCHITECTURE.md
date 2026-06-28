---
id: FCS_PUBLICATION_FAMILY_ARCHITECTURE
title: "FCS Publication Family Architecture"
type: protocol
version: "0.1"
status: ACTIVE
created_by: "Manus — Phase III FCS Publication Family Architecture"
created_date: "2026-06-28"
---

# FCS Publication Family Architecture

## 1. Purpose

Define how FCS manages multiple publications, series, collections, atlases, practical guides, workbooks, translations, and derivative products from a shared source ontology.

This protocol establishes the canonical pattern for organizing publication families within the FCS system and ensures that all publications are described through metadata before any prose is written.

## 2. Core Principle

**FCS is a publication architecture system, not only a single-book production system.**

One source ontology can generate many publication forms.

This principle supersedes any prior assumption that FCS manages isolated books only. Every publication in the ELYSIUM ecosystem — and any future ecosystem built on FCS — must be registered in the publication family registry before production begins.

## 3. Publication Types

FCS supports the following publication types:

| Type | Description |
|---|---|
| `core_book` | Presents the resulting model or ontology |
| `atlas` | Documents the research corpus, comparative synthesis, and emergence process |
| `companion_volume` | Supplements the core book with extended material |
| `practical_guide` | Translates the ontology into accessible, actionable domain-specific guides |
| `practical_series` | A collection of practical guides sharing a common template |
| `field_manual` | Operational reference for practitioners |
| `workbook` | Structured exercises and reflection tools |
| `course` | Curriculum-based learning format |
| `app_content` | Content structured for application delivery |
| `website_content` | Content structured for web delivery |
| `translation_edition` | A translated version of any publication |
| `derivative_product` | Any product derived from the source ontology |

## 4. Family Model

A publication family groups all publications derived from a single source model or ontology. A family may include:

- Source ontology (the canonical model)
- Core book (presents the resulting model)
- Companion atlas (documents the research corpus)
- Practical series (accessible, domain-specific guides)
- Workbooks and field manuals
- Courses and app/site content
- Translated editions

Every family must have a `family_id` and be registered in `publication_family_registry.yaml`.

## 5. Core Book vs. Atlas Rule

**Core books present the resulting model.**

Core books do not include the full research corpus, comparative analysis, or detailed influence mapping. They present the ontology, its structure, its logic, and its implications in a form accessible to the intended reader.

**Atlas / Great Synthesis volumes document the research field.**

Atlas volumes document the corpus of models, frameworks, thinkers, and civilizational maps that informed the ontology. They include comparative synthesis, influence mapping, and the emergence process. They are research documents, not introductory texts.

Do not overload core books with full research corpus. Do not reduce atlas volumes to summaries.

## 6. Practical Series Rule

Practical series translate the source ontology into accessible, actionable, domain-specific transformation guides.

Each volume in a practical series:
- Focuses on one domain, pillar, or problem
- Follows a stable macro-template (e.g., the FIX IT template: See It / Name It / Map It / Fix It / Transform It)
- Is less intellectually demanding than the core book
- Remains grounded in the full source ontology
- Is independently readable without prior knowledge of the core book

## 7. Metadata-Driven Generation

Every publication must be described through metadata before any prose is written. The following fields are required for all publications:

| Field | Description |
|---|---|
| `publication_id` | Unique identifier |
| `title` | Full title |
| `subtitle` | Subtitle |
| `publication_type` | One of the supported types above |
| `family_id` | Parent family identifier |
| `series` | Series identifier if applicable |
| `collection` | Collection identifier if applicable |
| `canonical_role` | One-sentence description of the publication's role |
| `source_model` | The source ontology or model |
| `related_core_book` | Related core book if applicable |
| `related_atlas` | Related atlas if applicable |
| `related_publications` | Other related publications |
| `primary_foundation` | Primary foundation from the source ontology |
| `secondary_foundations` | Secondary foundations |
| `related_facets` | Related facets |
| `target_reader` | Intended reader profile |
| `complexity` | Complexity level |
| `tone` | Tone guidance |
| `format_template` | Template identifier |
| `status` | CONCEPT / ACTIVE / IN_PRODUCTION / COMPLETE |
| `source_language` | Source language (default: en) |
| `translation_targets` | Target languages for translation |
| `prose_status` | NOT_WRITTEN / IN_PROGRESS / DRAFT / COMPLETE |
| `xray_status` | NOT_CREATED / XRAY_DRAFT / XRAY_APPROVED |
| `routing_status` | NOT_ROUTED / ROUTED / IN_REVIEW / APPROVED |

## 8. Translation Rule

Source publication metadata is English-first.

All `publication_id`, field names, and structural metadata use English. Full translations are future edition layers and are managed as separate `translation_edition` publications in the registry.

## 9. Status Flow

```
CONCEPT → ACTIVE → IN_PRODUCTION → COMPLETE
```

A publication may not enter IN_PRODUCTION until:
- Metadata is complete
- X-Ray structural layer is created (XRAY_APPROVED)
- Writing briefs are generated
- Routing is confirmed

## 10. FCS Principle Update

This protocol installs the following principle into FCS:

> FCS is not only a book production system. FCS is a publication architecture system. One source ontology can generate many publication forms. Every publication — regardless of type, format, or language — must be registered in the publication family registry before production begins.
