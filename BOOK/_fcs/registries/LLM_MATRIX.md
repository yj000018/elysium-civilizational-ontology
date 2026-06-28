---
id: LLM_MATRIX
title: "yOS LLM & Tool Routing Matrix"
type: registry
phase: yOS-Core
status: ACTIVE
last_updated: "2026-06-28"
---

# yOS LLM & Tool Routing Matrix

This matrix defines the operational parameters, capabilities, fallback rules, and quality control (QC) requirements for all LLMs and tools orchestrated by Manus within the yOS / FCS Program Management Mode. It is agnostic across all program types and is the canonical reference for the `LLM_OUTPUT_COMPLETION_AND_SECTIONING_PROTOCOL.md` and `FCS_MULTI_LLM_ORCHESTRATION_PROTOCOL.md`.

---

## 1. Provider & Capability Matrix

| Provider | Model / Tool | Authorized Task Types | Context Window | Safe Output Limit | Cost Profile | Latency | Quality Risk |
|----------|--------------|-----------------------|----------------|-------------------|--------------|---------|--------------|
| **Anthropic** | `claude-opus-4-5` | Book prose, prose revision, complex translation | 200k tokens | 6,000 tokens (~2,000 words) | High | High | Truncation at output limit (Confirmed) |
| **OpenAI** | `gpt-4o-2024-08-06` | Architecture, review, QA/QC, briefs, code, JSON | 128k tokens | 16,384 tokens | Medium | Low | Hallucination in long sessions |
| **Google** | `gemini-1.5-pro` | Long-doc analysis, broad research synthesis | 1M+ tokens | 8,192 tokens | Medium | Medium | "Lost in the middle" degradation |
| **Manus Native** | `generate_image` | Images, concept art, visual mockups | N/A | 1 image | Low | Low | Prompt adherence variance |
| **Manus Native** | `generate_video` | Video generation | N/A | ~5-10s clip | High | High | Physics/temporal coherence |
| **Manus Native** | `slides` | Slide decks, presentations | N/A | ~15 slides | Medium | Medium | Formatting rigidity |
| **Python/Manim** | Code Execution | Charts, data viz, vector animations, code | N/A | N/A | Low | Low | Syntax/dependency errors |
| **Web Tools** | `search` / Webdev | Broad research, web apps, dynamic data | N/A | N/A | Low | Low | Stale or gated data |

---

## 2. Routing Rules by Program / Task Type

| Task Category | Primary Engine | L2 Reviewer / QA | Sectioning Required? | Notes |
|---------------|----------------|------------------|----------------------|-------|
| **Book Prose** | Claude API | ChatGPT API | Yes (if >2,500w) | Manus must NEVER write book prose directly. |
| **Architecture** | ChatGPT API | Founder | No | Used for structural decisions and writing briefs. |
| **Code / Webdev** | Manus (Python/Node) | ChatGPT API | No | Manus writes and executes; ChatGPT reviews logic if complex. |
| **Charts / Viz** | Manus (Python/Matplotlib) | N/A | No | Deterministic code execution preferred over LLM ASCII art. |
| **Images / Video** | Manus Media Gen | Founder | No | Direct generation via native tools. |
| **Slides** | Manus Slides Gen | Founder | No | Content prepared by LLM, rendered by Manus. |
| **Research** | Manus Web/Search | Gemini/ChatGPT | No | Manus extracts; LLM synthesizes. |
| **Translation** | Claude API | ChatGPT API | Yes (if >2,000w) | Claude for nuance; ChatGPT for conceptual fidelity check. |

---

## 3. Output Limits & Finish Reason Mapping

| Provider | Raw Field | COMPLETE | TRUNCATED | INTERRUPTED | FILTERED | TOOL |
|----------|-----------|----------|-----------|-------------|----------|------|
| Anthropic | `stop_reason` | `end_turn`, `stop_sequence` | `max_tokens` | — | — | `tool_use` |
| OpenAI | `finish_reason` | `stop` | `length` | — | `content_filter` | `function_call`, `tool_calls` |
| Google | `finishReason` | `STOP` | `MAX_TOKENS` | — | `SAFETY`, `RECITATION` | — |

---

## 4. Fallback Rules

If the primary engine fails, hits a rate limit, or produces invalid output, Manus must follow these fallback rules:

| Scenario | Auto-Fallback Action | Approval-Required Fallback |
|----------|----------------------|----------------------------|
| **Claude API Rate Limit** | Wait 60s, retry 3x. | Switch to ChatGPT API for prose (requires Founder approval). |
| **Truncated Output (Max Tokens)** | Rerun immediately with `max_tokens` raised (e.g., 8,000). | If still truncated, halt and require Sectioned Generation approval. |
| **ChatGPT API Failure** | Wait 30s, retry 3x. | Halt. Do not use Claude for L2 review without approval. |
| **Tool Execution Error (Code)** | Debug and fix autonomously (up to 3 attempts). | Halt and request Founder intervention. |
| **Content Filter Block** | Rewrite prompt to remove trigger words. | Halt and request Founder override. |

*Hard Rule: Silent fallback is strictly forbidden. If an API is not called, the output must be labeled `API_NOT_CALLED` or `SCAFFOLD_ONLY`.*

---

## 5. Quality Control (QC) Requirements

Every task executed through this matrix requires strict QC validation before promotion.

| Task Type | L0 (Automated) | L1 (Manus) | L2 (LLM Review) | L3/L4 (Human) |
|-----------|----------------|------------|-----------------|---------------|
| **Prose** | `llm_output_guard.py` (terminal punct, length) | Format, frontmatter, registry check | ChatGPT API (Brief fidelity, voice) | Chief Architect / Founder |
| **Code** | Syntax check, unit tests | Execution verification | N/A (unless complex) | Founder |
| **Review** | `llm_output_guard.py` | Decision parsing (PASS/REVISE) | N/A | N/A |
| **Images** | File size, format check | Visual verification (multimodal) | N/A | Founder |

---

## 6. QC Debt & Legacy Reporting

As yOS empirical learning improves our validation tools (e.g., the introduction of `llm_completion_status` tracking), older files may lack the required metadata.

**Policy:**
1. Legacy files lacking new mandatory metadata must **not** be silently ignored.
2. They must be explicitly reported as **QC Debt** (Warnings) during validation runs.
3. They are permitted to remain in the repository but flag the need for eventual backfilling or re-validation.

---

## 7. Matrix Update Policy

This matrix is a living document governed by yOS empirical learning.

- **Trigger for Update:** Any confirmed failure mode (e.g., discovering a new token limit, a hallucination pattern, or a tool deprecation) must result in an immediate update to this matrix.
- **Authority:** Manus may propose updates to the matrix based on operational data. The Founder must approve structural changes to routing preferences.
