# Dashboard Model

The Fractal Content Studio (FCS) relies on dynamic dashboards powered by Obsidian Dataview. These dashboards provide real-time visibility into the repository's state, replacing manual folder traversal with query-driven insights.

All dashboards are located in `BOOK/views/dashboards/`.

## 1. Structure Dashboard (`STRUCTURE_DASHBOARD.md`)

This is the primary navigational hub for the Operator. It provides a top-down view of the entire manuscript hierarchy.

**Key Dataview Queries:**
- **Global Progress:** Aggregates the `status` of all nodes (e.g., % SCAFFOLDED, % PLANNED, % READY_FOR_AI).
- **The Hierarchy:** A nested list or table showing `type: part`, `type: foundation`, `type: facet`, and `type: module`, sorted by `parent` and `id`.
- **Metadata Health:** A query highlighting nodes missing `summary` or `reader_promise`.

## 2. Action Dashboard (`ACTION_DASHBOARD.md`)

This dashboard manages the workflow between the Operator and the AI agents. It tracks all files in the `action_requests/` directory.

**Key Dataview Queries:**
- **Queue (Ready for AI):** Lists action requests where `status: READY_FOR_AI`, grouped by `preferred_agent`.
- **In Progress:** Lists action requests currently being executed (`status: IN_PROGRESS`).
- **Blocked/Failed:** Highlights action requests requiring Operator intervention (`status: BLOCKED`).
- **Completed Proposals:** Lists action requests where the AI has generated a proposal (`status: AI_PROPOSAL_READY`), waiting for Operator review.

## 3. Review Dashboard (`REVIEW_DASHBOARD.md`)

This dashboard is used by the Operator to review AI-generated content before locking it into the master layer.

**Key Dataview Queries:**
- **Pending Review:** Lists content nodes where `status: REVIEW_PENDING`.
- **Revision Required:** Lists nodes sent back to the AI for rework (`status: REVISION_REQUIRED`).
- **Recently Locked:** A log of recently finalized nodes (`status: LOCKED`).
- **Quality Warnings:** Queries identifying nodes with `review.review_unit: true` but `review.last_reviewed_by: null`.

## 4. Graph & Resource Dashboard (`GRAPH_RESOURCE_DASHBOARD.md`)

This dashboard tracks the semantic layer, ensuring concepts and resources are properly linked and verified.

**Key Dataview Queries:**
- **Orphan Concepts:** Lists concepts defined in `concepts/` but not referenced in any content node.
- **Unverified Resources:** Lists resources in `resources/` where `status: TO_VERIFY`.
- **High-Value Concepts:** Sorts concepts by the number of inbound links (mentions).
- **Canonical Sources:** Lists resources marked as `status: CANONICAL_SOURCE`.
