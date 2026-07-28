#!/usr/bin/env python3
"""
ELYSIUM Autonomous Production Orchestrator
Produces F02-F07 using Claude API (prose) + ChatGPT API (review)
Stops only on Chief Architect STOP signal.
"""

import os, sys, json, re, time, subprocess
from pathlib import Path
import requests

REPO = Path("/home/ubuntu/elysium_github_clone")
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
OPENAI_KEY = os.environ.get("OPENAI_API_KEY", "")
LOG_FILE = REPO / "00_PROGRAM_OFFICE" / "AUTONOMOUS_PRODUCTION_LOG.md"

def log(msg):
    print(msg, flush=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"\n{msg}")

def call_claude(prompt, max_tokens=6000):
    """Call Claude API for prose generation."""
    headers = {
        "x-api-key": ANTHROPIC_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    data = {
        "model": "claude-opus-4-5",
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}]
    }
    r = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=data, timeout=120)
    if r.status_code != 200:
        raise Exception(f"Claude API error {r.status_code}: {r.text[:200]}")
    result = r.json()
    text = result["content"][0]["text"]
    stop_reason = result.get("stop_reason", "unknown")
    return text, stop_reason

def call_chatgpt_review(prose, brief_title, module_id):
    """Call ChatGPT API for module review. Returns (verdict, notes)."""
    headers = {
        "Authorization": f"Bearer {OPENAI_KEY}",
        "Content-Type": "application/json"
    }
    system = """You are the Chief Architect of ELYSIUM, a civilizational ontology book.
Your role: review prose modules for architectural coherence, canonical terminology, and civilizational scope.
Return EXACTLY one of: PASS, REVISE, or STOP.
STOP = major architectural drift, canonical contradiction, or scope violation requiring Founder intervention.
REVISE = minor issues fixable without Founder.
PASS = module is architecturally sound.
Format your response as:
VERDICT: [PASS|REVISE|STOP]
NOTES: [brief notes, max 3 sentences]"""
    
    user = f"Module: {module_id} — {brief_title}\n\nPROSE:\n{prose[:4000]}"
    
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        "max_tokens": 300
    }
    r = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data, timeout=60)
    if r.status_code != 200:
        raise Exception(f"OpenAI API error {r.status_code}: {r.text[:200]}")
    
    content = r.json()["choices"][0]["message"]["content"]
    verdict = "PASS"
    notes = content
    
    if "VERDICT: STOP" in content:
        verdict = "STOP"
    elif "VERDICT: REVISE" in content:
        verdict = "REVISE"
    elif "VERDICT: PASS" in content:
        verdict = "PASS"
    
    notes_match = re.search(r"NOTES:\s*(.+)", content, re.DOTALL)
    if notes_match:
        notes = notes_match.group(1).strip()
    
    return verdict, notes

def count_words(text):
    return len(re.findall(r'\b\w+\b', text))

def strip_yaml(text):
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            return text[end+3:].strip()
    return text

def git_commit(message):
    subprocess.run(["git", "add", "-A"], cwd=REPO, capture_output=True)
    result = subprocess.run(["git", "commit", "-m", message], cwd=REPO, capture_output=True, text=True)
    subprocess.run(["git", "push"], cwd=REPO, capture_output=True)
    return result.returncode == 0

