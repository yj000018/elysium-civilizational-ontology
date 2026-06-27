# Action Request Model

Action requests are the primary mechanism for commanding AI operations in FCS.

## Structure

Action requests are stored in:
- `BOOK/_fcs/action_requests/active/`
- `BOOK/_fcs/action_requests/completed/`
- `BOOK/_fcs/action_requests/archived/`
- `BOOK/_fcs/action_requests/templates/`

## Writeback Modes

Allowed writeback modes:
- `proposal`
- `direct_write`
- `patch`
- `review_only`

### Defaults

| Action | Default writeback mode |
|---|---|
| Write draft | proposal |
| Rewrite | proposal |
| Shorten | proposal |
| Structure split/merge | proposal |
| Resource extraction | proposal or direct_write_to_resources_pending |
| Render view | direct_write to views/output |
| Status report | direct_write to views/output |
| Validate | review_only |

Claude must not overwrite source modules directly by default. ChatGPT Chief Architect should produce architecture proposals/patches. Manus may directly write scaffolds, scripts, views, reports, templates, manifests, and generated indexes.
