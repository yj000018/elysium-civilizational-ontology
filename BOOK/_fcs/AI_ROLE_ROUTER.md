# AI Role Router

FCS routes AI tasks by role to ensure the right agent handles the right task.

## Roles and Responsibilities

### CHATGPT_CHIEF_ARCHITECT
Use for: architecture, structural decomposition, module positioning, title systems, executive summaries, reader promises, argument flow, canonical alignment, review of Manus outputs, next MPM generation.

### CLAUDE_WRITER
Use for: long-form prose, chapter/module drafting from detailed structure, narrative expansion, stylistic rewriting, transitions, tonal smoothing, continuity, readability.

### CLAUDE_REVIEWER
Use for: style review, readability review, repetition detection, flow review, literary coherence.

### MANUS_OPERATOR
Use for: repo operations, GitHub clone/branch/commit/push, batch file creation, scripts, manifests, action queue execution, resource extraction batches, validation commands, completion reports.

### FCS_SCRIPTS
Use for deterministic operations: render, validate, status, graph, resources/index generation, JSON generation.

### FOUNDER
Use for: strategic approval, final decision, taste judgment, locking major architecture, deciding when to start real drafting.

## Default Routing Table

| Action family | Default agent |
|---|---|
| Structure | CHATGPT_CHIEF_ARCHITECT |
| Titles / ToC / executive summaries | CHATGPT_CHIEF_ARCHITECT |
| Long-form writing | CLAUDE_WRITER |
| Long-form rewriting | CLAUDE_WRITER |
| Style review | CLAUDE_REVIEWER |
| Canonical review | CHATGPT_CHIEF_ARCHITECT |
| Resource extraction batch | MANUS_OPERATOR + ChatGPT review |
| Graph/index generation | FCS_SCRIPTS |
| Repo write operations | MANUS_OPERATOR |

## Claude API Rule

When an action requires Claude, Manus must: `call Claude via API`.
Use this exact operational instruction in action requests and reports. Do not merely say "use Claude". Do not silently fallback from Claude to ChatGPT if Claude works. If Claude API is unavailable, log: `Claude API unavailable — action not executed or fallback requires explicit approval.` Do not fake a Claude review.