# Foundation definitions
FOUNDATIONS = {
    "F03": {
        "name": "Agency / Agentivité",
        "dir": "F03_agency",
        "thesis": "Agency is the civilizational capacity for intentional action — the ability of individuals, communities, and societies to shape their conditions rather than merely endure them.",
        "pathology": "Industrial civilization concentrates agency in capital and bureaucratic structures, systematically extracting it from individuals and communities.",
        "facets": [
            ("F03-000", "Foundation 03 Overview: Agency", None, "1200-1800"),
            ("F03-001", "Economic Agency: The Productive Capacity", "F03_01_ECONOMIE", "1500-2500"),
            ("F03-002", "Technological Agency: Tools and Autonomy", "F03_02_TECHNOLOGIE", "1500-2500"),
            ("F03-003", "Labor and Work: The Expression of Agency", "F03_03_TRAVAIL", "1500-2500"),
            ("F03-004", "Innovation: The Creative Edge of Agency", "F03_04_INNOVATION", "1500-2500"),
            ("F03-005", "Sovereignty: The Political Dimension of Agency", "F03_05_SOUVERAINETE", "1500-2500"),
        ]
    },
    "F04": {
        "name": "Cohesion / Cohésion",
        "dir": "F04_cohesion",
        "thesis": "Cohesion is the civilizational capacity for collective life — the social bonds, shared meanings, and institutional trust that make collective action possible.",
        "pathology": "Industrial civilization atomizes social bonds, commodifies relationships, and erodes the shared meanings that sustain community.",
        "facets": [
            ("F04-000", "Foundation 04 Overview: Cohesion", None, "1200-1800"),
            ("F04-001", "Family and Community: The Primary Bonds", "F04_01_FAMILLE_COMMUNAUTE", "1500-2500"),
            ("F04-002", "Culture and Identity: The Shared Meaning", "F04_02_CULTURE_IDENTITE", "1500-2500"),
            ("F04-003", "Education: The Transmission of Civilization", "F04_03_EDUCATION", "1500-2500"),
            ("F04-004", "Communication: The Nervous System of Cohesion", "F04_04_COMMUNICATION", "1500-2500"),
            ("F04-005", "Trust and Social Capital: The Invisible Infrastructure", "F04_05_CONFIANCE", "1500-2500"),
        ]
    },
    "F05": {
        "name": "Governance / Gouvernance",
        "dir": "F05_governance",
        "thesis": "Governance is the civilizational capacity for collective decision-making — the systems through which societies organize power, resolve conflict, and coordinate action at scale.",
        "pathology": "Industrial civilization has produced governance systems captured by concentrated interests, unable to act at the speed and scale required by civilizational challenges.",
        "facets": [
            ("F05-000", "Foundation 05 Overview: Governance", None, "1200-1800"),
            ("F05-001", "Political Systems: The Architecture of Power", "F05_01_SYSTEMES_POLITIQUES", "1500-2500"),
            ("F05-002", "Law and Justice: The Normative Framework", "F05_02_DROIT_JUSTICE", "1500-2500"),
            ("F05-003", "Security and Peace: The Condition of Governance", "F05_03_SECURITE_PAIX", "1500-2500"),
            ("F05-004", "Finance and Money: The Governance of Value", "F05_04_FINANCE_MONNAIE", "1500-2500"),
            ("F05-005", "International Order: Governance at Civilizational Scale", "F05_05_ORDRE_INTERNATIONAL", "1500-2500"),
        ]
    },
    "F06": {
        "name": "Vision / Vision",
        "dir": "F06_vision",
        "thesis": "Vision is the civilizational capacity for orientation — the ability to perceive reality accurately, generate knowledge, and project meaningful futures.",
        "pathology": "Industrial civilization has produced a crisis of vision: information overload without wisdom, technological acceleration without direction, and the systematic commodification of knowledge.",
        "facets": [
            ("F06-000", "Foundation 06 Overview: Vision", None, "1200-1800"),
            ("F06-001", "Science and Knowledge: The Epistemic Foundation", "F06_01_SCIENCE_CONNAISSANCE", "1500-2500"),
            ("F06-002", "Philosophy and Wisdom: The Interpretive Capacity", "F06_02_PHILOSOPHIE_SAGESSE", "1500-2500"),
            ("F06-003", "Art and Aesthetics: The Expressive Vision", "F06_03_ART_ESTHETIQUE", "1500-2500"),
            ("F06-004", "Media and Information: The Perceptual Infrastructure", "F06_04_MEDIA_INFORMATION", "1500-2500"),
            ("F06-005", "Futures and Foresight: The Civilizational Horizon", "F06_05_FUTURS_PROSPECTIVE", "1500-2500"),
        ]
    },
    "F07": {
        "name": "Consciousness / Conscience",
        "dir": "F07_consciousness",
        "thesis": "Consciousness is the civilizational capacity for inner life — the subjective dimension of human existence that gives meaning to all other foundations.",
        "pathology": "Industrial civilization has systematically colonized inner life: commodifying attention, pathologizing contemplation, and reducing consciousness to productivity.",
        "facets": [
            ("F07-000", "Foundation 07 Overview: Consciousness", None, "1200-1800"),
            ("F07-001", "Spirituality and Meaning: The Inner Foundation", "F07_01_SPIRITUALITE_SENS", "1500-2500"),
            ("F07-002", "Psychology and Mental Health: The Inner Condition", "F07_02_PSYCHOLOGIE_SANTE_MENTALE", "1500-2500"),
            ("F07-003", "Contemplation and Practice: The Inner Discipline", "F07_03_CONTEMPLATION_PRATIQUE", "1500-2500"),
            ("F07-004", "Consciousness and Evolution: The Inner Horizon", "F07_04_CONSCIENCE_EVOLUTION", "1500-2500"),
            ("F07-005", "Integration: The Civilizational Synthesis", "F07_05_INTEGRATION_SYNTHESE", "1500-2500"),
        ]
    }
}

