---
id: ACT_<% tp.date.now("YYYYMMDD_HHmm") %>
action: EXPAND_DRAFT
target: <% tp.file.cursor(1) %>
preferred_agent: CLAUDE_WRITER
status: DRAFT_ACTION
mode: proposal
priority: medium

context_policy:
  include_target: true
  include_parent_index: true
  include_manifest: true
  include_sibling_summaries: false
  include_canonical_sources: false

instructions:
  goal: Expand this module into a coherent long-form draft.
  target_length: 1200
  style: analytical_narrative
  constraints:
    - preserve canonical facts
    - do not modify architecture unless explicitly requested
    - surface unsupported claims
    - maintain ELYSIUM tone
---
# Action Request: <% tp.file.title %>

## 1. Prompt / Brief
> [!info] Operator Instructions
> Write the specific instructions for the AI here. What exactly needs to be done?

<% tp.file.cursor(2) %>

## 2. AI Proposal Output
> [!warning] AI Instructions
> If `mode: proposal`, write your generated output below this line. Do NOT overwrite the target file directly.

---
*(AI Output will be appended here)*
