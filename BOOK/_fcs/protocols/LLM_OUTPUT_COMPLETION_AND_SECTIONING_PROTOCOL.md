---
id: LLM_OUTPUT_COMPLETION_AND_SECTIONING_PROTOCOL
title: "LLM Output Completion & Sectioning Protocol"
type: protocol
phase: III-1A
status: ACTIVE
last_updated: "2026-06-28"
---

# LLM Output Completion & Sectioning Protocol

## Purpose
Define how ELYSIUM handles LLM output limits, truncation detection, structured section generation, and post-generation QA/QC for all LLMs used in the pipeline.

## Scope
This protocol applies to:
- Claude API
- ChatGPT API
- Gemini API if used later
- Any other LLM API
- Any local or future model
- Any Manus-mediated LLM call

It applies to:
- prose generation
- prose revision
- review generation
- summaries
- compiled reports
- reader drafts
- architecture documents
- QA/QC reports

---

## 1. Core Distinction

- **Context window** is the amount of input a model can receive or consider.
- **Output limit** is the maximum amount the model can generate in one call.
- A model may have a large context window but still produce truncated output if max output tokens are too low.
- No output is trusted solely because the model has a large context window.

---

## 2. Universal Output Completion Checks

For every LLM call, the pipeline must capture and store:
- model name
- provider
- input token count if available
- output token count if available
- max output tokens requested
- stop_reason / finish_reason
- timestamp
- script/function used
- output file path

An output must be marked **INVALID** or **TRUNCATED** if:
- `stop_reason` / `finish_reason` indicates `max_tokens`, `length`, `content_filter` interruption, tool interruption, or equivalent
- output ends without terminal punctuation where prose is expected
- output ends with comma, colon, dash, semicolon, conjunction, or incomplete phrase
- required sections are missing
- word count is far below target without explanation
- word count is far above target and likely runaway
- YAML/frontmatter is incomplete
- Markdown fence or table is incomplete
- final paragraph appears cut
- output says it cannot continue due to length
- output asks to continue but was promoted as complete
- compiled reader ends before all expected modules are included

---

## 3. No Promotion Rule

**Hard rule:**
No LLM output may be promoted to DRAFT_0, registry status, compiled reader, or Chief Architect review package if it is marked TRUNCATED, INCOMPLETE, or OUTPUT_UNVERIFIED.

If output completion cannot be verified, stop and report.

---

## 4. Auto-Rerun Rule

If output is truncated:
1. Automatically rerun once with higher max output tokens if allowed.
2. If the second run is complete, use the complete output.
3. If the second run is still truncated, stop.
4. Do not stitch arbitrary fragments unless structured section generation was explicitly used.
5. Report the failure to Chief Architect.

---

## 5. Structured Section Generation

Use sectioned generation when:
- expected output exceeds safe one-shot output range for that LLM
- module target is above 2,500 words
- report target is above 4,000 words
- model has known low output limit
- prior one-shot attempt hit max_tokens
- output requires many explicit required sections
- generation includes long tables, registries, or compiled content
- LLM Matrix indicates sectioning for that model/task

Do not split arbitrarily by token count. Split by semantic sections.

**Examples:**

For prose modules:
- opening movement
- diagnostic section
- historical section
- pathology section
- regenerative direction
- transition paragraph

For reports:
- governance audit
- metadata audit
- validation audit
- content review
- process improvements
- decision request

For compiled reader:
- compile by module
- verify each module exists
- assemble after all modules pass source integrity checks

---

## 6. Sectioned Generation Workflow

For sectioned generation:
1. Create a locked section plan.
2. Generate each section separately.
3. Validate each section:
   - terminal punctuation
   - required content
   - no truncation
   - word count
   - continuity markers
4. Store each section output separately.
5. Assemble sections into one draft.
6. Run an assembly coherence pass.
7. Run global QA/QC:
   - no duplicated transitions
   - no missing sections
   - no contradictory terminology
   - no section seam artifacts
   - no summary instead of prose
8. Only then promote to DRAFT_0 or report final.

---

## 7. Provider-Specific Finish Reason Mapping

Create a normalized field: `llm_completion_status`

Allowed values:
- `COMPLETE`
- `TRUNCATED_MAX_TOKENS`
- `INTERRUPTED`
- `CONTENT_FILTERED`
- `TOOL_INTERRUPTED`
- `INVALID_FORMAT`
- `UNKNOWN`

Map provider-specific fields:
- Anthropic / Claude: `stop_reason`
- OpenAI / ChatGPT: `finish_reason`
- Google / Gemini: `finishReason`
- Other providers: equivalent field if available

If no finish reason is available, mark UNKNOWN and require secondary completion checks.

---

## 8. QA/QC A Posteriori

After generation, run a post-generation audit.

For prose modules, check:
- source draft exists
- frontmatter complete
- word_count matches actual prose count within tolerance
- terminal punctuation
- no forbidden canon errors
- no obvious truncation
- required concepts present
- title/module_id/path consistency
- ChatGPT API review file exists
- API output exists
- no Manus prose contamination
- registry entry exists

For compiled reader, check:
- all compile:true modules included
- module count matches registry
- word totals match registry
- no source ending truncated
- no compiled ending truncated
- summary table matches header
- all headings present
- no duplicate/missing modules
- no YAML frontmatter leaked unless intended

For QA/QC reports, check:
- all required sections present
- all promised files exist
- validation result included
- branch/commit/tag included
- F02 not started confirmed if relevant
- remaining issues clearly listed

---

## 9. LLM Matrix Integration

The LLM Matrix includes, for each model/provider:
- safe one-shot prose word target
- maximum recommended output tokens
- known output limit risk
- whether structured section generation is recommended
- whether `stop_reason` / `finish_reason` is available
- preferred retry strategy
- preferred review model
- whether the model is allowed for specific tasks (prose, revision, review, etc.)

**Default policy:**
- Claude: preferred prose generation, but output completion must be checked.
- ChatGPT API: preferred review / architecture validation, but review reports also require completion checks.
- Any model: no output accepted without completion verification.

---

## 10. Script Improvements Required

All relevant scripts or shared utility functions must record:
- provider
- model
- max_tokens / max_output_tokens
- input_tokens
- output_tokens
- stop_reason / finish_reason
- normalized completion status
- output file path
- validation result

Minimum required function: `validate_llm_output_completion(output_text, metadata)`
Returns: `COMPLETE`, `TRUNCATED`, `INCOMPLETE`, or `UNKNOWN` with reasons.

---

## 11. Reporting Requirements

Every module completion report must now include:
- model used
- provider
- max output tokens requested
- output tokens used
- stop_reason / finish_reason
- normalized completion status
- word count
- terminal punctuation status
- review status
- promotion decision

**Example:**
LLM completion:
- provider: Anthropic
- model: claude-opus-4-5
- max_tokens: 6000
- output_tokens: 3120
- stop_reason: end_turn
- completion_status: COMPLETE
- terminal_punctuation: PASS
- promoted_to_draft: YES

---

## 12. Stop Conditions

Global stop conditions added:
- Any prose output with `completion_status != COMPLETE`
- Any review output with `completion_status == TRUNCATED_MAX_TOKENS`
- Any compiled reader mismatch
- Any missing required section after sectioned generation
- Any model response that says continuation is needed
- Any output where source and compiled version differ unexpectedly
- Any uncertainty about whether a text is complete