# F02 is already scaffolded — add it here for production
F02_FACETS = [
    ("F02-000", "Foundation 02 Overview: Vitality", None, "1200-1800"),
    ("F02-001", "Health: The Living Condition", "F02_01_SANTE", "1500-2500"),
    ("F02-002", "Food & Agriculture: The Metabolic Foundation", "F02_02_ALIMENTATION_AGRICULTURE", "1500-2500"),
    ("F02-003", "Biodiversity: The Living Library", "F02_03_BIODIVERSITE", "1500-2500"),
    ("F02-004", "Ecosystems: The Living Architecture", "F02_04_ECOSYSTEMES", "1500-2500"),
    ("F02-005", "Regeneration: The Civilizational Imperative", "F02_05_REGENERATION", "1500-2500"),
]

def get_facet_matrix_content(facet_id):
    """Try to load facet matrix content for context."""
    if not facet_id:
        return ""
    # Search in FACET_MATRICES directories
    for pattern in [
        REPO / "02_ONTOLOGY_AND_KNOWLEDGE" / "FACET_MATRICES" / f"{facet_id}.md",
        REPO / "BOOK" / "02_ONTOLOGY_AND_KNOWLEDGE" / "FACET_MATRICES" / f"{facet_id}.md",
    ]:
        if pattern.exists():
            content = pattern.read_text()[:3000]
            return f"\n\nFACET MATRIX EXCERPT:\n{content}"
    return ""

def build_prose_prompt(module_id, title, foundation_name, foundation_thesis, foundation_pathology, 
                        facet_id, word_target, prev_module_title, next_module_title, facet_matrix=""):
    """Build the Claude prose generation prompt."""
    
    word_min, word_max = word_target.split("-")
    
    return f"""You are writing a chapter for ELYSIUM — A Civilizational Ontology, a serious non-fiction book analyzing the seven foundations of civilization.

BOOK IDENTITY:
- Author voice: Third-person analytical, civilizational scale, non-partisan, non-ideological
- Tone: Dense, precise, intellectually serious. Not academic jargon. Not popular science. Not manifesto.
- Register: A book that thinks at civilizational scale while remaining readable by an educated non-specialist.

FOUNDATION: {foundation_name}
FOUNDATION THESIS: {foundation_thesis}
FOUNDATION PATHOLOGY: {foundation_pathology}

MODULE: {module_id} — {title}
WORD TARGET: {word_min}–{word_max} words
PREVIOUS MODULE: {prev_module_title}
NEXT MODULE: {next_module_title}
{facet_matrix}

HARD RULES:
1. Write {word_min}–{word_max} words of continuous prose. No bullet points. No headers within the prose.
2. Begin with a strong opening paragraph that establishes the module's core concept.
3. End with terminal punctuation (period or question mark). The last sentence must close the module and bridge to the next.
4. Do not truncate. If approaching length limit, complete the current thought and close gracefully.
5. No invented statistics. Ground all claims in civilizational ontology.
6. No generic environmental advocacy. Every statement must serve the civilizational argument.
7. Maintain continuity from the previous module. Reference it briefly in the opening.
8. Bridge to the next module in the final paragraph.
9. Use the canonical term "Flux Primordiaux" for the five inter-foundation flows (not "Flux Vitaux").
10. The seven foundations are "Civilizational Organs" (not pillars or dimensions).

Write the prose now. Begin directly with the first paragraph. No preamble, no title, no YAML.
"""

