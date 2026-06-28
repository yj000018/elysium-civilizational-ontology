# AI Actions Model

The Fractal Content Studio (FCS) standardizes the interactions between the Operator and the AI agents into predefined **Action Families**. This prevents vague prompting and ensures predictable, parseable outputs.

Every action request (defined in `action_requests/`) must specify an action from these families.

## 1. Structure Actions
Used to modify the architectural skeleton of the manuscript. Usually executed by the Chief Architect or Manus Operator.

- `CREATE_NODE`: Scaffolds a new file with correct YAML and adds it to the parent manifest.
- `SPLIT_NODE`: Divides an overly long module into two distinct modules, updating manifests.
- `MERGE_NODES`: Combines two short modules, preserving relations and resources.
- `REORDER_CHILDREN`: Modifies the `manifest.md` sequence based on logical flow.

## 2. Write Actions
Used to generate new prose. Executed by the Claude Writer.

- `WRITE_FIRST_DRAFT`: Generates initial prose based on the `summary` and `reader_promise`.
- `EXPAND_DRAFT`: Adds depth, examples, or theoretical grounding to existing prose.
- `GENERATE_INTRODUCTION`: Writes the index file content for a parent node, synthesizing its children.

## 3. Rewrite Actions
Used to modify existing prose without changing the underlying argument. Executed by the Claude Writer.

- `DENSIFY`: Reduces word count while maintaining information density (removes filler).
- `CLARIFY`: Simplifies complex sentences and improves logical transitions.
- `ALIGN_TO_STYLE_GUIDE`: Ensures the tone matches the ELYSIUM voice (e.g., removing corporate jargon, enhancing architectural tone).

## 4. Check Actions
Used to audit content quality and structural integrity. Executed by the Chief Architect or Claude Reviewer.

- `CHECK_CANONICAL_ALIGNMENT`: Verifies that the prose aligns with the foundational matrices in `02_ONTOLOGY_AND_KNOWLEDGE/`.
- `CHECK_ARGUMENT_FLOW`: Analyzes transitions between modules in a manifest sequence.
- `CHECK_UNSUPPORTED_CLAIMS`: Identifies factual assertions lacking resource citations.

## 5. Resource Actions
Used to manage the semantic layer. Executed by the Manus Operator or Python scripts.

- `EXTRACT_MENTIONED_RESOURCES`: Scans prose for entities and populates the `resources` YAML block.
- `CREATE_RESOURCE_CARDS`: Generates new files in `resources/` for extracted entities.

## 6. Action Execution Protocol

Every action request must define:
1. **Target:** The specific file or directory ID.
2. **Preferred Agent:** Which AI should execute this (e.g., `CLAUDE_WRITER`).
3. **Writeback Mode:** How the result is applied (e.g., `proposal`, `direct_write`).
4. **Context Policy:** What context the AI needs (e.g., "Load parent index and sibling modules").
