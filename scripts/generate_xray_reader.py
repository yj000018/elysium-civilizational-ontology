#!/usr/bin/env python3
"""
generate_xray_reader.py
ELYSIUM / FCS — Phase III-1A-S2X-R
Generates enriched Opening X-Ray Reader exports (EN + FR) from X-Ray module cards.
No external libraries required beyond stdlib.
"""

import re
import sys
from pathlib import Path
from datetime import date

REPO_ROOT = Path(__file__).parent.parent
XRAY_DIR = REPO_ROOT / "BOOK/manuscript/01_opening/xray_modules"
BINDER_DIR = REPO_ROOT / "BOOK/_fcs/binder_views"
REGISTRY_PATH = REPO_ROOT / "BOOK/_fcs/registries/opening_xray_registry.yaml"

# Canonical reader transitions (from MPM S2X-R)
TRANSITIONS = {
    "OPN-001": {"en": "Diffuse unease → Civilizational recognition",
                "fr": "Malaise diffus → Reconnaissance civilisationnelle"},
    "OPN-002": {"en": "Many separate crises → One systemic pattern",
                "fr": "Crises séparées → Motif systémique unique"},
    "OPN-003": {"en": "Problem list → Whole-patient diagnosis",
                "fr": "Liste de problèmes → Diagnostic du patient entier"},
    "OPN-004": {"en": "Trust in specialist maps → Awareness of structural blindness",
                "fr": "Confiance dans les cartes spécialisées → Conscience de la cécité structurelle"},
    "OPN-005": {"en": "Local solutions → Awareness of displaced consequences",
                "fr": "Solutions locales → Conscience des conséquences déplacées"},
    "OPN-006": {"en": "Expertise as sufficient → Expertise needing ontology",
                "fr": "Expertise suffisante → Expertise ayant besoin d'ontologie"},
    "OPN-007": {"en": "Machine repair logic → Living-system openness",
                "fr": "Logique de réparation mécanique → Ouverture au système vivant"},
    "OPN-008": {"en": "Living-system openness → Metabolic perception",
                "fr": "Ouverture au système vivant → Perception métabolique"},
    "OPN-009": {"en": "Material metabolism → Full civilizational metabolism",
                "fr": "Métabolisme matériel → Métabolisme civilisationnel complet"},
    "OPN-010": {"en": "Metabolic reframe → Need for civilizational ontology",
                "fr": "Recadrage métabolique → Besoin d'une ontologie civilisationnelle"},
    "OPN-011": {"en": "Need for a map → Multi-scale orientation",
                "fr": "Besoin d'une carte → Orientation multi-échelles"},
    "OPN-012": {"en": "Multi-scale orientation → Seven-Foundation reading path",
                "fr": "Orientation multi-échelles → Chemin de lecture des Sept Fondations"},
    "OPN-013": {"en": "Received map → Committed reader orientation",
                "fr": "Carte reçue → Orientation de lecture engagée"},
}

MOVEMENTS = [
    {"id": "MOV-I", "title_en": "The Malaise of the Present",
     "title_fr": "Le Malaise du Présent",
     "theme_en": "Naming the civilizational unease — from feeling to systemic diagnosis",
     "theme_fr": "Nommer le malaise civilisationnel — du sentiment au diagnostic systémique",
     "modules": ["OPN-001", "OPN-002", "OPN-003"]},
    {"id": "MOV-II", "title_en": "The Failure of Fragmented Maps",
     "title_fr": "L'Échec des Cartes Fragmentées",
     "theme_en": "Why silo-based expertise cannot diagnose or solve the polycrisis",
     "theme_fr": "Pourquoi l'expertise en silos ne peut pas diagnostiquer ni résoudre la polycrise",
     "modules": ["OPN-004", "OPN-005", "OPN-006"]},
    {"id": "MOV-III", "title_en": "Civilization as Metabolism",
     "title_fr": "La Civilisation comme Métabolisme",
     "theme_en": "The metabolic reframe — from machine-repair to living system",
     "theme_fr": "Le recadrage métabolique — de la réparation machine au système vivant",
     "modules": ["OPN-007", "OPN-008", "OPN-009"]},
    {"id": "MOV-IV", "title_en": "The ELYSIUM Map",
     "title_fr": "La Carte d'ELYSIUM",
     "theme_en": "The ontological architecture — 3 Scales, 7 Foundations, reading contract",
     "theme_fr": "L'architecture ontologique — 3 Échelles, 7 Fondations, contrat de lecture",
     "modules": ["OPN-010", "OPN-011", "OPN-012", "OPN-013"]},
]


