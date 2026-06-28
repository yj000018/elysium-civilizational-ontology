---
id: ELYSIUM_SessionLifecycle_ContextPack_InterLLM_Restatement
title: "ELYSIUM — Technical Restatement: Session Lifecycle, Context Packs & Inter-LLM Orchestration"
date: "2026-06-28"
status: AUDIT_COMPLETE
type: technical_restitution
---

# ELYSIUM — Technical Restatement: Session Lifecycle, Context Packs & Inter-LLM Orchestration

## 1. Executive Summary

This document audits the current state of inter-LLM orchestration within the ELYSIUM production system. It identifies what has been implemented, what exists conceptually but lacks technical enforcement, and what remains to be built to achieve full integration into yOS / FCS Program Management Mode.

**Current State (The 80%):**
- **IMPLEMENTED:** Manus successfully acts as an autonomous API orchestrator (calling Claude for prose and ChatGPT for review) via Python scripts (`call_claude_prose.py`, `call_chatgpt_review.py`).
- **IMPLEMENTED:** Output validation and completion guards are active (`llm_output_guard.py`).
- **IMPLEMENTED:** Governance and LLM routing rules are codified (`FCS_QA_QC_GOVERNANCE_PROTOCOL.md`, `FCS_MULTI_LLM_ORCHESTRATION_PROTOCOL.md`, `LLM_MATRIX.md`).
- **IMPLEMENTED:** Context packs are heavily used and manually/script-generated for individual module runs.

**Missing State (The 20%):**
- **MISSING:** Formal session lifecycle management (decision criteria for opening/closing ChatGPT sessions).
- **MISSING:** Persistent conversation chaining (`previous_response_id` passing) in the Chief Architect API.
- **MISSING:** A structured Message Bus and Decision Ledger for inter-LLM communication history.
- **MISSING:** Automated context pack generation pipelines (`context_pack_generator.py`).
- **MISSING:** The overarching Program Management Mode to orchestrate these components autonomously at the phase/gate level.

---

## 2. Existing Inter-LLM Architecture

The current architecture relies on file-system state and API calls rather than conversational memory.

*   **Manus as orchestrator / dispatcher:** Manus does not write prose. It reads the repo state, prepares payloads, executes Python scripts to call APIs, processes the responses, updates YAML frontmatter, and commits to Git.
*   **Claude API as prose engine:** Used exclusively for generating and revising prose. It operates statelessly (one-shot or revised-shot) using a Context Pack.
*   **ChatGPT API as reviewer / QA / Chief Architect advisor:** Used to review Claude's prose against Writing Briefs. Currently implemented as a stateless API call (`call_chatgpt_review.py`), returning structured PASS/REVISE decisions.
*   **Context pack generation:** Context packs are markdown files containing the writing brief, ontology rules, phase context, and task instructions. Currently, they are generated ad-hoc or via specialized scripts per phase, rather than a universal generator.
*   **`previous_response_id` / persistent conversation chaining:** **MISSING.** Currently, every API call is stateless. There is no technical implementation of conversation threading in the Chief Architect API scripts.
*   **Message passing between Manus and LLMs:** Implemented via file I/O. Manus writes a prompt/context file, passes it to the API script, captures the markdown output, and saves it to `BOOK/_fcs/api_outputs/`.
*   **Git persistence:** All prompts (context packs), raw outputs, review decisions, and final drafts are saved as Markdown files with YAML metadata and committed to Git, making the repository the absolute source of truth.

---

## 3. Session Lifecycle Doctrine

The doctrine for ChatGPT API sessions (Chief Architect) dictates that memory should be explicit, auditable, and bounded.

*   **Persistent session is useful but not infinite memory:** Long context windows degrade reasoning and lead to "lost in the middle" phenomena. Sessions must be bounded by phase or task.
*   **`previous_response_id` is a temporary work thread, not canonical memory:** Threading is for immediate back-and-forth refinement (e.g., debating an architectural split). Once a decision is made, it must be committed to the repo.
*   **Repo is the source of truth:** The file system (YAML registries, Markdown drafts, Protocol files) holds the canonical state, not the LLM's conversational history.
*   **Context packs are generated at task time:** Instead of relying on a model remembering a rule from 50 prompts ago, the exact rules, state, and briefs needed for the *current* task are compiled into a fresh Context Pack.
*   **New session triggers:** A new session should be opened when history is too long, the theme changes, a phase boundary is crossed, or QA risks increase (to clear the context window of previous errors).

---

## 4. Criteria for Starting a New Session

Precise decision criteria for rotating / splitting to a new ChatGPT API session:

