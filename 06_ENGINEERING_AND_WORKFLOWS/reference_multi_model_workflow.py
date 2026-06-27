#!/usr/bin/env python3
"""
Reference Multi-Model Workflow Implementation
Correct provider separation and fallback logging.
"""
import os
import json
from datetime import datetime
from pathlib import Path

# ============================================================
# PROVIDER CLIENTS
# ============================================================

def get_openai_client():
    """OpenAI/ChatGPT — use for drafting, synthesis, architectural decisions."""
    from openai import OpenAI
    return OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_anthropic_client():
    """Anthropic/Claude — use for critical review, contradiction detection."""
    from anthropic import Anthropic
    return Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def get_gemini_client():
    """Google Gemini — use for long-context synthesis only."""
    import google.generativeai as genai
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    return genai

# ============================================================
# CALL FUNCTIONS (correctly named)
# ============================================================

def call_chatgpt(prompt: str, system: str = "", model: str = "gpt-4o") -> str:
    """Call ChatGPT via OpenAI API."""
    client = get_openai_client()
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content

def call_claude(prompt: str, system: str = "", model: str = "claude-sonnet-4-20250514") -> str:
    """Call Claude via Anthropic API. MUST actually call Anthropic."""
    client = get_anthropic_client()
    response = client.messages.create(
        model=model,
        max_tokens=4000,
        system=system if system else "You are Claude, Critical Reviewer.",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def call_chatgpt_as_reviewer_fallback(prompt: str) -> str:
    """Fallback: use GPT-4o when Claude is unavailable. EXPLICITLY NAMED."""
    return call_chatgpt(prompt, system="You are acting as Critical Reviewer (Claude fallback).")

# ============================================================
# LOGGING
# ============================================================

def log_api_call(log_path: Path, call_id: str, requested: str, executed: str,
                 task_type: str, input_desc: str, output_file: str,
                 success: bool = True, fallback: bool = False, reason: str = ""):
    """Log every API call with full provenance."""
    entry = {
        "call_id": call_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "requested_engine": requested,
        "executed_engine": executed,
        "task_type": task_type,
        "input_file_or_prompt": input_desc,
        "output_file": output_file,
        "success": success,
        "fallback_used": fallback,
        "reason_for_fallback": reason
    }
    existing = []
    if log_path.exists():
        existing = json.loads(log_path.read_text())
    existing.append(entry)
    log_path.write_text(json.dumps(existing, indent=2))

# ============================================================
# WORKFLOW EXAMPLE
# ============================================================

def generate_document(doc_id: str, prompt: str, log_path: Path):
    """Standard workflow: ChatGPT drafts, Claude reviews, ChatGPT revises."""
    # Step 1: Draft
    draft = call_chatgpt(prompt, system="You are the Chief Architect.")
    log_api_call(log_path, f"draft_{doc_id}", "ChatGPT", "GPT-4o", "DRAFTING", prompt[:100], f"{doc_id}_draft.md")
    
    # Step 2: Review
    try:
        review = call_claude(f"Review this document critically:\n\n{draft}")
        log_api_call(log_path, f"review_{doc_id}", "Claude", "Claude-3.5-Sonnet", "REVIEW", f"{doc_id}_draft.md", f"{doc_id}_review.md")
    except Exception as e:
        review = call_chatgpt_as_reviewer_fallback(f"Review this document critically:\n\n{draft}")
        log_api_call(log_path, f"review_{doc_id}", "Claude", "GPT-4o", "REVIEW", f"{doc_id}_draft.md", f"{doc_id}_review.md",
                     fallback=True, reason=str(e))
    
    # Step 3: Revise
    final = call_chatgpt(f"Revise based on this feedback:\n{review}\n\nOriginal:\n{draft}")
    log_api_call(log_path, f"revise_{doc_id}", "ChatGPT", "GPT-4o", "REVISION", f"{doc_id}_review.md", f"{doc_id}_final.md")
    
    return final
