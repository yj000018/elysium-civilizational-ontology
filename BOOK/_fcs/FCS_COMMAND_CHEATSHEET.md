# FCS Command Cheatsheet

| Family | Purpose | Typical Command | Preferred Agent | Default Mode | Expected Output |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **View** | Render readable docs | `python scripts/render.py expanded BOOK/manuscript` | Manus | Read-only | Markdown file in `views/` |
| **Structure** | Check node counts | `python scripts/status.py` | Manus | Read-only | Status report in `views/dashboards/` |
| **Write** | Draft new content | Execute Action Request | Claude | Write | Updated node in `manuscript/` |
| **Rewrite** | Edit existing content | Execute Action Request | Claude | Write | Updated node in `manuscript/` |
| **Check** | Validate integrity | `python scripts/validate.py BOOK` | Manus | Read-only | Validation report (exit 0/1) |
| **Resources** | Extract entities | `python scripts/resources.py` | Manus | Write | JSON/MD in `output/` |
| **Output** | Generate graphs | `python scripts/graph.py` | Manus | Write | Mermaid/JSON in `output/graphs/` |
