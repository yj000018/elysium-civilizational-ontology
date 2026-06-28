---
id: FCS_MULTI_LLM_ORCHESTRATION_PROTOCOL
type: protocol
version: "0.1"
phase: yOS/FCS
status: ACTIVE
created_date: "2026-06-28"
created_by: "Manus — yOS/FCS Multi-LLM Orchestration Protocol MPM"
manus_role: ORCHESTRATION_ONLY
chatgpt_api_status: NOT_REQUIRED
claude_api_status: NOT_REQUIRED
routing_status: PROTOCOL_INSTALL
fallback_status: NONE
approval_status: PENDING_FOUNDER_REVIEW
---

# FCS Multi-LLM Orchestration Protocol

## Core Principle

> **Manus is the orchestration layer, not the authoring layer.**

> Founder gives intent once.
> Manus routes tasks between LLMs via API.
> Founder is consulted only at decision gates, approval gates, risk gates, or ambiguity gates.

---

## 1. Purpose

Define how Manus autonomously coordinates multiple LLMs and tools in FCS/yOS workflows so the Founder no longer has to manually copy-paste between systems.

The current workflow requires the Founder to copy-paste:
- Manus report → ChatGPT
- ChatGPT review → Manus
- Manus updated files → ChatGPT
- ChatGPT prompt → Manus
- Manus output → Claude later

This is unacceptable at scale.

The desired mode is: **One Founder command → Manus autonomous orchestration → Founder receives decision-ready result.**

---

## 2. Role Matrix

### Founder
- Gives intent
- Defines taste / vision / constraints
- Approves decision gates
- Adds Founder notes
- Validates final readiness

### Manus
- Decomposes task
- Checks routing matrix
- Calls LLM **VIA API** when needed
- Coordinates sequence
- Writes files
- Runs scripts
- Validates artifacts
- Commits / pushes / tags
- Writes reports
- Escalates only when required

### ChatGPT API
- Structure
- Architecture
- Ontology alignment
- Coherence review
- Writing brief review
- Decision framing
- Critique / risk review
- Factual/structural synthesis when relevant

### Claude API
- Prose writing
- Literary flow
- Voice
- Style
- Narrative density
- Revision
- Rhetorical polish

### Specialist tools/models
- Diagrams
- Citations
- Research extraction
- Data analysis
- Formatting
- Translation
- Design
- Audio/video if needed

---

## 3. Trigger Conditions

### Manus must orchestrate LLMs VIA API when a task requires:
- Prose writing
- Prose revision
- Architectural review
- Model comparison
- Ontology synthesis
- Deep coherence review
- Content compression
- Writing brief generation
- Translation review
- Multi-step intellectual work

### Manus may act alone only for:
- File operations
- Git
- Validation
- Metadata patching
- Registry updates
- Simple template creation
- Reports based on local facts
- Mechanical transformations

---

## 4. API Invocation Rule

When using another model, Manus must explicitly call the model **VIA API**.

Use exact instruction language in prompts and reports:

```text
Call the LLM VIA API.
```

If Manus cannot call the API, it must say so and mark the output:

```text
API_NOT_CALLED
SCAFFOLD_ONLY
PROVISIONAL_MANUS_OUTPUT
```

**Manus must never silently replace ChatGPT or Claude with internal Manus reasoning.**

---

## 5. No Silent Fallback Rule

If the selected LLM cannot be called:
- Do NOT pretend the routed step happened
- Do NOT mark output as approved
- Do NOT promote prose
- Write a blocked/partial report
- Create a payload that can be manually pasted if needed

---

## 6. Standard Orchestration Loop

Use this default loop for major content tasks:

1. Founder intent
2. Manus task decomposition
3. Routing preflight
4. Manus prepares context pack
5. ChatGPT API architecture/review pass
6. Manus applies structural result
7. Claude API prose pass if writing is authorized
8. ChatGPT API coherence/review pass
9. Claude API revision pass if required
10. Manus validates
11. Manus commits/pushes/tags
12. Manus writes completion report
13. Founder receives decision-ready output

---

## 7. Gate Model

### Manus must stop and ask the Founder at:
- Architecture lock gate
- Founder taste/voice gate
- Major split/merge/remove decision
- Factual uncertainty gate
- Risk gate
- Cost escalation gate
- Publication readiness gate
- S4 prose authorization gate

### Manus must NOT ask the Founder for:
- Routine file paths
- Mechanical registry updates
- Known branch names if inferable
- Repeated copy-paste
- Reports that can be read directly from repo
- Obvious validation reruns

---

## 8. Output Labeling

Every routed artifact must state:

