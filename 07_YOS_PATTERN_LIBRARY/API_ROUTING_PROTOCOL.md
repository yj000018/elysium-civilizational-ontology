# API ROUTING PROTOCOL

**Date:** 2026-06-27
**Status:** CANONICAL

## 1. Principle
The engine claimed in documentation MUST match the actual API used. Falsifying engine provenance undermines the integrity of the yOS architecture.

## 2. Correct Function Naming
- `call_chatgpt()` — calls OpenAI API
- `call_claude()` — calls Anthropic API
- `call_chatgpt_as_reviewer_fallback()` — explicitly named fallback

## 3. Forbidden Patterns
- `def call_claude()` that actually calls OpenAI
- Claiming "Claude reviewed" without actual Anthropic API call
- Omitting fallback logging

## 4. Fallback Protocol
If Claude API fails:
1. Log the failure with error message
2. Use `call_chatgpt_as_reviewer_fallback()` (explicitly named)
3. Mark output as `review_engine: GPT-4o (Fallback due to: [reason])`
4. Never claim Claude reviewed

## 5. Provenance Metadata
Every generated document must include:
- `drafting_engine`
- `review_engine` (with fallback note if applicable)
- `revision_engine`
- `orchestration_engine: Manus`
