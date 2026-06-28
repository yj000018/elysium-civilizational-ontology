# AI-First Editor Model

## Purpose
The AI-First Editor Model defines the paradigm shift in how the founder interacts with the ELYSIUM corpus. Instead of manually typing long-form prose, the founder acts as an editor-in-chief, directing AI agents to generate, restructure, and refine content.

## Scope
This model covers all interactions between the human operator (founder) and the content corpus, primarily facilitated through Obsidian and the FCS Python scripts.

## Core Workflow
1. **Intention**: The founder identifies a need (e.g., "Expand this module", "Extract resources from this text").
2. **Action Request**: The founder creates an AI Action Request (via an Obsidian QuickAdd command) detailing the goal, constraints, and target node.
3. **Execution**: The assigned AI agent (Claude, ChatGPT, or Manus) processes the request.
4. **Review**: The output is written to a proposal file or directly patched. The founder reviews the changes via Dataview dashboards or diff tools.
5. **Integration**: The founder accepts the changes, updating the node's status.

## Supported Operations
The AI editor can perform:
- **Generative**: Write, expand, develop.
- **Structural**: Restructure, split, merge, move.
- **Analytical**: Review, check consistency, extract resources, generate summaries.
- **Administrative**: Update statuses, render views, compile handoff packages.

## Inputs and Outputs
- **Inputs**: YAML frontmatter (metadata), existing Markdown prose, and structured Action Requests.
- **Outputs**: Proposed Markdown files, patched source files, and updated review statuses.

## Failure Modes
- **Context Loss**: An AI agent hallucinates because it wasn't provided the necessary parent/sibling context. (Mitigated by the `context_policy` in the Action Request).
- **Silent Overwrites**: An AI agent overwrites canonical text without a review step. (Mitigated by the `writeback_policy`).

## Do-Not Rules
- Do NOT encourage the founder to manually rewrite large sections of text. Always use an Action Request.
- Do NOT allow AI agents to bypass the `writeback_policy` (e.g., forcing a direct write when a proposal is required).
