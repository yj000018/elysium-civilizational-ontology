# Action Dashboard

*This dashboard is designed to be rendered by Dataview in Obsidian.*

## Pending Action Requests

```dataview
TABLE 
  action as "Action", 
  target as "Target", 
  preferred_agent as "Agent", 
  priority as "Priority"
FROM "BOOK/_fcs/action_requests/active"
WHERE status = "READY_FOR_AI"
SORT priority DESC
```

## Actions In Progress

```dataview
TABLE 
  action as "Action", 
  target as "Target", 
  preferred_agent as "Agent"
FROM "BOOK/_fcs/action_requests/active"
WHERE status = "IN_PROGRESS"
```

## Actions Needing Founder Review

```dataview
TABLE 
  action as "Action", 
  target as "Target"
FROM "BOOK/_fcs/action_requests/active"
WHERE status = "AI_PROPOSAL_READY"
```
