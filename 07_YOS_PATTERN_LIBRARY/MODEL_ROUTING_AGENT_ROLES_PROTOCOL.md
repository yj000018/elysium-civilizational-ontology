# Model Routing & Agent Roles Protocol — v0.1

**Status:** Candidate yOS Program Mode Protocol
**Source:** ELYSIUM operational development
**Version:** v0.1
**Integration status:** Pending yOS Notion reconciliation
**Authority:** Founder + ChatGPT Chief Architect review required before yOS Core integration

> ⚠️ This document defines a candidate yOS Program Mode protocol. It must be reconciled with existing yOS Notion documentation before being promoted into yOS Core.

---

## 1. Purpose

The Model Routing & Agent Roles Protocol defines which AI model or agent is responsible for each type of task in yOS Program Mode.

---

## 2. Agent Roster

| Agent | Role | Primary Use Cases |
|---|---|---|
| Manus | Executive Orchestrator | Multi-step execution, GitHub, Notion, file ops, program management |
| ChatGPT (GPT-4o / GPT-5) | Chief Architect | Architecture design, strategic decisions, vision alignment |
| Claude API (Opus / Sonnet) | Review Officer | Document review, quality audit, canonicalization |
| Gemini | Long Document Processor | Very long documents, multi-file synthesis |
| Grok | Web / X Intelligence | Real-time web search, X/Twitter analysis |
| Perplexity | Research Synthesis | Research queries, fact verification |
| n8n | Automation Orchestrator | Complex workflow automation, webhooks, scheduled tasks |

---

## 3. Model Selection Matrix

| Task Type | Primary Model | Secondary Model |
|---|---|---|
| MPM execution | Manus | — |
| GitHub operations | Manus | — |
| Notion operations | Manus (MCP) | — |
| Architecture design | ChatGPT | Manus |
| Document review | Claude API | Manus |
| Long doc synthesis | Gemini | Claude API |
| Research | Perplexity | Grok |
| Web search | Grok | Perplexity |
| Automation workflows | n8n | Manus |
| Code generation | Manus | Claude API |
| Strategic decisions | ChatGPT | Founder |

---

## 4. Authority Hierarchy

1. Founder / Yannick — final authority on all decisions
2. ChatGPT Chief Architect — architecture and strategy authority
3. Manus — execution authority
4. Claude API — review authority
5. Other models — specialist support, no authority

No model may override the Founder's decisions.
No model may promote candidate patterns to yOS Core without Founder + Chief Architect sign-off.

---

## 5. Cost Optimization Rules

- Use Manus Normal (not Max) for documentation tasks
- Use Claude Sonnet (not Opus) for review unless Opus is explicitly required
- Batch multiple documents in a single Claude API call when possible
- Use Perplexity for research before falling back to GPT-4o
- Do not use Manus Max for tasks that Manus Normal can handle

---

## 6. Notion Reference

Notion page: yOS / Program Mode / 11 Model Routing & Agent Roles Protocol