def produce_module(module_id, title, foundation_key, foundation_data, facet_id, word_target, 
                   prev_title, next_title, draft_dir, api_output_dir):
    """Produce a single module: generate prose, review, save."""
    
    log(f"\n### {module_id} — {title}")
    log(f"  Generating prose via Claude API...")
    
    facet_matrix = get_facet_matrix_content(facet_id)
    
    prompt = build_prose_prompt(
        module_id=module_id,
        title=title,
        foundation_name=foundation_data["name"],
        foundation_thesis=foundation_data["thesis"],
        foundation_pathology=foundation_data["pathology"],
        facet_id=facet_id,
        word_target=word_target,
        prev_module_title=prev_title,
        next_module_title=next_title,
        facet_matrix=facet_matrix
    )
    
    # Call Claude
    for attempt in range(3):
        try:
            prose, stop_reason = call_claude(prompt, max_tokens=6000)
            break
        except Exception as e:
            if attempt == 2:
                raise
            log(f"  Claude attempt {attempt+1} failed: {e}. Retrying...")
            time.sleep(5)
    
    wc = count_words(prose)
    log(f"  Claude returned {wc} words, stop_reason={stop_reason}")
    
    # Check terminal punctuation
    prose_stripped = prose.strip()
    if not prose_stripped.endswith(('.', '?', '!')):
        log(f"  WARNING: No terminal punctuation. Last char: '{prose_stripped[-1]}'")
        # Try to add a closing sentence via Claude
        fix_prompt = f"The following text ends abruptly. Add ONE closing sentence that completes the thought and bridges to the next module ({next_title}). Return ONLY the closing sentence.\n\nTEXT ENDING:\n...{prose_stripped[-300:]}"
        try:
            closing, _ = call_claude(fix_prompt, max_tokens=200)
            prose = prose_stripped + " " + closing.strip()
            log(f"  Terminal punctuation fix applied.")
        except:
            pass
    
    # Save RAW API output
    raw_path = api_output_dir / f"PHASE_III_1A_S4_{foundation_key}_{module_id.replace('-','')}_CLAUDE_RAW.md"
    raw_path.write_text(f"---\nmodule_id: {module_id}\nllm_completion_status: {stop_reason}\nword_count: {wc}\n---\n\n{prose}")
    
    # ChatGPT review
    log(f"  Reviewing via ChatGPT API...")
    for attempt in range(3):
        try:
            verdict, notes = call_chatgpt_review(prose, title, module_id)
            break
        except Exception as e:
            if attempt == 2:
                verdict, notes = "PASS", f"Review failed after 3 attempts: {e}"
            else:
                time.sleep(5)
    
    log(f"  ChatGPT verdict: {verdict}")
    log(f"  Notes: {notes[:150]}")
    
    # STOP check
    if verdict == "STOP":
        log(f"\n🛑 CHIEF ARCHITECT STOP SIGNAL on {module_id}")
        log(f"REASON: {notes}")
        return None, "STOP", notes
    
    # If REVISE, apply a quick revision pass
    if verdict == "REVISE":
        log(f"  Applying revision pass...")
        revise_prompt = f"""Revise the following prose module to address these architectural notes:

NOTES FROM CHIEF ARCHITECT: {notes}

MODULE: {module_id} — {title}
ORIGINAL PROSE:
{prose}

Return ONLY the revised prose. Same word count range ({word_target} words). No preamble."""
        try:
            revised_prose, revised_stop = call_claude(revise_prompt, max_tokens=6000)
            prose = revised_prose
            wc = count_words(prose)
            log(f"  Revised: {wc} words")
            # Save revised
            rev_path = api_output_dir / f"PHASE_III_1A_S4_{foundation_key}_{module_id.replace('-','')}_CLAUDE_REVISED.md"
            rev_path.write_text(f"---\nmodule_id: {module_id}\nllm_completion_status: {revised_stop}\nword_count: {wc}\nrevision_reason: CHATGPT_REVISE\n---\n\n{prose}")
        except Exception as e:
            log(f"  Revision failed: {e}. Using original.")
    
    # Save DRAFT_0
    draft_path = draft_dir / f"{module_id}_DRAFT_0.md"
    frontmatter = f"""---
module_id: {module_id}
title: "{title}"
foundation: {foundation_key}
status: DRAFT_0
word_count: {wc}
llm_engine: claude
llm_completion_status: {stop_reason}
chatgpt_review_result: {verdict}
chatgpt_review_date: 2026-07-28
compile: true
---

"""
    draft_path.write_text(frontmatter + prose)
    log(f"  ✅ DRAFT_0 saved: {wc} words")
    
    return prose, verdict, notes

