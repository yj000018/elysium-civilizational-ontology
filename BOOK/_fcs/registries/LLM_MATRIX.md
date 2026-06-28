---
id: LLM_MATRIX
title: "yOS LLM & Tool Routing Matrix"
type: registry
phase: yOS_Orchestration_Core
status: ACTIVE
last_updated: "2026-06-28"
---

# yOS LLM & Tool Routing Matrix

This matrix defines the operational parameters, capabilities, fallback rules, and quality control (QC) requirements for all LLMs and tools orchestrated by Manus. 

**Scope:** This is a **Core yOS registry**, belonging to the **yOS Orchestration Core** (Inter-LLM, Inter-Tool & Context Coordination Layer). It is not FCS-only; FCS and the ELYSIUM Book are downstream applications that utilize this core layer.

---

## 1. The 7 Intelligences Mapping

The yOS Orchestration Core operates across 7 distinct intelligence vectors. This matrix primarily governs **Routing Intelligence** while integrating with the others:

1. **Context Intelligence** (`context_pack_generator.py`)
2. **Session Intelligence** (`chief_architect_api_session.py`)
3. **Routing Intelligence** (This Matrix)
4. **Message Intelligence** (Message Bus)
5. **Memory Intelligence** (Decision Ledger & Git)
6. **Output Intelligence** (`llm_output_guard.py`)
7. **Governance Intelligence** (Protocols & Approvals)

---

## 2. Routing Governance & Authority Model

Routing decisions are governed by a strict authority model to prevent cost overruns and architectural drift.

- **L3 Authority:** Chief Architect (ChatGPT API)
- **L4 Authority:** Founder (Yannick)

**Governance Rules:**
- **Manus** may *propose* routing updates based on empirical learning.
- **Chief Architect (L3)** approves *technical* routing changes (e.g., swapping Claude versions for minor tasks).
- **Founder (L4)** approves *strategic, sovereign, or cost-sensitive* routing changes (e.g., adding a new paid API, altering the primary prose engine).

---

## 3. Expanded Task Taxonomy & Routing Rules

| Task Type | Primary | Secondary | Fallback | Auto-Fallback? | Escalation Required | Output Guard | Context Need | Output Need | Cost Risk | Latency Risk | Quality Risk | Known Failure Modes | Last Updated | Update Reason |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Book Prose** | Claude API | None | None | No | Founder (L4) | Strict (Len/Punct) | High | High (Prose) | High | High | High | Truncation, tone drift | 2026-06-28 | Hardening |
| **Architecture** | ChatGPT API | Claude API | None | No | Chief Arch (L3) | Medium | High | High (Struct) | Med | Low | Med | Hallucination | 2026-06-28 | Hardening |
| **Research** | Web/Search | Perplexity | Gemini | Yes | Chief Arch (L3) | Low | Med | Med (Facts) | Low | Low | Low | Stale data | 2026-06-28 | Hardening |
| **Code** | Manus (Node/Py) | ChatGPT API | Claude API | Yes | Chief Arch (L3) | Syntax/Test | High | High (Exec) | Low | Low | Med | Dependency errors | 2026-06-28 | Hardening |
| **Charts** | Manus (Python) | N/A | N/A | Yes | Chief Arch (L3) | Image Check | Low | Med (Visual) | Low | Low | Low | Axis rendering | 2026-06-28 | Hardening |
| **Diagrams** | Manus (Manim) | Mermaid | N/A | Yes | Chief Arch (L3) | SVG/PNG Check | Med | Med (Visual) | Low | Med | Low | Syntax errors | 2026-06-28 | Hardening |
| **Image Gen** | Manus Media | DALL-E 3 | N/A | No | Founder (L4) | Visual Check | Low | High (Visual) | Low | Low | Med | Prompt adherence | 2026-06-28 | Hardening |
| **Image Edit** | Manus Media | N/A | N/A | No | Founder (L4) | Visual Check | Low | High (Visual) | Low | Low | Med | Artifacting | 2026-06-28 | Hardening |
| **Video Gen** | Manus Media | N/A | N/A | No | Founder (L4) | Visual Check | Low | High (Visual) | High | High | High | Physics coherence | 2026-06-28 | Hardening |
| **Slides** | Manus Slides | N/A | N/A | No | Founder (L4) | Format Check | Med | Med (Visual) | Med | Med | Low | Formatting rigidity | 2026-06-28 | Hardening |
| **Translation** | Claude API | ChatGPT API | DeepL | Yes | Chief Arch (L3) | Len/Punct | High | High (Prose) | Med | Med | Med | Idiom loss | 2026-06-28 | Hardening |
| **Audio/Voice** | Manus Media | N/A | N/A | No | Founder (L4) | Audio Check | Low | High (Audio) | Med | Low | Low | Robotic tone | 2026-06-28 | Hardening |
| **Data Extract** | Web/Search | Firecrawl | N/A | Yes | Chief Arch (L3) | JSON Schema | Low | Med (Data) | Low | Low | Low | Anti-bot blocks | 2026-06-28 | Hardening |
| **Doc Prod** | ChatGPT API | Claude API | N/A | Yes | Chief Arch (L3) | Format Check | Med | High (Struct) | Low | Low | Low | Formatting loss | 2026-06-28 | Hardening |
| **Web/App Gen** | Manus Webdev | N/A | N/A | Yes | Founder (L4) | Build Check | High | High (Code) | Low | High | High | Build failures | 2026-06-28 | Hardening |

---

## 4. Fallback Doctrine

Fallback rules distinguish between automatic recovery and escalation:

- **Automatic Fallback:** Manus may autonomously switch to the defined fallback tool (e.g., Search failing -> try Perplexity) without asking, provided the "Auto-Fallback?" flag is Yes.
- **Chief Architect Approval Required:** If an L3-escalation task fails all auto-fallbacks, Manus must halt and request a decision from the Chief Architect API thread.
- **Founder Approval Required:** If an L4-escalation task fails (e.g., Book Prose generation fails due to Claude API limits), Manus must **Hard Stop** and escalate to the Founder. Silent fallback is strictly forbidden.

---

## 5. QC Debt & Legacy Validation Doctrine

The validation doctrine is strictly enforced across the yOS Orchestration Core:

1. **Legacy Non-Critical = Debt:** Older API outputs missing `llm_completion_status` are flagged as `[QC DEBT]` warnings.
2. **Legacy Gate-Critical = Blocker:** Any legacy file missing metadata that acts as a gate (e.g., a final review before phase transition) is a **Blocker**. The phase cannot advance until it is verified.
3. **New Missing Metadata = Error:** Any newly generated API output missing `llm_completion_status` triggers a hard validation `[ERROR]`.
4. **Promoted Unverified Output = Hard Stop:** If an unverified output is promoted to a canonical draft, the validation script will trigger a **Hard Stop**.
5. **Transparency:** Validation reports must explicitly list the count of legacy skipped/unverified files. They must not hide behind a "0 warnings" facade.

---

## 6. yOS Empirical Learning Log

This matrix evolves based on empirical data. Every structural change to this matrix must be logged here.

| Date | Task Type | Incident / Improvement | Old Rule | New Rule | Evidence | Decision Authority | Follow-up Validation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-06-28 | Book Prose | Claude API truncation at 2k words | 4096 token limit | 6000 token limit + `llm_output_guard` | F01-000 REVISED truncation | Founder (L4) | validate.py 0 errors |
| 2026-06-28 | All | Missing fallback granularity | Binary fallback | 4-tier fallback (Auto, L3, L4, Stop) | Matrix ambiguity | Founder (L4) | Matrix updated |