```yaml
manus_role:
chatgpt_api_status:
claude_api_status:
specialist_tool_status:
routing_status:
fallback_status:
approval_status:
```

Accepted values:

```yaml
chatgpt_api_status:
  - NOT_REQUIRED
  - USED
  - FAILED
  - NOT_CALLED_SCAFFOLD_ONLY

claude_api_status:
  - NOT_REQUIRED
  - USED
  - FAILED
  - NOT_CALLED

fallback_status:
  - NONE
  - PROVISIONAL_MANUS_OUTPUT
  - SCAFFOLD_ONLY
  - BLOCKED
```

---

## 9. FCS Phase-Specific Routing

### X-Ray / Architecture phases
- Manus inspects files
- ChatGPT API reviews architecture
- Manus applies structural changes
- Claude API not used

### Writing Brief phases
- Manus scaffolds context
- ChatGPT API generates/reviews brief architecture
- Claude API not used

### Prose phases
- Manus prepares context and prompt
- ChatGPT API validates structural brief
- Claude API writes prose
- ChatGPT API reviews prose for coherence and ontology alignment
- Claude API revises prose if needed
- Manus stores output as draft only after routing is complete

### Translation phases
- Claude or specialist translation model translates
- ChatGPT API reviews conceptual fidelity
- Manus stores translated edition layer

### Atlas / Research phases
- Manus gathers corpus
- ChatGPT API synthesizes ontology/fact sheet architecture
- Specialist research tools may extract sources
- Claude API may polish prose only if writing is authorized

---

## 10. Cost and Mode Control

Manus must choose the minimum sufficient model/tool.

Use expensive calls only when:
- Structure is complex
- Prose quality matters
- Ontology coherence matters
- Founder has authorized deeper review
- Publication-level quality is required

Report model usage and cost class:

```yaml
cost_class: LOW | MEDIUM | HIGH
api_calls:
  chatgpt:
  claude:
  specialist:
```

---

## 11. Reporting Standard

Every multi-LLM orchestration run must report:
- Task classification
- Routing preflight
- APIs called
- APIs not called
- Fallback status
- Files created/modified
- Validation results
- Git status
- Mem0 status
- Decision gates pending
- Next action

---

## 12. Failure Modes

| Failure | Response |
|---|---|
| API unavailable | Mark BLOCKED, create manual paste payload |
| API returned unusable output | Mark FAILED, log, escalate to Founder |
| Model wrote prose when only brief was allowed | Discard output, mark PROTOCOL_VIOLATION |
| Manus wrote prose internally | Mark PROVISIONAL_MANUS_OUTPUT, do not promote |
| Context too large | Split into sub-tasks, pass via files |
| Validation failed | Fix before commit, never commit broken state |
| Git failed | Retry ×2, then report BLOCKED |
| Founder decision needed | Stop, create decision request, wait |

---

## 13. Founder Burden Minimization Rule

Manus must minimize Founder copy-paste:
- If an input exists in repo → Manus reads it
- If a prior report exists → Manus reads it
- If ChatGPT output can be passed via API → Manus passes it
- If Claude can be called via API → Manus calls it
- If a manual handoff is unavoidable → Manus creates a **single copy-paste payload**

---

## 14. Application to ELYSIUM Phase III-1A

**Current state:**
- S3 Writing Briefs exist but are marked `SCAFFOLDED` (not yet reviewed by ChatGPT API)
- Before S4, S3-R must call ChatGPT API VIA API for Chief Architect brief review/enrichment
- S4 must call Claude API VIA API for prose writing
- ChatGPT API must review Claude prose for ontology alignment before any DRAFT_0 promotion

**Required future sequence:**

1. **S3-R:** ChatGPT API reviews/enriches the 13 Writing Briefs
2. Founder reviews/adds notes (Section 18 of each brief)
3. **S4:** Manus calls Claude API to write one module at a time
4. ChatGPT API reviews each prose module
5. Claude API revises if needed
6. Manus saves outputs with correct status

---

## 15. Inheritance

This protocol inherits from and extends:
- `07_YOS_PATTERN_LIBRARY/LLM_ROUTING_MATRIX_PROTOCOL.md` (v0.2 — existing yOS Routing Matrix)
- `07_YOS_PATTERN_LIBRARY/MODEL_ROUTING_MATRIX.md`
- `BOOK/_fcs/protocols/FCS_WRITING_BRIEF_PROTOCOL.md`
- yOS Program Mode Doc 11 — Model Routing & Agent Roles Protocol

It does NOT replace the existing yOS Routing Matrix. It is a **FCS/ELYSIUM operational specialization** of that matrix.
