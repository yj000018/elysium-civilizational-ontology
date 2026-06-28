---
id: AR_005
title: Review Opening Part
type: action_request
status: DRAFT_ACTION
target: PART_01
assigned_role: CLAUDE_REVIEWER
execute_now: false
---

# Action Request: Review Opening Part

## Objective
Perform a stylistic and structural review of the drafted Part 01.

## Context
Ensures the 4 drafted modules flow together and adhere to the Voice Guide.

## Input Files
- `BOOK/manuscript/01_opening/modules/*.md`
- `BOOK/_fcs/BOOK_STYLE_AND_VOICE_GUIDE.md`

## Instructions for Manus
1. Compile the 4 modules into a single text block.
2. Invoke Claude API with the Reviewer persona to critique the text.
3. Save the review report to `BOOK/reviews/01_opening_review.md`.
4. Update node statuses to `REVISION` if needed, or `DRAFT_INTEGRATED_QA_PENDING`.
