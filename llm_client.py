"""
LLM Client — wraps Ollama HTTP API for local model inference.
"""

import json
import urllib.request
import urllib.error
from config import OLLAMA_BASE_URL, OLLAMA_MODEL, OLLAMA_OPTIONS


def check_ollama_available() -> bool:
    """Check if Ollama server is reachable."""
    try:
        req = urllib.request.Request(f"{OLLAMA_BASE_URL}/api/tags")
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status == 200
    except Exception:
        return False


def generate(system_prompt: str, user_message: str, conversation_history: list[dict] | None = None) -> str:
    """
    Send a prompt to the local Ollama model and return the response text.
    """
    messages = [{"role": "system", "content": system_prompt}]

    if conversation_history:
        # Keep only last 4 messages to stay within context budget
        messages.extend(conversation_history[-4:])

    messages.append({"role": "user", "content": user_message})

    payload = {
        "model": OLLAMA_MODEL,
        "messages": messages,
        "stream": False,
        "options": OLLAMA_OPTIONS,
    }

    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            f"{OLLAMA_BASE_URL}/api/chat",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        # 10 minute timeout for CPU-only i5-1035G1
        with urllib.request.urlopen(req, timeout=600) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result.get("message", {}).get("content", "[No response generated]")
    except urllib.error.URLError as e:
        return (
            f"[LLM ERROR: Could not reach Ollama at {OLLAMA_BASE_URL}. "
            f"Make sure Ollama is running with: ollama serve]\n"
            f"Details: {e}"
        )
    except Exception as e:
        return f"[LLM ERROR: {e}]"
