---
id: FCS_XRAY_STRUCTURAL_WRITING_PROTOCOL
title: "FCS X-Ray Structural Writing Protocol"
type: protocol
status: SCAFFOLDED
parent: FCS_PROTOCOLS
created_by: "Manus"
phase: "Phase III-1A-S2X"
---

# FCS X-Ray Structural Writing Protocol

## 1. Purpose

Define the X-Ray layer as the primary architectural writing surface of FCS.

FCS is not primarily a prose generator.
FCS is first an architectural writing interface.

Its first job is to let the Founder see, refine, and iterate the book's structure before any prose is written.

The X-Ray layer is the primary planning surface of the book.

## 2. Principle

**No prose before structure.**

The book is first written as architecture:
- binder
- movements
- modules
- beats
- executive summaries
- key points
- semantic positioning
- cross-links
- resources
- notes
- tone guidance
- writing constraints

## 3. Prose generation gate

A module may be sent to routed prose writing only after:
1. macro-architecture validated
2. ultra-fine binder validated
3. X-Ray layer enriched
4. writing briefs created
5. module-level generation explicitly requested

And at the module level:
- executive summary exists
- key points exist
- semantic positioning exists
- cross-links reviewed
- resources/quotes captured if required
- tone/depth guidance exists
- Founder approved readiness (`readiness_status: READY_FOR_WRITING_BRIEF` or higher)

## 4. X-Ray fields

Every module may carry the following X-Ray metadata (stored in sidecar X-Ray cards):

```yaml
module_id: "OPN-XXX"
title_en: "..."
title_fr: "..."
movement_id: "MOV-X"
order: "XXX"
status: SCAFFOLDED
xray_status: XRAY_DRAFT

exec_summary_en: "..."
exec_summary_fr: "..."

binder_highlight_en: "..."
binder_highlight_fr: "..."

reader_state_in_en: "..."
reader_state_in_fr: "..."
reader_state_out_en: "..."
reader_state_out_fr: "..."

beats_en:
  - "..."
beats_fr:
  - "..."

key_points_to_develop_en:
  - "..."
key_points_to_develop_fr:
  - "..."

semantic_positioning_en: "..."
semantic_positioning_fr: "..."

transformational_role_en: "..."
transformational_role_fr: "..."

systemic_relevance_en: "..."
systemic_relevance_fr: "..."

cross_module_links:
  - module_id: "OPN-..."
    relation_type: "prepares|depends_on|contrasts_with|deepens|foreshadows|returns_to"
    reason: "..."

resources_to_use:
  - resource_id: null
    title: null
    note: "..."

quotes_to_include:
  - quote: null
    source: null
    status: "PLACEHOLDER|FOUNDER_NOTE|NEEDS_SOURCE|APPROVED"

founder_notes:
  - note: null
    date: null
    status: "OPEN|RESOLVED|INTEGRATED"

orientation_notes_en: "..."
orientation_notes_fr: "..."

tone_guidance_en:
  - "..."
tone_guidance_fr:
  - "..."

depth_guidance_en:
  - "..."
depth_guidance_fr:
  - "..."

what_to_avoid_en:
  - "..."
what_to_avoid_fr:
  - "..."

split_merge_move_notes:
  - "..."

future_writing_brief_seed_en: "..."
future_writing_brief_seed_fr: "..."
future_claude_prompt_seed: "..."

writing_priority: "LOW|MEDIUM|HIGH|CRITICAL"
readiness_status: "XRAY_DRAFT|XRAY_REVIEW|XRAY_APPROVED|READY_FOR_WRITING_BRIEF|READY_FOR_ROUTED_PROSE"
prose_status: "NOT_WRITTEN"
```

## 5. X-Ray views

FCS must support:
- binder view (existing)
- module X-Ray view (sidecar cards)
- part X-Ray reader (OPENING_XRAY_READER_EN.md / FR.md)
- whole-book X-Ray reader (future)
- printable/exportable X-Ray reader (current)

## 6. X-Ray editing actions

The Founder should be able to request:
- split module
- merge modules
- move module
- rename module
- add key point
- add resource
- add quote
- add cross-link
- change tone
- change angle
- deepen / simplify / make concrete
- add transformational emphasis
- generate writing brief
- only later: write module

## 7. Language policy

- System / Backend / Repository: English only
- Book source prose: English first
- Structural reading metadata: English-first + French companion display fields
- Full translated editions: deferred to explicit translation layers

## 8. Sidecar architecture

X-Ray metadata is stored in sidecar files at:

`BOOK/manuscript/{part}/xray_modules/{module_id}_xray.md`

This keeps FCS module frontmatter clean and validate.py compliant.
The sidecar registry is at:

`BOOK/_fcs/registries/opening_xray_registry.yaml`