| Criterion | Status | Description |
| :--- | :--- | :--- |
| **Phase or gate change** | **CONCEPTUAL** | Moving from F01 to F02, or from Writing to Review phase. |
| **Task theme change** | **CONCEPTUAL** | Shifting from Material Existence (F01) to Vitality (F02). |
| **Long conversation / token bloat** | **CONCEPTUAL** | Reaching a predefined token threshold (e.g., >30k tokens in thread). |
| **Context window pressure** | **CONCEPTUAL** | Approaching model limits where reasoning degrades. |
| **Rising cost** | **CONCEPTUAL** | Preventing exponential cost growth in long threads. |
| **Signs of drift** | **CONCEPTUAL** | When the model starts hallucinating rules or forgetting the persona. |
| **After a formal gate** | **CONCEPTUAL** | Upon Founder approval of a major milestone (e.g., DRAFT_0 complete). |
| **After a QA incident** | **CONCEPTUAL** | Resetting context after a major hallucination or truncation error. |
| **After canon or protocol changes** | **CONCEPTUAL** | Ensuring the model uses the newly updated rules, not its cached memory. |
| **Output target changes** | **CONCEPTUAL** | Switching from prose generation to QA to architecture to publication prep. |

*Note: While the doctrine is understood, there is currently no programmatic enforcer (e.g., a session manager script) implementing these criteria.*

---

## 5. High-Quality Context Pack Creation

A high-quality Context Pack is the foundation of stateless, deterministic LLM execution.

**Required Elements:**
*   **Required files / sources:** Source material to be processed.
*   **Program state & Current phase / gate:** Where the project is in the lifecycle.
*   **Canon and protocol excerpts:** Relevant rules (e.g., ELYSIUM voice, formatting constraints).
*   **Module registry / status:** Metadata about the specific module being worked on.
*   **Recent decisions & Open issues:** Context from the Decision Ledger.
*   **Stop conditions:** When the LLM must halt and return.
*   **Exact task objective:** The specific action required (e.g., "Write prose for OPN-001").
*   **Forbidden actions:** Negative constraints (e.g., "No bullet points").
*   **Output format:** Exact schema or markdown structure expected.
*   **Citations / file paths / proof:** Grounding data to prevent hallucination.

**Current Implementation Status:**
*   **PARTIAL:** Context packs are heavily used (21 exist in `BOOK/_fcs/context_packs/`). They successfully include task objectives, writing briefs, and voice rules.
*   **MISSING:** Automated dynamic compilation. Currently, Manus creates them ad-hoc. A universal `context_pack_generator.py` that automatically pulls from the Decision Ledger, Program State, and Registries is missing.

---

## 6. Why Context Packs Beat Opaque Long Memory

**Experimental / Practical Conclusion:** Generated task-specific context packs consistently produce better, more reliable results than relying on long-session memory alone.

**Why:**
1.  **Explicit & Auditable:** Every rule the LLM operates under is visible in a text file. If the output is wrong, the prompt can be debugged. Opaque memory cannot be debugged.
2.  **Compressed:** Context packs only include what is necessary for the *current* task, saving tokens and improving LLM attention (reducing the "lost in the middle" effect).
3.  **Task-Specific:** A context pack for prose generation is radically different from one for architectural review. Long memory dilutes focus.
4.  **Less Drift:** Models in long sessions tend to drift into conversational sycophancy or forget early constraints. Fresh sessions with hardcoded context packs reset the alignment.
5.  **Less Black-Box Reliance:** The intelligence is stored in the repo's architecture (YAML, file structure), not trapped in an ephemeral chat thread.

---

## 7. Output Validation After Session Reset

QA/QC becomes critically more important when using new sessions and context packs.

**The Risks of Session Resets:**
*   Loss of implicit conversation memory (nuances agreed upon previously but not documented).
*   Risk of missing the specific nuance of the current module.
*   Risk of wrong target (misinterpreting the fresh prompt).
*   Risk of drift (reverting to generic LLM behaviors if the context pack is weak).

**Required Validation (Implemented vs Missing):**
*   **Output in target:** **IMPLEMENTED** (Word count checks in `llm_output_guard.py`).
*   **No scope drift:** **IMPLEMENTED** (ChatGPT API L2 review checks brief fidelity).
*   **No canon drift:** **IMPLEMENTED** (ChatGPT API L2 review checks forbidden moves).
*   **No truncation:** **IMPLEMENTED** (`llm_output_guard.py` checks terminal punctuation and finish reasons).
*   **No missing sections:** **IMPLEMENTED** (Validation scripts check module counts).
*   **Review against context pack:** **IMPLEMENTED** (ChatGPT API explicitly reviews against the writing brief).
*   **Registry/source consistency:** **IMPLEMENTED** (`validate.py` checks cross-references).
*   **Post-generation audit:** **IMPLEMENTED** (Manus produces Completion Reports).

---

## 8. Prompt Blueprint Ownership