def extract_section(content, section_header):
    """Extract content between a section header and the next --- or # header."""
    pattern = rf'^{re.escape(section_header)}\s*\n(.*?)(?=\n---\n|\n# |\Z)'
    m = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


def extract_frontmatter(content):
    """Extract YAML frontmatter as dict of key: value strings."""
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, _, v = line.partition(':')
            fields[k.strip()] = v.strip().strip('"')
    return fields


def extract_lang_section(section_text, lang="EN"):
    """Extract the EN or FR subsection from a bilingual section."""
    marker = f"**{lang}:**" if lang == "EN" else f"**FR:**"
    other = "**FR:**" if lang == "EN" else "**EN:**"
    idx = section_text.find(marker)
    if idx == -1:
        return section_text.strip()
    end = section_text.find(other, idx + len(marker))
    if end == -1:
        return section_text[idx + len(marker):].strip()
    return section_text[idx + len(marker):end].strip()


def extract_binder_highlight(content, lang="EN"):
    """Extract binder highlight for given language."""
    section = extract_section(content, "# Binder Highlight")
    marker = f"**{lang}:**"
    idx = section.find(marker)
    if idx == -1:
        # Try blockquote style
        m = re.search(r'^> (.+)', section, re.MULTILINE)
        return m.group(1).strip() if m else section.strip()
    end_markers = ["**EN:**", "**FR:**", "---"]
    end = len(section)
    for em in end_markers:
        pos = section.find(em, idx + len(marker))
        if pos != -1 and pos < end:
            end = pos
    return section[idx + len(marker):end].strip()


def extract_executive_summary(content, lang="EN"):
    """Extract executive summary."""
    section = extract_section(content, "# Executive Summary")
    if not section:
        # Try from Module Identity table
        section = extract_section(content, "# Module Identity")
    return extract_lang_section(section, lang)


def extract_reader_transition(content, module_id, lang="EN"):
    """Extract reader transition, falling back to canonical values."""
    section = extract_section(content, "# Reader Transition")
    # Try table format: | State In | ... | State Out | ... |
    state_in = ""
    state_out = ""
    col = 1 if lang == "EN" else 2
    for line in section.splitlines():
        if "State In" in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) > col + 1:
                state_in = parts[col + 1].strip()
        if "State Out" in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) > col + 1:
                state_out = parts[col + 1].strip()
    if state_in and state_out:
        return f"{state_in} → {state_out}"
    # Fallback to canonical
    return TRANSITIONS.get(module_id, {}).get(lang.lower(), "XRAY_DRAFT")


def read_xray_card(module_id):
    """Read and parse an X-Ray card."""
    path = XRAY_DIR / f"{module_id}_xray.md"
    if not path.exists():
        return None
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


