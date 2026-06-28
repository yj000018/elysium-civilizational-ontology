---
id: FCS_STRUCTURAL_METADATA_LANGUAGE_SCHEMA
title: "FCS Structural Metadata Language Schema"
type: protocol
status: SCAFFOLDED
parent: FCS_PROTOCOLS
created_by: "Manus"
phase: "Phase III-1A-S2X"
---

# FCS Structural Metadata Language Schema

## 1. Language architecture

| Layer | Language | Notes |
|---|---|---|
| System / Backend / Repository | English only | File names, scripts, code, protocols, reports, YAML keys, MPMs |
| Book source prose | English first | Canonical source for all translations |
| Structural reading metadata | English-first + French companion | title_en/title_fr, exec_summary_en/fr, etc. |
| Full translated editions | Deferred | French, Italian, Spanish, German — explicit translation layers only |

## 2. Bilingual field naming convention

All structural metadata fields use `_en` / `_fr` suffix pairs.

Canonical source is always `_en`.
`_fr` is structural display only — not full prose translation.

## 3. X-Ray metadata schema (YAML)

```yaml
# --- Module Identity ---
module_id: "OPN-XXX"
title_en: "..."
title_fr: "..."
movement_id: "MOV-X"
movement_title_en: "..."
movement_title_fr: "..."
order: "XXX"
status: SCAFFOLDED
xray_status: "XRAY_DRAFT|XRAY_REVIEW|XRAY_APPROVED|READY_FOR_WRITING_BRIEF|READY_FOR_ROUTED_PROSE"

# --- Executive Summary ---
exec_summary_en: "..."
exec_summary_fr: "..."

# --- Binder Highlight ---
binder_highlight_en: "..."
binder_highlight_fr: "..."

# --- Reader Transition ---
reader_state_in_en: "..."
reader_state_in_fr: "..."
reader_state_out_en: "..."
reader_state_out_fr: "..."

# --- Beats ---
beats_en:
  - "..."
beats_fr:
  - "..."

# --- Key Points ---
key_points_to_develop_en:
  - "..."
key_points_to_develop_fr:
  - "..."

# --- Semantic Positioning ---
semantic_positioning_en: "..."
semantic_positioning_fr: "..."

# --- Transformational Role ---
transformational_role_en: "..."
transformational_role_fr: "..."

# --- Systemic Relevance ---
systemic_relevance_en: "..."
systemic_relevance_fr: "..."

# --- Cross-Module Links ---
cross_module_links:
  - module_id: "OPN-..."
    relation_type: "prepares|depends_on|contrasts_with|deepens|foreshadows|returns_to"
    reason: "..."

# --- Resources ---
resources_to_use:
  - resource_id: null
    title: null
    note: "..."

# --- Quotes ---
quotes_to_include:
  - quote: null
    source: null
    status: "PLACEHOLDER|FOUNDER_NOTE|NEEDS_SOURCE|APPROVED"

# --- Founder Notes ---
founder_notes:
  - note: null
    date: null
    status: "OPEN|RESOLVED|INTEGRATED"

# --- Tone / Depth / Orientation ---
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

# --- Structural Notes ---
split_merge_move_notes:
  - "..."

# --- Writing Brief Seeds ---
future_writing_brief_seed_en: "..."
future_writing_brief_seed_fr: "..."
future_claude_prompt_seed: "..."

# --- Status ---
writing_priority: "LOW|MEDIUM|HIGH|CRITICAL"
readiness_status: "XRAY_DRAFT|XRAY_REVIEW|XRAY_APPROVED|READY_FOR_WRITING_BRIEF|READY_FOR_ROUTED_PROSE"
prose_status: "NOT_WRITTEN"
```

## 4. Sidecar architecture

X-Ray metadata is stored in sidecar files, not in FCS module frontmatter.

Reason: FCS module frontmatter is validated by `validate.py` against a fixed schema. X-Ray fields would cause validation errors if added directly.

Sidecar location: `BOOK/manuscript/{part}/xray_modules/{module_id}_xray.md`

Registry: `BOOK/_fcs/registries/opening_xray_registry.yaml`

## 5. Allowed FCS module frontmatter fields

The following are the canonical FCS module frontmatter fields (validate.py compliant):

```yaml
id: "..."
title: "..."
type: module
part: "..."
movement_id: "..."
movement_title: "..."
parent: "..."
order: "..."
status: SCAFFOLDED
operational_status: STRUCTURE_DRAFT
fcs_role: manuscript_module
source_status: STRUCTURE_ONLY
prose_status: NOT_WRITTEN
routing_status: NOT_ROUTED
word_count_target: null
word_count_current: 0
created_by: "..."
last_updated_by: "..."
phase: "..."
```

Do not add X-Ray fields to FCS module frontmatter. Use sidecar.