*   **ChatGPT Chief Architect defines prompt blueprints:** The overarching structure of how tasks should be requested is designed by the Chief Architect.
*   **Manus fills variables and assembles concrete prompts:** Manus acts as the templating engine, injecting the specific module ID, word count, and brief into the blueprint.
*   **Manus routes according to LLM Matrix:** Manus reads `LLM_MATRIX.md` to determine which API to call.
*   **Manus archives every outgoing prompt:** All context packs and API outputs are saved to the repo.
*   **Manus must not improvise architectural prompts outside blueprint authority:** Manus is an operator. It executes the blueprint; it does not invent new architectural directions.

---

## 9. LLM Routing / Tool Routing

Manus routes prompts to the correct engine/tool based on the `LLM_MATRIX.md` and `llm_orchestration_registry.yaml`.

*   **Claude:** Used exclusively for prose generation and prose revision. It possesses the necessary literary capability for the ELYSIUM voice.
*   **ChatGPT:** Used for architecture, review, QA/QC, and decision support. It acts as the analytical control tower.
*   **Image models / Graph tools / Specialist tools:** Used when indicated by the matrix for specific non-text tasks.

**Emphasis:** Not everything goes to Claude. Claude is the writer; ChatGPT is the editor/architect; Manus is the publisher/orchestrator.

---

## 10. Program Management Mode Integration

To complete the architecture, these components must be integrated into yOS / FCS Program Management Mode.

*   **Program state & Phase/gate management:** A centralized state machine tracking whether the project is in Planning, Drafting, Review, or Hardening.
*   **Session lifecycle management:** Automated rotation of API sessions based on the criteria in Section 4.
*   **Context pack generation:** Automated compilation before important calls.
*   **Persistent Chief Architect API thread:** Used *only* for bounded work phases, then archived.
*   **Decision ledger & Message bus:** Persistent storage of architectural decisions and inter-agent messages.
*   **Prompt blueprints & LLM Matrix router:** Standardized templates and routing logic.
*   **Output completion guard & QA/QC protocol integration:** The existing `llm_output_guard.py` and validation scripts acting as automated gates.
*   **Escalation:** Automated escalation to conversational ChatGPT or the Founder at major gates or when stop conditions are met.

---

## 11. Existing Artifacts / Missing Artifacts

| Artifact | Status | Notes |
| :--- | :--- | :--- |
| `BOOK/_fcs/protocols/FCS_QA_QC_GOVERNANCE_PROTOCOL.md` | **IMPLEMENTED** | Active, updated with stop conditions. |
| `BOOK/_fcs/protocols/LLM_OUTPUT_COMPLETION_AND_SECTIONING_PROTOCOL.md` | **IMPLEMENTED** | Active, governs truncation and limits. |
| `BOOK/_fcs/protocols/FCS_INTER_LLM_MESSAGE_BUS_PROTOCOL.md` | **MISSING** | Required for agent communication standards. |
| `BOOK/_fcs/protocols/FCS_SESSION_LIFECYCLE_PROTOCOL.md` | **MISSING** | Required for session rotation rules. |
| `BOOK/_fcs/protocols/FCS_PROMPT_BLUEPRINT_AND_CONTEXT_PACK_PROTOCOL.md` | **MISSING** | Required for dynamic pack generation rules. |
| `BOOK/_fcs/context_packs/` | **PARTIAL** | Directory exists, heavily used, but packs are generated ad-hoc. |
| `BOOK/_fcs/message_bus/` | **MISSING** | Directory does not exist. |
| `BOOK/_fcs/decision_ledger/` | **MISSING** | Directory does not exist. |
| `scripts/context_pack_generator.py` | **MISSING** | Required to automate context pack assembly. |
| `scripts/chief_architect_api_session.py` | **MISSING** | Required for persistent, chained API sessions. |
| `scripts/llm_output_guard.py` | **IMPLEMENTED** | Active, enforces completion validation. |

---

## 12. Recommended Next Step

**DO NOT IMPLEMENT.**

To complete the missing 20% and integrate it into Program Management Mode, the recommended next concrete step is:

**Create the Program Management Foundation:**
1.  Draft the three missing protocols (`FCS_SESSION_LIFECYCLE_PROTOCOL.md`, `FCS_PROMPT_BLUEPRINT_AND_CONTEXT_PACK_PROTOCOL.md`, `FCS_INTER_LLM_MESSAGE_BUS_PROTOCOL.md`).
2.  Initialize the missing directories (`message_bus/`, `decision_ledger/`).
3.  Develop `scripts/chief_architect_api_session.py` to support `previous_response_id` chaining and session rotation based on the lifecycle protocol.

---

## 13. Confirmations

*   **F02 not started:** CONFIRMED.
*   **No new book prose generated:** CONFIRMED.
*   **No manuscript changes made:** CONFIRMED.
*   **Audit/restitution only:** CONFIRMED.