def build_module_block(module_id, content, lang="EN"):
    """Build a full enriched module block for the reader."""
    fm = extract_frontmatter(content)
    title_key = "title_en" if lang == "EN" else "title_fr"
    title = fm.get(title_key, fm.get("title_en", module_id))

    binder = extract_binder_highlight(content, lang)
    exec_sum = extract_lang_section(extract_section(content, "# Executive Summary"), lang)
    if not exec_sum:
        exec_sum = extract_lang_section(extract_section(content, "# Module Identity"), lang)
    transition = extract_reader_transition(content, module_id, lang)
    key_points = extract_lang_section(extract_section(content, "# Key Points to Develop"), lang)
    beats = extract_lang_section(extract_section(content, "# Beats"), lang)
    semantic = extract_lang_section(extract_section(content, "# Semantic Positioning"), lang)
    transform = extract_lang_section(extract_section(content, "# Transformational Role"), lang)
    systemic = extract_lang_section(extract_section(content, "# Systemic Relevance"), lang)
    cross_links = extract_section(content, "# Cross-Module Links")
    resources = extract_section(content, "# Resources to Use")
    quotes = extract_section(content, "# Quotes to Include")
    founder_notes = extract_section(content, "# Founder Notes")
    tone_depth = extract_lang_section(extract_section(content, "# Tone / Depth / Orientation"), lang)
    avoid = extract_lang_section(extract_section(content, "# What to Avoid"), lang)
    split_notes = extract_section(content, "# Split / Merge / Move Notes")
    brief_seed = extract_lang_section(extract_section(content, "# Future Writing Brief Seed"), lang)

    status = fm.get("status", "SCAFFOLDED")
    xray_status = fm.get("xray_status", "XRAY_DRAFT")
    priority = fm.get("writing_priority", "—")
    readiness = fm.get("readiness_status", "XRAY_DRAFT")

    # OPN-012 special: add structural decision block
    opn012_decision = ""
    if module_id == "OPN-012":
        if lang == "EN":
            opn012_decision = "\n**Structural Decision:** FULL REVEAL LIGHT.\n\nReveal the skeleton of the Seven Foundations, not the full body of Part II. The module should name all seven Foundations, explain the ascent logic, and show why they form a reading path. It must not become seven mini-chapters, must not explain the 38 Facets, and must preserve the discovery of Part II.\n"
        else:
            opn012_decision = "\n**Décision structurelle :** RÉVÉLATION COMPLÈTE LÉGÈRE.\n\nRévéler le squelette des Sept Fondations, non le corps complet de la Partie II. Le module doit nommer les sept Fondations, expliquer la logique d'ascension et montrer pourquoi elles forment un chemin de lecture. Il ne doit pas devenir sept mini-chapitres, ne doit pas expliquer les 38 Facettes, et doit préserver la découverte de la Partie II.\n"

    block = f"""### {module_id} — {title}
{opn012_decision}
> {binder}

**Executive Summary:** {exec_sum}

**Reader Transition:** {transition}

**Key Points to Develop**
{key_points}

**Beats**
{beats}

**Semantic Positioning:** {semantic}

**Transformational Role:** {transform}

**Systemic Relevance:** {systemic}

**Cross-Module Links**
{cross_links}

**Resources to Use**
{resources}

**Quotes to Include**
{quotes}

**Founder Notes**
{founder_notes}

**Tone / Depth / Orientation**
{tone_depth}

**What to Avoid**
{avoid}

**Split / Merge / Move Notes**
{split_notes}

**Future Writing Brief Seed**
{brief_seed}

| Status | X-Ray Status | Writing Priority | Readiness |
|---|---|---|---|
| {status} | {xray_status} | {priority} | {readiness} |

---
"""
    return block


