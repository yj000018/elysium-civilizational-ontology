# Action Request Model

## Purpose
The Action Request Model formalizes how tasks are delegated to AI agents within the Fractal Content Studio (FCS). It ensures that every AI operation is intentional, tracked, and subject to Operator review before modifying the canonical corpus.

## Scope
This model defines the lifecycle, structure, and execution policies of AI Action Requests. All action requests live in `BOOK/_fcs/action_requests/`.

## Lifecycle and Statuses

Action Requests move through a strict state machine:

1. `DRAFT_ACTION`: The Operator is currently defining the prompt or parameters.
2. `READY_FOR_AI`: The request is queued for execution by Manus or an API script.
3. `IN_PROGRESS`: Currently being processed.
4. `AI_PROPOSAL_READY`: Execution complete. The output is ready for Operator review.
5. `COMPLETED`: The Operator has approved the proposal and integrated it.
6. `BLOCKED`: Cannot be executed (e.g., missing context, API failure).
7. `ARCHIVED`: Moved out of the active queue.

## Request Structure (YAML Frontmatter)

Every Action Request must define specific YAML fields to ensure programmatic routing:

- `id`: Unique identifier (e.g., `ACT_YYYYMMDD_HHMM`).
- `action`: The specific operation from the AI Actions Model (e.g., `EXPAND_DRAFT`).
- `target`: The ID of the node or directory to act upon (e.g., `F01_01_M01`).
- `preferred_agent`: The assigned role (e.g., `CLAUDE_WRITER`).
- `status`: Current lifecycle state.
- `mode`: Writeback mode (see below).
- `priority`: `high`, `medium`, or `low`.

## Writeback Modes

Writeback modes dictate how the AI agent delivers its output, protecting the master corpus from accidental overwrites.

- `proposal`: **(Default for Prose)** The AI writes the output to a separate proposal file or appends it to the Action Request document itself. The Operator must manually copy/paste or run a script to apply it to the target node.
- `direct_write`: **(Restricted)** The AI overwrites the target file. Used only for structural scaffolding (e.g., `CREATE_NODE`) or when explicitly authorized.
- `review_only`: The AI generates a review document (e.g., `CHECK_ARGUMENT_FLOW`); no source files are modified.

## Context Policy

To prevent hallucinations, Action Requests must explicitly define what context the AI needs. The Operator checks these flags, and the execution script bundles the required files before sending the prompt.

- `include_target`: The file being acted upon.
- `include_parent_index`: The parent folder's `index.md` (crucial for `reader_promise`).
- `include_manifest`: The parent folder's `manifest.md` (crucial for flow).
- `include_sibling_summaries`: Summaries of adjacent modules.
- `include_canonical_sources`: Relevant canonical matrices from `02_ONTOLOGY_AND_KNOWLEDGE/`.

## Do-Not Rules
- **Do NOT** use `direct_write` for prose generation.
- **Do NOT** execute an Action Request if the target node is `status: LOCKED`.
- **Do NOT** execute an Action Request without providing the parent `index.md` context.