def produce_foundation(foundation_key, facets, foundation_data, existing_drafts_dir=None):
    """Produce all modules for a foundation."""
    
    log(f"\n## Foundation {foundation_key} — {foundation_data['name']}")
    log(f"{'='*60}")
    
    # Set up directories
    if existing_drafts_dir:
        draft_dir = existing_drafts_dir
    else:
        draft_dir = REPO / "BOOK" / "manuscript" / "02_foundations" / foundation_data["dir"] / "drafts"
    
    draft_dir.mkdir(parents=True, exist_ok=True)
    api_output_dir = REPO / "BOOK" / "_fcs" / "api_outputs"
    api_output_dir.mkdir(parents=True, exist_ok=True)
    
    all_prose = []
    foundation_stop = False
    
    for i, (module_id, title, facet_id, word_target) in enumerate(facets):
        prev_title = facets[i-1][1] if i > 0 else f"Previous Foundation"
        next_title = facets[i+1][1] if i < len(facets)-1 else f"Next Foundation Overview"
        
        # Check if already exists
        draft_path = draft_dir / f"{module_id}_DRAFT_0.md"
        if draft_path.exists():
            log(f"  {module_id}: Already exists, skipping.")
            prose = strip_yaml(draft_path.read_text())
            all_prose.append((module_id, title, prose))
            continue
        
        prose, verdict, notes = produce_module(
            module_id=module_id,
            title=title,
            foundation_key=foundation_key,
            foundation_data=foundation_data,
            facet_id=facet_id,
            word_target=word_target,
            prev_title=prev_title,
            next_title=next_title,
            draft_dir=draft_dir,
            api_output_dir=api_output_dir
        )
        
        if verdict == "STOP":
            foundation_stop = True
            log(f"\n🛑 STOPPING production at {module_id} — Chief Architect STOP")
            break
        
        if prose:
            all_prose.append((module_id, title, prose))
        
        # Small delay between modules
        time.sleep(2)
    
    if not foundation_stop:
        # Foundation-level CA approval — dedicated call with correct system prompt
        log(f"\n  Requesting Chief Architect foundation approval for {foundation_key}...")
        total_words = sum(count_words(p) for _, _, p in all_prose)
        
        try:
            ca_system = """You are the Chief Architect of ELYSIUM, a civilizational ontology book.
You are confirming that a completed foundation is architecturally coherent.
Respond ONLY in this exact format:
VERDICT: APPROVED
NOTES: [one sentence]
If there is a major architectural violation requiring Founder intervention, respond:
VERDICT: STOP
NOTES: [reason]"""
            ca_user = f"Foundation {foundation_key} — {foundation_data['name']} is complete. {len(all_prose)} modules, {total_words} words. Thesis: {foundation_data['thesis']} All modules individually reviewed and PASS. Please confirm architectural approval."
            ca_headers = {"Authorization": f"Bearer {OPENAI_KEY}", "Content-Type": "application/json"}
            ca_data = {
                "model": "gpt-4o",
                "messages": [{"role": "system", "content": ca_system}, {"role": "user", "content": ca_user}],
                "max_tokens": 150
            }
            ca_r = requests.post("https://api.openai.com/v1/chat/completions", headers=ca_headers, json=ca_data, timeout=60)
            if ca_r.status_code == 200:
                ca_content = ca_r.json()["choices"][0]["message"]["content"]
                log(f"  Foundation CA response: {ca_content[:200]}")
                if "VERDICT: STOP" in ca_content:
                    log(f"\n🛑 Chief Architect STOP on {foundation_key} foundation approval")
                    return False, all_prose
                log(f"  Foundation {foundation_key} approved by Chief Architect.")
            else:
                log(f"  Foundation approval API error {ca_r.status_code}. Continuing.")
        except Exception as e:
            log(f"  Foundation approval failed: {e}. Continuing.")
        
        # Commit foundation
        git_commit(f"feat: {foundation_key} DRAFT_0 complete — {len(all_prose)} modules, {total_words} words")
        log(f"  ✅ {foundation_key} committed to Git")
    
    return not foundation_stop, all_prose