def build_reader(lang="EN"):
    """Build the full enriched X-Ray Reader for the given language."""
    today = date.today().isoformat()
    lang_label = "EN" if lang == "EN" else "FR"
    lang_full = "English" if lang == "EN" else "French"

    if lang == "EN":
        header = f"""---
id: OPENING_XRAY_READER_EN
title: "Opening X-Ray Reader — Enriched"
type: xray_reader
language: EN
part: 01_opening
status: XRAY_DRAFT
prose_status: NOT_WRITTEN
opn012_decision: FULL_REVEAL_LIGHT
generated_by: "Manus — Phase III-1A-S2X-R"
generated_date: "{today}"
---

# Opening X-Ray Reader — Enriched (EN)
_ELYSIUM — Civilizational Ontology
Opening Part — Full Structural Architecture View
Phase III-1A-S2X-R | Status: XRAY_DRAFT | Prose: NOT_WRITTEN_

---

## What This Document Is

This is the enriched structural X-Ray of the Opening Part of ELYSIUM.
It is a printable, diagonal, systemic reading of the book's opening architecture.
It is not prose. It is the full architectural skeleton — the map before the journey.

For each module you will find:
- Executive summary
- Binder highlight (one-sentence architectural anchor)
- Reader transition (state in → state out)
- Key points to develop
- Beats (narrative sequence)
- Semantic positioning
- Transformational role
- Systemic relevance
- Cross-module links
- Resources / quote placeholders
- Founder note placeholders
- Tone / depth / orientation guidance
- What to avoid
- Split / merge / move notes
- Future writing brief seed
- Status table

**No prose has been written.** All modules are XRAY_DRAFT.
Prose writing begins only after Founder review and approval, following the yOS routing protocol.

---

## What This Document Is Not

- Not prose
- Not a draft of the book
- Not a final structure (open to Founder review)
- Not a writing brief (writing briefs are generated in Phase III-1A-S3)

---

## How to Read This Document

1. Read the Movement overview to understand the arc
2. Read each module block as a structural card
3. Mark each module: KEEP / REFINE / SPLIT / MERGE / MOVE / ENRICH
4. Add Founder notes, resources, quotes, cross-links in the placeholders
5. Decide on any structural changes before writing begins
6. Do not write prose yet

---

## Movement Overview

| Movement | Modules | Theme |
|---|---|---|
| MOV-I — The Malaise of the Present | OPN-001, OPN-002, OPN-003 | Naming the civilizational unease — from feeling to systemic diagnosis |
| MOV-II — The Failure of Fragmented Maps | OPN-004, OPN-005, OPN-006 | Why silo-based expertise cannot diagnose or solve the polycrisis |
| MOV-III — Civilization as Metabolism | OPN-007, OPN-008, OPN-009 | The metabolic reframe — from machine-repair to living system |
| MOV-IV — The ELYSIUM Map | OPN-010, OPN-011, OPN-012, OPN-013 | The ontological architecture — 3 Scales, 7 Foundations, reading contract |

---

## Full Module Sequence

| Module | Title | Movement | Transition |
|---|---|---|---|
| OPN-001 | The Feeling That Everything Is Coming Apart | MOV-I | Diffuse unease → Civilizational recognition |
| OPN-002 | The Polycrisis Is Not a List of Problems | MOV-I | Many separate crises → One systemic pattern |
| OPN-003 | The Civilizational Patient | MOV-I | Problem list → Whole-patient diagnosis |
| OPN-004 | The Silo Trap | MOV-II | Trust in specialist maps → Awareness of structural blindness |
| OPN-005 | The Displacement Problem | MOV-II | Local solutions → Awareness of displaced consequences |
| OPN-006 | Why Expertise Is Not Enough | MOV-II | Expertise as sufficient → Expertise needing ontology |
| OPN-007 | From Machine to Living System | MOV-III | Machine repair logic → Living-system openness |
| OPN-008 | The Metabolic Pivot | MOV-III | Living-system openness → Metabolic perception |
| OPN-009 | The Five Metabolic Dimensions | MOV-III | Material metabolism → Full civilizational metabolism |
| OPN-010 | The Need for a Civilizational Ontology | MOV-IV | Metabolic reframe → Need for civilizational ontology |
| OPN-011 | The Three Scales | MOV-IV | Need for a map → Multi-scale orientation |
| OPN-012 | The Seven Foundations as a Reading Path | MOV-IV | Multi-scale orientation → Seven-Foundation reading path |
| OPN-013 | The Reading Contract | MOV-IV | Received map → Committed reader orientation |

---

## Critical Pivots

- **OPN-008** = Central metabolic pivot. The book's conceptual engine. If this module fails, the whole metabolic argument fails.
- **OPN-012** = FULL REVEAL LIGHT of the 7 Foundations. Decision resolved: name all 7, show ascent logic, no mini-chapters, preserve Part II discovery.

---

## Review Instructions for Founder

For each module, mark:
- **KEEP** — structure is correct, proceed to writing brief
- **REFINE** — structure needs adjustment before writing
- **SPLIT** — module should be divided into two
- **MERGE** — module should be combined with adjacent module
- **MOVE** — module belongs in a different position
- **ENRICH** — add resources, quotes, cross-links, Founder notes

Add notes, resources, quotes, cross-links in the placeholders.
Do not write prose yet.

---
"""
    else:
        header = f"""---
id: OPENING_XRAY_READER_FR
title: "Lecteur X-Ray Ouverture — Enrichi"
type: xray_reader
language: FR
part: 01_opening
status: XRAY_DRAFT
prose_status: NOT_WRITTEN
opn012_decision: FULL_REVEAL_LIGHT
generated_by: "Manus — Phase III-1A-S2X-R"
generated_date: "{today}"
---

# Lecteur X-Ray Ouverture — Enrichi (FR)
_ELYSIUM — Ontologie Civilisationnelle
Partie Ouverture — Vue Architecture Structurelle Complète
Phase III-1A-S2X-R | Statut : XRAY_DRAFT | Prose : NOT_WRITTEN_

---

## Ce qu'est ce document

C'est le X-Ray structurel enrichi de la Partie Ouverture d'ELYSIUM.
C'est une lecture diagonale, systémique et imprimable de l'architecture d'ouverture du livre.
Ce n'est pas de la prose. C'est le squelette architectural complet — la carte avant le voyage.

Pour chaque module :
- Résumé exécutif
- Highlight binder (ancre architecturale en une phrase)
- Transition lecteur (état entrant → état sortant)
- Points clés à développer
- Beats (séquence narrative)
- Positionnement sémantique
- Rôle transformationnel
- Pertinence systémique
- Liens inter-modules
- Ressources / citations (placeholders)
- Notes du Fondateur (placeholders)
- Guidance ton / profondeur / orientation
- Ce qu'il faut éviter
- Notes split / merge / move
- Graine de brief d'écriture futur
- Tableau de statut

**Aucune prose n'a été écrite.** Tous les modules sont XRAY_DRAFT.
L'écriture commence uniquement après la revue et l'approbation du Fondateur, selon le protocole de routage yOS.

---

## Vue d'ensemble des Mouvements

| Mouvement | Modules | Thème |
|---|---|---|
| MOV-I — Le Malaise du Présent | OPN-001, OPN-002, OPN-003 | Nommer le malaise civilisationnel — du sentiment au diagnostic systémique |
| MOV-II — L'Échec des Cartes Fragmentées | OPN-004, OPN-005, OPN-006 | Pourquoi l'expertise en silos ne peut pas diagnostiquer ni résoudre la polycrise |
| MOV-III — La Civilisation comme Métabolisme | OPN-007, OPN-008, OPN-009 | Le recadrage métabolique — de la réparation machine au système vivant |
| MOV-IV — La Carte d'ELYSIUM | OPN-010, OPN-011, OPN-012, OPN-013 | L'architecture ontologique — 3 Échelles, 7 Fondations, contrat de lecture |

---

## Pivots Critiques

- **OPN-008** = Pivot métabolique central. Le moteur conceptuel du livre.
- **OPN-012** = RÉVÉLATION COMPLÈTE LÉGÈRE des 7 Fondations. Décision résolue : nommer les 7, montrer la logique d'ascension, pas de mini-chapitres, préserver la découverte de la Partie II.

---

## Instructions de revue pour le Fondateur

Pour chaque module, marquer :
- **KEEP** — structure correcte, passer au brief d'écriture
- **REFINE** — ajustement nécessaire avant l'écriture
- **SPLIT** — diviser en deux modules
- **MERGE** — fusionner avec un module adjacent
- **MOVE** — repositionner dans la séquence
- **ENRICH** — ajouter ressources, citations, liens, notes

Ne pas écrire de prose.

---
"""

    body = header

    for mov in MOVEMENTS:
        if lang == "EN":
            body += f"\n## Movement {mov['id']} — {mov['title_en']}\n\n"
            body += f"_{mov['theme_en']}_\n\n---\n\n"
        else:
            body += f"\n## Mouvement {mov['id']} — {mov['title_fr']}\n\n"
            body += f"_{mov['theme_fr']}_\n\n---\n\n"

        for module_id in mov["modules"]:
            content = read_xray_card(module_id)
            if content:
                body += build_module_block(module_id, content, lang)
            else:
                body += f"### {module_id}\n\n_Card not found._\n\n---\n\n"

    return body


def main():
    BINDER_DIR.mkdir(parents=True, exist_ok=True)

    print("Generating enriched Opening X-Ray Reader EN...")
    en_reader = build_reader("EN")
    en_path = BINDER_DIR / "OPENING_XRAY_READER_EN.md"
    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(en_reader)
    print(f"  Written: {en_path} ({len(en_reader.splitlines())} lines)")

    print("Generating enriched Opening X-Ray Reader FR...")
    fr_reader = build_reader("FR")
    fr_path = BINDER_DIR / "OPENING_XRAY_READER_FR.md"
    with open(fr_path, 'w', encoding='utf-8') as f:
        f.write(fr_reader)
    print(f"  Written: {fr_path} ({len(fr_reader.splitlines())} lines)")

    print("Done.")


if __name__ == "__main__":
    main()
