# Graph Model

## Purpose
The Graph Model transforms the hierarchical and relational metadata embedded in the YAML frontmatter into structured graph data. This enables advanced visualization (e.g., Obsidian Graph View, Mermaid diagrams, D3.js), consistency checking, and semantic navigation.

## Scope
The model defines three distinct but interconnected graphs: Content, Concept, and Resource. It is implemented by `scripts/graph.py`.

## The Three Graphs

### 1. Content Graph
**Nodes:** Every folder node (`index.md`) and file node (module) in the manuscript.
**Edges:**
- **Structural:** `child_of` (derived from the `parent` field).
- **Relational:** `depends_on`, `supports`, `contrasts_with`, `echoes` (derived from the `relations` YAML block).
**Purpose:** Visualizing the architectural backbone of the book and identifying logical dependencies.

### 2. Concept Graph
**Nodes:** Unique concepts defined in the `concepts` list of any node, plus any dedicated concept cards in `BOOK/resources/concepts/`.
**Edges:** `mentioned_in` (linking a concept to the manuscript nodes that reference it).
**Purpose:** Tracking recurring themes and ensuring semantic consistency across disparate chapters. Identifying "orphan concepts" (defined but never used) or "overloaded concepts" (used too frequently).

### 3. Resource Graph
**Nodes:** Entities defined in `BOOK/resources/` (people, books, institutions, etc.).
**Edges:** `referenced_by` (linking a resource to manuscript nodes).
**Purpose:** Maintaining a canonical registry of external facts and tracing their usage in the text. This is critical for the "Unsupported Claims" check.

## Execution and Outputs

The `scripts/graph.py` script parses all YAML frontmatter and generates the following artifacts:

**JSON Data (for programmatic consumption):**
- `content_graph.json`
- `concept_graph.json`
- `resource_graph.json`
- `fcs_graph.json` (The unified graph)

**Visualizations (for human inspection):**
- `fcs_graph.mmd` (Mermaid diagram syntax)
- `fcs_graph.md` (Markdown wrapper for the Mermaid diagram)

**Locations:**
- Internal working views: `BOOK/views/graph/`
- Final Master Content Layer: `BOOK/output/graphs/` and `BOOK/output/json/`

## Edge Validation and Null Safety
The graph generation process MUST be robust.
- If a node defines a relation to a target ID that does not exist, the script must log a warning to `GRAPH_WARNINGS.md`.
- It MUST NEVER emit an edge where the target is `null` or an empty string. This will crash downstream visualization tools.
- The `ELYSIUM_ROOT` node is a special case and does not require a parent.

## Do-Not Rules
- **Do NOT** manually edit the JSON or Mermaid files. They are generated artifacts.
- **Do NOT** define graph relations in the body text. They must be in the YAML frontmatter to be parsed by the script.
- **Do NOT** create cyclic dependencies in the `depends_on` or `supports` relations (e.g., A depends on B, B depends on A).
