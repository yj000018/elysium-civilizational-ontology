---
id: ELYSIUM_yOS_Program_Management_Runtime_GapFill_Report
title: "ELYSIUM / yOS — Program Management Runtime Integration Gap-Fill"
date: "2026-06-28"
status: DESIGN_COMPLETE
type: architecture_report
---

# ELYSIUM / yOS — Program Management Runtime Integration Gap-Fill

## 1. Mapping Old yOS Concepts to Current FCS Components

To unify the system without reinventing parallel modules, legacy yOS conceptual components map directly to the active and planned FCS/ELYSIUM architecture:

| Legacy yOS Concept | Current/Planned FCS Component |
| :--- | :--- |
| **Context Builder** | `context_pack_generator.py` (To be built) |
| **Retriever** | Context selector / source selector (Internal to `context_pack_generator.py`) |
| **Session Delta Engine** | Session lifecycle + Decision deltas (Triggering session rotation) |
| **Memory Consolidation Engine** | Decision Ledger / Canonical Memory (`BOOK/_fcs/decision_ledger/`) |
| **Git Memory Layer** | Repo source of truth (Markdown + YAML frontmatter) |
| **YOS Tool Routing** | `LLM_MATRIX.md` (Upgraded to agnostic yOS LLM & Tool Routing Matrix) |
| **YOS Model Routing** | `LLM_MATRIX.md` |
| **Conversation Capture Layer** | Message Bus + Decision Ledger (`BOOK/_fcs/message_bus/`) |
| **yoos-hydrate** | Context Pack Injection (At session start) |
| **yoos-memorize** | Capture / Ledger Persistence (At gate closure) |

---

## 2. Identification of Duplicate Risks

If implemented without care, the following overlaps present severe architectural risks:

*   **Duplicate Memory:** If the ChatGPT API thread retains long conversational memory while the Git repo also stores decisions, the two will drift. *Resolution:* The repo is the sole canonical source of truth. API sessions must be bounded and reset.
*   **Duplicate Routing Logic:** If `llm_orchestration_registry.yaml` and `LLM_MATRIX.md` contain overlapping routing instructions, conflicts will occur. *Resolution:* `LLM_MATRIX.md` is the universal, agnostic router; the orchestration registry defines phase-specific implementations.
*   **Duplicate Context Assembly:** If Manus manually assembles context while `context_pack_generator.py` also exists, discrepancies will emerge. *Resolution:* Manus must exclusively use the generator script.
*   **Duplicate Status Tracking:** If Notion tracks project state while `validate.py` tracks file state, they can desync. *Resolution:* The Git repo is the absolute state. Notion is a projection/dashboard of that state.

---

## 3. The Unified Program Management Runtime

The Program Management Runtime is the overarching control loop for yOS/FCS. It consists of 10 unified components:

