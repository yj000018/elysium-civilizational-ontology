# Git / Mem0 / Claude API Protocol — v0.1

## Status

**Status:** Candidate yOS Program Mode Pattern
**Source:** ELYSIUM operational development
**Version:** v0.1
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration
**Label:** CANDIDATE_YOS_CORE_PATTERN_PENDING_NOTION_RECONCILIATION

> ⚠️ This document is a candidate yOS Program Mode pattern extracted from ELYSIUM. It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.

**Notion page:** https://app.notion.com/p/38d35e218cf881fb9361df2f6a5453f7

---

## 1. Purpose

The Git / Mem0 / Claude API Protocol defines the persistence, memory, and review infrastructure for yOS Program Mode.

It ensures that Manus executions are: versioned, auditable, recoverable, memory-aware, reviewable, honest about API usage, safe against silent fallbacks, compatible with semi-autonomous execution.

This protocol applies to: ELYSIUM, FCS — Fractal Content Studio, yOS Program Mode, CasaTAO, future books, websites, knowledge systems, automation programs.

---

## 2. Three Persistence Layers

| Layer | Role | Stores |
|---|---|---|
| Git / GitHub | operational source of truth | files, prompts, reports, code, manifests |
| Mem0 | durable memory | accepted facts, stable decisions, durable rules |
| Notion | architectural documentation | concepts, protocols, maps, operating docs |

No single layer replaces the others.

---

## 3. Git / GitHub Protocol

### 3.1 Role

GitHub is the operational source of truth for active program execution.

### 3.2 Public repositories

Current ELYSIUM repository: https://github.com/yj000018/elysium-civilizational-ontology

### 3.3 Required Git behavior

Every Manus run that modifies files should: use a branch when appropriate, commit changes, push to GitHub when possible, include commit hash in completion report, tag major milestones, avoid untracked outputs, create fallback manual commands if push fails.

### 3.4 Branch naming

- canonicalization/pass-0.2C
- phase-iii/fractal-content-studio
- yos/program-mode

### 3.5 Tag naming

- pass-0.2C
- phase-iii-0A-fcs
- yos-program-mode-v0.1

### 3.6 Commit messages

Explicit and task-bound. Examples:
- ELYSIUM Pass 0.2C — public GitHub persistence and Mem0 repair
- yOS Program Mode docs — add Git / Mem0 / Claude API Protocol v0.1

### 3.7 Git failure handling

If Git push fails: do not claim success, keep local commit if possible, create Git bundle if useful, provide manual commands, log blocker.

Status: `GIT_PUSH_BLOCKED_MANUAL_ACTION_REQUIRED`

---

## 4. Mem0 Protocol

### 4.1 What to persist

- accepted canonical architecture
- accepted phase status
- durable naming decisions
- durable process rules
- accepted protocol creation
- stable source-of-truth decisions

### 4.2 What not to persist

- temporary drafts
- speculative ideas
- rejected options
- every Manus run detail
- every Git commit

### 4.3 Mem0 success rule

Do not claim Mem0 success unless it actually succeeds. If Mem0 fails: `MEM0_PERSISTENCE_BLOCKED_RETRY_REQUIRED`

Create: MEM0_IMPORT_PAYLOAD.json and MEM0_TROUBLESHOOTING_NOTES.md

### 4.4 Mem0 retry rule

If Mem0 fails due to telemetry or timeout, retry with safe mitigation. Example from ELYSIUM Pass 0.2C: fixed by disabling PostHog telemetry via environment variables.

---

## 5. Notion Protocol

### 5.1 yOS source of truth rule

Existing yOS Notion documentation remains source of truth for yOS.

Candidate patterns must be marked: `Candidate yOS Program Mode Pattern — Pending yOS Notion reconciliation`

Do not promote candidate ELYSIUM-derived patterns into yOS Core without reconciliation.

### 5.2 Notion failure handling

Status: `NOTION_SYNC_BLOCKED_MANUAL_INSERT_REQUIRED`

---

## 6. Claude API Protocol

### 6.1 Preferred models

- claude-sonnet-4-6 for normal substantial review
- claude-opus-4-8 for heavy architectural review

### 6.2 No silent fallback rule

- call Claude via API
- do not silently fallback to ChatGPT if Claude works
- do not simulate Claude review
- do not claim Claude reviewed anything unless Claude API actually succeeded

If Claude API fails: `CLAUDE_REVIEW_BLOCKED`

Fallback must be labeled: `PROVISIONAL_FALLBACK_REVIEW_NOT_CLAUDE`

### 6.3 When Claude is required

- book chapter critique
- major architecture review
- source-of-truth contradiction detection
- high-stakes editorial coherence
- dense philosophical / civilizational synthesis
- final review before publication candidate

---

## 7. ChatGPT API Protocol

ChatGPT may draft and synthesize. Claude reviews, critiques, detects contradictions.

Do not label ChatGPT output as Claude review.

---

## 8. Recommended Persistence by Task Type

| Task Type | Git | Mem0 | Notion | Claude |
|---|---|---|---|---|
| Canonicalization | required | required if facts change | optional | often required |
| FCS creation | required | durable facts only | optional | optional/recommended |
| Book drafting | required | durable facts only | optional | required for review |
| Notion protocol sync | optional backup | durable fact optional | required | not required |
| Small edit | optional | no | no | no |
| yOS Program Mode design | required | required if accepted | required | recommended |

---

## 9. Strategic Summary

The Git / Mem0 / Claude API Protocol ensures that yOS Program Mode is: version-controlled, memory-aware, reviewable, transparent, recoverable, honest about model/API provenance, compatible with semi-autonomous execution.
