#!/usr/bin/env python3
"""
FCS Graph Script
Generates content, concept, and resource graphs from YAML frontmatter.

Usage:
    python scripts/graph.py
"""

import sys
import os
import re
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BOOK = REPO_ROOT / "BOOK"


def extract_frontmatter(filepath):
    """Extract YAML frontmatter as dict (simple parser)."""
    content = filepath.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    fm_text = content[3:end]
    fields = {}
    current_key = None
    current_list = None
    for line in fm_text.splitlines():
        # Simple key: value
        m = re.match(r"^(\w[\w_]*):\s*(.+)$", line)
        if m and not line.startswith("  "):
            current_key = m.group(1)
            val = m.group(2).strip()
            if val == "[]":
                fields[current_key] = []
            elif val.startswith("["):
                fields[current_key] = []
            else:
                fields[current_key] = val
            current_list = None
            continue
        # List item
        m2 = re.match(r"^\s+- (.+)$", line)
        if m2 and current_key:
            if current_key not in fields or not isinstance(fields.get(current_key), list):
                fields[current_key] = []
            fields[current_key].append(m2.group(1).strip())
            continue
        # Nested key
        m3 = re.match(r"^(\w[\w_]*):\s*$", line)
        if m3:
            current_key = m3.group(1)
            fields[current_key] = {}
    return fields


def build_content_graph():
    """Build content graph from manuscript nodes."""
    nodes = []
    edges = []
    for md in (BOOK / "manuscript").rglob("*.md"):
        if md.name in ("manifest.md",):
            continue
        fields = extract_frontmatter(md)
        if not fields.get("id"):
            continue
        node = {
            "id": fields["id"],
            "title": fields.get("title", ""),
            "type": fields.get("type", ""),
            "status": fields.get("status", ""),
            "path": str(md.relative_to(REPO_ROOT)),
        }
        nodes.append(node)
        # Parent edge
        if fields.get("parent"):
            edges.append({"source": fields["id"], "target": fields["parent"], "type": "child_of"})
        # Relations
        if isinstance(fields.get("depends_on"), list):
            for dep in fields["depends_on"]:
                edges.append({"source": fields["id"], "target": dep, "type": "depends_on"})
        if isinstance(fields.get("supports"), list):
            for sup in fields["supports"]:
                edges.append({"source": fields["id"], "target": sup, "type": "supports"})
    return {"nodes": nodes, "edges": edges}


def build_concept_graph():
    """Build concept graph from concepts fields."""
    concepts = set()
    mentions = []
    for md in BOOK.rglob("*.md"):
        fields = extract_frontmatter(md)
        if isinstance(fields.get("concepts"), list):
            for c in fields["concepts"]:
                concepts.add(c)
                mentions.append({"concept": c, "source": fields.get("id", str(md.relative_to(REPO_ROOT)))})
    nodes = [{"id": c, "type": "concept"} for c in sorted(concepts)]
    return {"nodes": nodes, "mentions": mentions}


def build_resource_graph():
    """Build resource graph from resource files."""
    nodes = []
    for md in (BOOK / "resources").rglob("*.md"):
        fields = extract_frontmatter(md)
        if fields.get("id"):
            nodes.append({
                "id": fields["id"],
                "title": fields.get("title", ""),
                "type": fields.get("type", ""),
                "status": fields.get("status", ""),
            })
    return {"nodes": nodes, "edges": []}


def generate_mermaid(content_graph):
    """Generate Mermaid diagram from content graph."""
    lines = ["graph TD"]
    for node in content_graph["nodes"]:
        safe_id = node["id"].replace(" ", "_")
        lines.append(f'    {safe_id}["{node["title"]}"]')
    for edge in content_graph["edges"]:
        src = edge["source"].replace(" ", "_")
        tgt = edge["target"].replace(" ", "_")
        label = edge["type"]
        lines.append(f"    {src} -->|{label}| {tgt}")
    return "\n".join(lines)


def main():
    print("=" * 60)
    print("FCS GRAPH GENERATION")
    print("=" * 60)

    content_graph = build_content_graph()
    concept_graph = build_concept_graph()
    resource_graph = build_resource_graph()

    # Write to views/graph/
    graph_dir = BOOK / "views" / "graph"
    graph_dir.mkdir(parents=True, exist_ok=True)

    (graph_dir / "content_graph.json").write_text(json.dumps(content_graph, indent=2), encoding="utf-8")
    (graph_dir / "concept_graph.json").write_text(json.dumps(concept_graph, indent=2), encoding="utf-8")
    (graph_dir / "resource_graph.json").write_text(json.dumps(resource_graph, indent=2), encoding="utf-8")

    fcs_graph = {
        "content": content_graph,
        "concepts": concept_graph,
        "resources": resource_graph,
    }
    (graph_dir / "fcs_graph.json").write_text(json.dumps(fcs_graph, indent=2), encoding="utf-8")

    mermaid = generate_mermaid(content_graph)
    (graph_dir / "fcs_graph.mmd").write_text(mermaid, encoding="utf-8")
    (graph_dir / "fcs_graph.md").write_text(f"# FCS Graph\n\n```mermaid\n{mermaid}\n```\n", encoding="utf-8")

    # Adjacency
    adj_lines = ["# FCS Adjacency Map\n"]
    for edge in content_graph["edges"]:
        adj_lines.append(f"- {edge['source']} --[{edge['type']}]--> {edge['target']}")
    (graph_dir / "fcs_adjacency.md").write_text("\n".join(adj_lines), encoding="utf-8")

    # Readme
    readme = "# FCS Graph Readme\n\nThis directory contains generated graph outputs.\n"
    readme += "- `content_graph.json`: Manuscript structure graph.\n"
    readme += "- `concept_graph.json`: Concept mentions graph.\n"
    readme += "- `resource_graph.json`: Resource entities graph.\n"
    readme += "- `fcs_graph.json`: Combined graph.\n"
    readme += "- `fcs_graph.mmd`: Mermaid diagram.\n"
    (graph_dir / "fcs_graph_readme.md").write_text(readme, encoding="utf-8")

    # Write to output/
    out_graphs = BOOK / "output" / "graphs"
    out_graphs.mkdir(parents=True, exist_ok=True)
    (out_graphs / "content_graph.json").write_text(json.dumps(content_graph, indent=2), encoding="utf-8")
    (out_graphs / "concept_graph.json").write_text(json.dumps(concept_graph, indent=2), encoding="utf-8")
    (out_graphs / "resource_graph.json").write_text(json.dumps(resource_graph, indent=2), encoding="utf-8")
    (out_graphs / "graph.mmd").write_text(mermaid, encoding="utf-8")

    out_json = BOOK / "output" / "json"
    out_json.mkdir(parents=True, exist_ok=True)

    # Navigation JSON
    nav = {"nodes": [{"id": n["id"], "title": n["title"], "type": n["type"], "path": n.get("path", "")} for n in content_graph["nodes"]]}
    (out_json / "navigation.json").write_text(json.dumps(nav, indent=2), encoding="utf-8")

    print(f"\nContent graph: {len(content_graph['nodes'])} nodes, {len(content_graph['edges'])} edges")
    print(f"Concept graph: {len(concept_graph['nodes'])} concepts")
    print(f"Resource graph: {len(resource_graph['nodes'])} resources")
    print(f"\nOutputs written to: BOOK/views/graph/ and BOOK/output/graphs/")


if __name__ == "__main__":
    main()
