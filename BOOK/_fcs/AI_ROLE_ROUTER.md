# AI Role Router

## Purpose
The AI Role Router defines the division of labor among the various AI agents and the human operator. It ensures that tasks are assigned to the entity best suited for them, preventing hallucinations, stylistic degradation, and structural drift.

## Roles and Responsibilities

### 1. FOUNDER (Human Operator)
- **Domain:** Ultimate authority, strategic direction, and taste.
- **Tasks:** Approves architecture, sets the tone, defines the core matrices, locks nodes, and triggers Action Requests via Obsidian.
- **Output:** Approvals, rejections, high-level prompts, locked files.

### 2. CHATGPT_CHIEF_ARCHITECT (ChatGPT o1/o3)
- **Domain:** High-level structure, logic, and canonical alignment.
- **Tasks:** Architecture design, structural decomposition, module positioning, generating `reader_promise` and `summary`, argument flow analysis, and reviewing Manus execution.
- **Output:** Structural Markdown, YAML updates, validation reports.
- **Why ChatGPT?** Superior at complex logical reasoning, following strict structural rules, and maintaining large context windows of architectural data.

### 3. CLAUDE_WRITER (Claude 3.5 Sonnet / 3 Opus)
- **Domain:** Prose generation and stylistic refinement.
- **Tasks:** Drafting long-form prose from structural prompts, narrative expansion, stylistic rewriting (Densify, Clarify), and ensuring tonal continuity.
- **Output:** Markdown prose.
- **Why Claude?** Superior at natural, non-robotic prose, adhering to specific stylistic guidelines without falling into "GPT-isms" (e.g., "In conclusion," "It is important to note").

### 4. CLAUDE_REVIEWER (Claude 3.5 Sonnet)
- **Domain:** Editorial oversight.
- **Tasks:** Style review, readability review, repetition detection, flow review.
- **Output:** Review notes, suggested revisions (as proposals).

### 5. MANUS_OPERATOR (Manus AI)
- **Domain:** Autonomous execution and repository management.
- **Tasks:** GitHub operations (clone/branch/commit/push), batch file creation, executing Python scripts, processing the Action Queue, and extracting resources.
- **Output:** File modifications, Git commits, script outputs.
- **Why Manus?** Can interact with the filesystem, run scripts, and orchestrate the workflow without constant human hand-holding.

### 6. FCS_SCRIPTS (Python)
- **Domain:** Deterministic automation.
- **Tasks:** `render.py`, `validate.py`, `status.py`, `graph.py`, `resources.py`.
- **Output:** Rendered views, validation reports, JSON graphs, Mermaid diagrams.

## Default Routing Table

| Action Family | Default Agent | Rationale |
| :--- | :--- | :--- |
| **Structure Actions** | `CHATGPT_CHIEF_ARCHITECT` | Requires logical reasoning and ontology awareness. |
| **Write Actions** | `CLAUDE_WRITER` | Requires high-quality, natural prose generation. |
| **Rewrite Actions** | `CLAUDE_WRITER` | Requires stylistic nuance and tone matching. |
| **Check Actions (Logic)** | `CHATGPT_CHIEF_ARCHITECT` | Requires structural analysis and canonical alignment. |
| **Check Actions (Style)** | `CLAUDE_REVIEWER` | Requires editorial sensitivity. |
| **Resource Actions** | `MANUS_OPERATOR` | Requires filesystem scanning and batch file creation. |
| **Output/Render Actions** | `FCS_SCRIPTS` | Must be 100% deterministic and reproducible. |

## The Claude API Rule

When an action requires Claude (e.g., `CLAUDE_WRITER`), Manus MUST call Claude via the API. 
- **Instruction:** `call Claude via API`.
- **Constraint:** Do not silently fallback to ChatGPT for prose generation. If the Claude API is unavailable, Manus must log: `Claude API unavailable — action blocked` and await Operator instruction.
