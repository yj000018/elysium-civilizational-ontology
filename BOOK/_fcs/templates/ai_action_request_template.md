---
action_id: ACT_YYYYMMDD_0001
action: EXPAND_DRAFT
target: BOOK/manuscript/path/to/target.md
preferred_agent: CLAUDE_WRITER
fallback_agent: CHATGPT_CHIEF_ARCHITECT
status: READY_FOR_AI
mode: proposal
requested_by: founder
priority: medium

context_policy:
  include_target: true
  include_parent_index: true
  include_manifest: true
  include_sibling_summaries: true
  include_canonical_sources: true
  include_related_resources: true
  include_graph_neighborhood: false

instructions:
  goal: Expand this module into a coherent long-form draft.
  target_length: 1200
  style: analytical_narrative
  constraints:
    - preserve canonical facts
    - do not modify architecture unless explicitly requested
    - surface unsupported claims
    - maintain ELYSIUM tone

output_policy:
  write_to: proposal_file
  do_not_overwrite_source: true
  status_after: AI_PROPOSAL_READY

writeback_policy:
  default: proposal
  requires_review: true
---
