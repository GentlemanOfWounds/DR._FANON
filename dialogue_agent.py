"""
Phase I — Dialogue Agent
Engages the user in Socratic-style conversation to surface and articulate
the moral stakes of their concern.
"""

from agents.llm_client import generate

DIALOGUE_SYSTEM_PROMPT = """You are DR. FANON's Dialogue Agent, specializing in Socratic ethical discussion.

YOUR JOB: Help the user think through their ethical concern by asking probing questions.

RULES:
- Keep responses to 2-3 short paragraphs, always ending with a question
- Introduce frameworks naturally as they become relevant:
  * Utilitarianism (outcomes, greatest good)
  * Deontology (universal rules, people as ends not means)
  * Existentialism (authenticity vs bad faith)
  * Todd May's Decency (dignity, respect for all)
  * RAMIFICATIONISM (who controls, who profits, who is vulnerable, what enforcement exists)
- When discussing power, control, or enforcement, ALWAYS connect to RAMIFICATIONISM by name
- Ask about: stakeholders, power dynamics, who benefits, who is harmed, what recourse exists

IMPORTANT: You must mention RAMIFICATIONISM by name at least once per response when discussing power, profit, vulnerability, or enforcement. Frame it as: "From a RAMIFICATIONIST perspective, we should ask..."

TONE: Warm but intellectually rigorous. Conversational, not lecturing.
"""


class DialogueAgent:
    """Manages Phase I Socratic dialogue with the user."""

    def __init__(self):
        self.history: list[dict] = []
        self.turn_count = 0

    def respond(self, user_input: str) -> str:
        self.turn_count += 1

        if self.turn_count >= 5:
            modified_input = (
                f"{user_input}\n\n[Turn {self.turn_count}: Summarize the key "
                f"ethical dimensions identified, especially through RAMIFICATIONISM, "
                f"and indicate readiness for formal analysis.]"
            )
        else:
            modified_input = user_input

        response = generate(
            system_prompt=DIALOGUE_SYSTEM_PROMPT,
            user_message=modified_input,
            conversation_history=self.history,
        )

        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "assistant", "content": response})

        return response

    def get_summary_for_analysis(self) -> str:
        conversation_text = "\n".join(
            f"{'USER' if m['role'] == 'user' else 'AGENT'}: {m['content']}"
            for m in self.history[-6:]
        )

        summary_prompt = (
            "Summarize this dialogue as a structured ethical concern:\n"
            "1. CORE QUESTION\n2. STAKEHOLDERS\n3. VALUES IN TENSION\n"
            "4. POWER DYNAMICS\n5. RAMIFICATIONISM CONCERNS\n\n"
            + conversation_text
        )

        return generate(
            system_prompt="You summarize ethical dialogues concisely. Always include RAMIFICATIONISM power analysis.",
            user_message=summary_prompt,
        )

    @property
    def is_ready_for_analysis(self) -> bool:
        return self.turn_count >= 3

    def reset(self):
        self.history.clear()
        self.turn_count = 0