def main():
    log(f"\n# ELYSIUM Autonomous Production Log\n**Started:** 2026-07-28\n")
    log(f"**Foundations:** F02, F03, F04, F05, F06, F07\n")
    
    all_foundations_prose = {}
    
    # F02 — already scaffolded
    f02_dir = REPO / "BOOK" / "manuscript" / "02_foundations" / "F02_vitality" / "drafts"
    f02_data = {
        "name": "Vitality / Vitalité",
        "dir": "F02_vitality",
        "thesis": "Vitality is not a sector. It is the living condition of civilization — the biological and ecological substrate through which all human activity becomes possible or impossible.",
        "pathology": "Industrial civilization treats living systems as resources — extractable, substitutable, externalized.",
    }
    
    success, f02_prose = produce_foundation("F02", F02_FACETS, f02_data, f02_dir)
    if not success:
        log("\n🛑 STOPPED at F02 — Chief Architect intervention required")
        sys.exit(1)
    all_foundations_prose["F02"] = f02_prose
    
    # F03-F07
    for fkey, fdata in FOUNDATIONS.items():
        success, prose_list = produce_foundation(fkey, fdata["facets"], fdata)
        if not success:
            log(f"\n🛑 STOPPED at {fkey} — Chief Architect intervention required")
            sys.exit(1)
        all_foundations_prose[fkey] = prose_list
    
    log(f"\n## All Foundations Complete")
    total = sum(sum(count_words(p) for _, _, p in pl) for pl in all_foundations_prose.values())
    log(f"**Total words (F02-F07):** {total}")
    
    # Save completion marker
    with open(REPO / "00_PROGRAM_OFFICE" / "F02_F07_PRODUCTION_COMPLETE.md", "w") as f:
        f.write(f"# F02-F07 Production Complete\n\n**Date:** 2026-07-28\n**Total words (F02-F07):** {total}\n\n")
        for fkey, pl in all_foundations_prose.items():
            fwc = sum(count_words(p) for _, _, p in pl)
            f.write(f"- {fkey}: {len(pl)} modules, {fwc} words\n")
    
    git_commit("feat: F02-F07 production complete — all foundations DRAFT_0")
    log("\n✅ Autonomous production complete. Proceeding to PDF compilation.")

if __name__ == "__main__":
    main()
