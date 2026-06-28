# FCS Operational Quickstart

## 1. Inspect Structure
Check the current state of the manuscript nodes and their metadata.
`python scripts/status.py`

## 2. Render Views
Generate readable Markdown versions of the manuscript.
`python scripts/render.py expanded BOOK/manuscript` (Includes child content)
`python scripts/render.py review BOOK/manuscript` (Includes review notes)
`python scripts/render.py master BOOK/manuscript` (Full corpus output)

## 3. Run Validation
Ensure all IDs, parents, manifests, and relations are correct.
`python scripts/validate.py BOOK`

## 4. Generate Graphs
Update the Mermaid and JSON graphs for content, concepts, and resources.
`python scripts/graph.py`

## 5. Extract Resources
Index all resources and concepts mentioned in the manuscript.
`python scripts/resources.py`

## 6. Action Requests
Action requests live in `BOOK/_fcs/action_requests/active/`.
To execute one:
1. Read the `.md` file.
2. Follow the instructions (e.g., call Claude API).
3. Write the output to the `target` node.
4. Move the request to `done/`.

## 7. Obsidian Dashboards
Open the repository in Obsidian. Ensure Dataview is installed. View the dashboards in `BOOK/views/dashboards/`.

## 8. Routing Work
- **Claude:** For drafting prose, deep synthesis, and creative writing.
- **ChatGPT:** For architectural review, session management, and strategic guidance.
- **Manus:** For script execution, file manipulation, API orchestration, and validation.
