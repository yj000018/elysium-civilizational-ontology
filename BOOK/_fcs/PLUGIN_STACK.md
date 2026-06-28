# Plugin Stack & Configuration

The Fractal Content Studio (FCS) relies on a specific stack of Obsidian Community Plugins to transform a static folder of Markdown files into an interactive, data-driven application.

## 1. Core Plugins (Mandatory)

### 1.1 Dataview
**Purpose:** Querying YAML frontmatter to build dynamic dashboards.
**Configuration:**
- Enable JavaScript queries (required for advanced status rollups).
- Enable inline queries.
- **Usage in FCS:** Powers `STRUCTURE_DASHBOARD.md`, `ACTION_DASHBOARD.md`, `REVIEW_DASHBOARD.md`, and `GRAPH_RESOURCE_DASHBOARD.md`.

### 1.2 Templater
**Purpose:** Dynamic file generation with pre-filled YAML and system variables.
**Configuration:**
- Template folder location: `BOOK/_fcs/templates`
- Trigger Templater on new file creation: Enabled
- **Usage in FCS:** Generates `index.md`, `module_template.md`, `concept_template.md`, and `ai_action_request_template.md`. Injects current dates, parent IDs, and default statuses.

### 1.3 QuickAdd
**Purpose:** Command palette macros to streamline workflow.
**Configuration:**
- Create a macro for "New Action Request" that captures the active file's ID and passes it to the Templater script.
- Create macros for "New Module", "New Concept", and "New Resource".
- **Usage in FCS:** The primary interaction mechanism for the Operator. Replaces manual file creation and folder navigation.

## 2. Visual & Structural Plugins (Highly Recommended)

### 2.1 Graph View & Local Graph (Core Plugin)
**Purpose:** Visualizing the semantic ontology.
**Configuration:**
- **Filters:** Exclude `_fcs`, `views`, `output`.
- **Groups:** 
  - Color 1: `type: part` (Red)
  - Color 2: `type: foundation` (Orange)
  - Color 3: `type: facet` (Yellow)
  - Color 4: `type: module` (Blue)
- **Forces:** Increase link force, decrease repel force to cluster related concepts.
- **Usage in FCS:** Validating `parent`, `depends_on`, and `supports` relationships visually before running Python validation scripts.

### 2.2 Canvas (Core Plugin)
**Purpose:** Spatial storyboarding and sense-making.
**Usage in FCS:** 
- Dragging modules onto a canvas to visually arrange the sequence before hardcoding them into a `manifest.md`.
- Creating visual "murder boards" for complex topics (e.g., Energy Transition Vectors) linking concepts, resources, and action requests.

## 3. Watchlist (Future Integration)

These plugins are currently under evaluation for future phases of FCS.

- **Pandoc Plugin:** For local PDF/EPUB generation (currently handled by `render.py` + external Pandoc, but could be integrated into the UI).
- **Longform:** For manuscript compilation (currently handled by `render.py` and `manifest.md`, but Longform offers a native drag-and-drop UI).
- **Quire / Obsidian Publish:** For public deployment of the Graph and rendered views.
