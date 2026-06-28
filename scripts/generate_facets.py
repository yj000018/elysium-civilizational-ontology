import os
import yaml

facets = [
    ("F01_01", "energy", "Energy", "F01_material_base", "F01_material_base/F01_01_energy"),
    ("F01_02", "water", "Water", "F01_material_base", "F01_material_base/F01_02_water"),
    ("F01_03", "habitat", "Habitat", "F01_material_base", "F01_material_base/F01_03_habitat"),
    ("F01_04", "infrastructure", "Infrastructure", "F01_material_base", "F01_material_base/F01_04_infrastructure"),
    ("F01_05", "mobility", "Mobility", "F01_material_base", "F01_material_base/F01_05_mobility"),
    ("F01_06", "materials", "Materials", "F01_material_base", "F01_material_base/F01_06_materials"),

    ("F02_01", "health", "Health", "F02_vitality", "F02_vitality/F02_01_health"),
    ("F02_02", "food_agriculture", "Food & Agriculture", "F02_vitality", "F02_vitality/F02_02_food_agriculture"),
    ("F02_03", "biodiversity", "Biodiversity", "F02_vitality", "F02_vitality/F02_03_biodiversity"),
    ("F02_04", "ecosystems", "Ecosystems", "F02_vitality", "F02_vitality/F02_04_ecosystems"),
    ("F02_05", "regeneration", "Regeneration", "F02_vitality", "F02_vitality/F02_05_regeneration"),

    ("F03_01", "economy", "Economy", "F03_agency", "F03_agency/F03_01_economy"),
    ("F03_02", "work", "Work", "F03_agency", "F03_agency/F03_02_work"),
    ("F03_03", "finance", "Finance", "F03_agency", "F03_agency/F03_03_finance"),
    ("F03_04", "entrepreneurship", "Entrepreneurship", "F03_agency", "F03_agency/F03_04_entrepreneurship"),
    ("F03_05", "innovation", "Innovation", "F03_agency", "F03_agency/F03_05_innovation"),
    ("F03_06", "production", "Production", "F03_agency", "F03_agency/F03_06_production"),

    ("F04_01", "community", "Community", "F04_cohesion", "F04_cohesion/F04_01_community"),
    ("F04_02", "relationships", "Relationships", "F04_cohesion", "F04_cohesion/F04_02_relationships"),
    ("F04_03", "culture", "Culture", "F04_cohesion", "F04_cohesion/F04_03_culture"),
    ("F04_04", "art", "Art", "F04_cohesion", "F04_cohesion/F04_04_art"),
    ("F04_05", "media", "Media", "F04_cohesion", "F04_cohesion/F04_05_media"),
    ("F04_06", "belonging_identity", "Belonging & Identity", "F04_cohesion", "F04_cohesion/F04_06_belonging_identity"),

    ("F05_01", "law_justice", "Law & Justice", "F05_governance", "F05_governance/F05_01_law_justice"),
    ("F05_02", "democracy", "Democracy", "F05_governance", "F05_governance/F05_02_democracy"),
    ("F05_03", "institutions", "Institutions", "F05_governance", "F05_governance/F05_03_institutions"),
    ("F05_04", "security", "Security", "F05_governance", "F05_governance/F05_04_security"),
    ("F05_05", "communication", "Communication", "F05_governance", "F05_governance/F05_05_communication"),

    ("F06_01", "education", "Education", "F06_vision", "F06_vision/F06_01_education"),
    ("F06_02", "science", "Science", "F06_vision", "F06_vision/F06_02_science"),
    ("F06_03", "foresight", "Foresight", "F06_vision", "F06_vision/F06_03_foresight"),
    ("F06_04", "systems_thinking", "Systems Thinking", "F06_vision", "F06_vision/F06_04_systems_thinking"),
    ("F06_05", "technology", "Technology", "F06_vision", "F06_vision/F06_05_technology"),

    ("F07_01", "ethics", "Ethics", "F07_consciousness", "F07_consciousness/F07_01_ethics"),
    ("F07_02", "spirituality", "Spirituality", "F07_consciousness", "F07_consciousness/F07_02_spirituality"),
    ("F07_03", "meaning_purpose", "Meaning & Purpose", "F07_consciousness", "F07_consciousness/F07_03_meaning_purpose"),
    ("F07_04", "worldview", "Worldview", "F07_consciousness", "F07_consciousness/F07_04_worldview"),
    ("F07_05", "civilizational_direction", "Civilizational Direction", "F07_consciousness", "F07_consciousness/F07_05_civilizational_direction"),
]

base_dir = "/home/ubuntu/elysium-civilizational-ontology/BOOK/manuscript/02_foundations"

for f_id, f_code, f_name, parent, path in facets:
    full_path = os.path.join(base_dir, path)
    os.makedirs(full_path, exist_ok=True)
    
    # Generate index.md
    index_path = os.path.join(full_path, "index.md")
    
    # Don't overwrite if it exists and has content (we'll manually update F01_01 later)
    if not os.path.exists(index_path) or os.path.getsize(index_path) < 100:
        content = f"""---
id: {f_id}
title: {f_name}
type: facet
status: SCAFFOLDED
parent: {parent}
children_mode: manifest
summary: Placeholder for {f_name} facet.
reader_promise: ""
concepts: []
resources:
  people: []
  institutions: []
relations:
  depends_on: []
  supports: []
  contrasts_with: []
  echoes: []
graph:
  layer: manuscript
  cluster: facets
  node_type: facet
  weight: 3
  show_in_public_graph: true
review:
  review_unit: false
  last_reviewed_by: null
  review_notes: []
---

# {f_name}

## Function in the Book
TBD

## Intended Argument
TBD

## Drafting Strategy
TBD
"""
        with open(index_path, "w") as f:
            f.write(content)
            
    # Generate manifest.md
    manifest_path = os.path.join(full_path, "manifest.md")
    if not os.path.exists(manifest_path):
        content = f"""# Manifest — {f_name}

## Include

## Optional / Parked

## Exclude
"""
        with open(manifest_path, "w") as f:
            f.write(content)

print(f"Scaffolded {len(facets)} facets.")
