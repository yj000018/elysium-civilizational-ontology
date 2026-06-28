---
id: LLM_MATRIX
title: "ELYSIUM LLM Matrix"
type: registry
phase: III-1A
status: ACTIVE
last_updated: "2026-06-28"
---

# ELYSIUM LLM Matrix

This matrix defines the operational parameters, capabilities, and constraints for each LLM provider and model used in the ELYSIUM production pipeline. It is the canonical reference for the `LLM_OUTPUT_COMPLETION_AND_SECTIONING_PROTOCOL.md`.

---

## Provider Matrix

| Provider | Model | Role | Safe One-Shot Prose (words) | Max Output Tokens | Output Limit Risk | Sectioning Recommended | finish_reason Available | Preferred Retry | Preferred Review Model |
|----------|-------|------|----------------------------|-------------------|-------------------|----------------------|------------------------|-----------------|----------------------|
| Anthropic | claude-opus-4-5 | Prose generation | 1,500–2,000 | 6,000 (configured) | MEDIUM — token ceiling confirmed in F01-000 | Yes if >2,500w | Yes (`stop_reason`) | Rerun with max_tokens=8000 | gpt-4o-2024-08-06 |
| OpenAI | gpt-4o-2024-08-06 | Prose review / QA | 400 (review) | 500 (configured) | LOW for reviews | No (reviews are short) | Yes (`finish_reason`) | Rerun with max_tokens=800 | N/A |
| Google | gemini-pro (future) | Long-doc analysis | TBD | TBD | UNKNOWN | TBD | Yes (`finishReason`) | TBD | TBD |
| Any local model | (future) | TBD | TBD | TBD | HIGH — no API metadata | Yes | Unknown | Manual check | TBD |

---

## Capability Matrix

| Task | Claude | ChatGPT API | Manus (orchestration) | Notes |
|------|--------|-------------|----------------------|-------|
| Prose generation | ✅ PREFERRED | ❌ NOT ALLOWED | ❌ NOT ALLOWED | Claude only; Manus prose = contamination |
| Prose revision | ✅ PREFERRED | ❌ NOT ALLOWED | ❌ NOT ALLOWED | Claude only |
| Prose review | ⚠️ NOT PREFERRED | ✅ PREFERRED | ❌ NOT ALLOWED | ChatGPT API is L2 reviewer |
| Architecture review | ❌ NOT ALLOWED | ✅ PREFERRED | ❌ NOT ALLOWED | Chief Architect authority |
| QA/QC audit | ❌ NOT ALLOWED | ⚠️ PARTIAL | ✅ OPERATIONAL | Manus = L1; ChatGPT = L2 |
| Compilation | ❌ NOT ALLOWED | ❌ NOT ALLOWED | ✅ PREFERRED | Manus compiles reader drafts |
| Registry updates | ❌ NOT ALLOWED | ❌ NOT ALLOWED | ✅ PREFERRED | Manus manages metadata |
| Translation (future) | ✅ | ✅ | ⚠️ | TBD |

---

## Output Limit Risk Register

| Provider | Model | Known Truncation Risk | Root Cause | Mitigation |
|----------|-------|----------------------|------------|------------|
| Anthropic | claude-opus-4-5 | CONFIRMED — F01-000 truncated at 2,048 tokens | Default max_tokens was 4,096; actual output hit 2,048 ceiling | Raise max_tokens to 6,000; validate stop_reason after every call |
| OpenAI | gpt-4o-2024-08-06 | LOW for reviews (500 tokens sufficient) | N/A | Monitor finish_reason; raise to 800 if review is cut |
| Google | gemini-pro | UNKNOWN | N/A | Require finishReason check; default to sectioning |

---

## Finish Reason Mapping

| Provider | Raw Field | COMPLETE | TRUNCATED | INTERRUPTED | FILTERED | TOOL |
|----------|-----------|----------|-----------|-------------|----------|------|
| Anthropic | `stop_reason` | `end_turn`, `stop_sequence` | `max_tokens` | — | — | `tool_use` |
| OpenAI | `finish_reason` | `stop` | `length` | — | `content_filter` | `function_call`, `tool_calls` |
| Google | `finishReason` | `STOP` | `MAX_TOKENS` | — | `SAFETY`, `RECITATION` | — |

---

## Default Policy

The following defaults apply to all ELYSIUM LLM calls:

1. No output is trusted solely because the model has a large context window.
2. Every LLM call must record: provider, model, max_tokens, input_tokens, output_tokens, stop_reason/finish_reason, normalized `llm_completion_status`.
3. No output with `llm_completion_status != COMPLETE` may be promoted to DRAFT_0.
4. Sectioned generation is required for any prose module targeting >2,500 words.
5. The `llm_output_guard.py` utility must be used for all new LLM calls.
6. Claude API is the only authorized prose generator. ChatGPT API is the only authorized L2 prose reviewer. Manus is the only authorized orchestrator and compiler.