1.  **Program State Manager:** Tracks the current active phase, active module, and global completion percentage via Git/YAML registries.
2.  **Phase/Gate Manager:** Enforces stop conditions (e.g., F02 cannot start until F01 is approved by the Chief Architect).
3.  **Context Pack Generator:** (`context_pack_generator.py`) Dynamically compiles the required context for the current task.
4.  **Session Lifecycle Manager:** (`chief_architect_api_session.py`) Manages `previous_response_id` chaining and enforces rotation criteria.
5.  **Inter-LLM Message Bus:** (`BOOK/_fcs/message_bus/`) Stores raw agent-to-agent communication (e.g., Claude's notes to ChatGPT).
6.  **Decision Ledger:** (`BOOK/_fcs/decision_ledger/`) Stores finalized architectural decisions extracted from the Message Bus.
7.  **Prompt Blueprint System:** Standardized templates for API calls, ensuring the Chief Architect dictates the prompt structure, not Manus.
8.  **LLM & Tool Routing Matrix:** (`LLM_MATRIX.md`) The universal lookup table for which tool handles which task type.
9.  **Output Guard / QA-QC Validator:** (`llm_output_guard.py` & `validate.py`) Validates outputs for truncation, scope drift, and registry consistency before promotion.
10. **Escalation Protocol:** The mechanism by which Manus halts execution and pings the Founder or conversational ChatGPT upon hitting a hard stop condition.

---

## 4. Session Rotation Criteria

API sessions (specifically the ChatGPT Chief Architect thread) must be rotated (reset) to prevent context bloat and drift. Rotation occurs upon any of the following triggers:

*   **Phase/Gate change:** Moving from Drafting to Review, or F01 to F02.
*   **Theme change:** Shifting from Material Existence to Vitality.
*   **Token bloat:** Reaching >30k tokens in the current thread.
*   **Context pressure:** When the model begins losing "middle" context (hallucinating constraints).
*   **Rising cost:** To prevent exponential token pricing on deep threads.
*   **Drift signals:** When the LLM violates a hard constraint or forgets its persona.
*   **After formal gate:** Upon Founder approval of a milestone.
*   **After QA incident:** To wipe the context window of previous errors or truncations.
*   **After canon/protocol change:** Ensuring the model uses updated rules, not cached memory.
*   **Output target change:** Switching from prose review to structural architecture.

---

## 5. High-Quality Context Pack Schema

A dynamically generated Context Pack must include:

1.  **Task Objective:** Exact action required (e.g., "Review OPN-001 prose against brief").
2.  **Phase/Gate:** Current program location.
3.  **Program State:** Completion status of surrounding modules.
4.  **Relevant Canon:** Core ontology definitions.
5.  **Relevant Protocol Excerpts:** Voice rules, formatting constraints.
6.  **Latest Decisions:** Recent rulings from the Decision Ledger.
7.  **Open Issues:** Known conflicts or unresolved debates.
8.  **Source Files:** The actual drafts, briefs, or code to be processed.
9.  **Forbidden Actions:** Negative constraints (e.g., "No bullet points").
10. **Routing Decision:** Why this model was chosen (from LLM Matrix).
11. **Expected Output:** Exact schema (e.g., "PASS" or "REVISE").
12. **QA/QC Criteria:** How the output will be judged by the Output Guard.
13. **Stop Conditions:** When the LLM must halt.

---

## 6. Context Pack Statuses

Context packs are stateful artifacts:

*   **`CONTEXT_PACK_READY`**: Fully compiled, up-to-date with the repo, ready for API injection.
*   **`CONTEXT_PACK_INCOMPLETE`**: Missing source files or required ledger entries.
*   **`CONTEXT_PACK_STALE`**: Generated before a recent Git commit; must be regenerated.
*   **`CONTEXT_PACK_GATE_CRITICAL`**: Contains decisions that require Founder approval before the pack can be executed.

---

## 7. Post-Reset Output Validation

When a session is reset, implicit memory is lost. The `llm_output_guard.py` and `validate.py` must aggressively check the first output of a new session for:

*   **Output matches target:** Word counts and formats are correct.
*   **No scope drift:** The LLM did not invent new facets or modules.
*   **No canon drift:** Terminology matches the ontology (e.g., "five flow classes").
*   **No truncation:** Terminal punctuation and `finish_reason` are valid.
*   **No missing constraints:** The LLM obeyed the "Forbidden Actions" in the context pack.
*   **No wrong routing:** The LLM did not attempt to perform a task assigned to another model.
*   **No hidden summary:** The LLM delivered the actual artifact, not a summary of what it *would* do.
*   **Context pack coverage sufficient:** The LLM did not complain about missing information.

---

## 8. Upgraded LLM & Tool Routing Matrix

The `LLM_MATRIX.md` has been upgraded to an agnostic routing matrix covering all yOS program types.

*   **Book Prose:** Primary: Claude API. Review: ChatGPT API. Sectioning: Yes.
*   **Book Architecture:** Primary: ChatGPT API. Review: Founder. Sectioning: No.
*   **Image Creation:** Primary: Manus Native (`generate_image`). Review: Founder.
*   **Video Creation:** Primary: Manus Native (`generate_video`). Review: Founder.
*   **Graph/Chart Creation:** Primary: Python/Manim. Review: N/A (Code execution).
*   **Research:** Primary: Web/Search. Review: Gemini/ChatGPT synthesis.
*   **Code/Scripts:** Primary: Manus (Python/Node). Review: ChatGPT (if complex).
*   **Slides:** Primary: Manus Native (`slides`). Review: Founder.
*   **Translation:** Primary: Claude API. Review: ChatGPT API (conceptual fidelity).

*Matrix includes: Auto-fallback vs approval-required fallback, context/output limits, and known failure modes.*

---

## 9. Legacy Validation Doctrine (Fixed)

The validation doctrine has been permanently upgraded:

*   **QC Debt:** Legacy skipped files (API outputs generated before `llm_completion_status` existed) are no longer silently ignored. They are reported as `[QC DEBT]` warnings.
*   **New File Error:** Any *new* API output missing the `llm_completion_status` frontmatter field triggers a hard validation error.
*   **Blocker:** Gate-critical legacy unverified files act as blockers for phase transitions (e.g., F02 cannot start until F01 legacy files are re-verified or explicitly approved).
*   **Reporting:** Validation reports (`VALIDATION_REPORT.md`) now explicitly include legacy skipped / unverified counts.

---

## 10. Proposed Files to Create/Update

To physically implement this Program Management Runtime, the following file operations are required in the next phase:

**To Create:**
1.  `BOOK/_fcs/protocols/FCS_PROGRAM_MANAGEMENT_RUNTIME_PROTOCOL.md` (The master loop)
2.  `BOOK/_fcs/protocols/FCS_SESSION_LIFECYCLE_PROTOCOL.md` (Rotation rules)
3.  `BOOK/_fcs/protocols/FCS_PROMPT_BLUEPRINT_AND_CONTEXT_PACK_PROTOCOL.md` (Schema rules)
4.  `BOOK/_fcs/protocols/FCS_INTER_LLM_MESSAGE_BUS_PROTOCOL.md` (Communication rules)
5.  `scripts/context_pack_generator.py` (The Context Builder)
6.  `scripts/chief_architect_api_session.py` (The Session Manager with `previous_response_id`)
7.  `BOOK/_fcs/decision_ledger/` (Directory)
8.  `BOOK/_fcs/message_bus/` (Directory)

**To Update / Merged:**
1.  `BOOK/_fcs/registries/LLM_MATRIX.md` (Already upgraded to the agnostic routing matrix).
2.  `scripts/validate.py` (Already updated to handle QC debt).

---

## 11. Confirmations

*   **F02 not started:** CONFIRMED.
*   **No book prose generated:** CONFIRMED.
*   **Manuscript unchanged:** CONFIRMED.
*   **Implementation halted:** CONFIRMED. This is a design/integration report only.
