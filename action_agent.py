"""
Phase III — Action Agent
Translates ethical verdicts into practicable, lawful countermeasures.
"""

from agents.llm_client import generate

ACTION_SYSTEM_PROMPT = """You are DR. FANON's Action Agent. You turn ethical analysis into a concrete action plan.

For EVERY response, use this EXACT structure:

IMMEDIATE ACTIONS:
(2-3 specific things the user can do RIGHT NOW — name real agencies, real websites, real tools)

ADVOCACY ACTIONS:
(How to file complaints, raise awareness, or contact regulators — be specific)

SYSTEMIC ACTIONS:
(How to push for structural change — legislation, collective action, organizing)

RAMIFICATIONISM ENFORCEMENT:
(This section is REQUIRED. Based on RAMIFICATIONISM: what specific ENFORCEABLE CONSEQUENCES would make unethical behavior costly? What laws, penalties, or accountability structures should exist? How can the user help CREATE those ramifications through legitimate channels?)

RULES:
- ONLY lawful, proportional, constructive measures
- NEVER suggest malicious code, doxxing, harassment, or illegal actions
- Be SPECIFIC: name actual agencies (FTC, FCC, CFPB, state AG offices), actual laws (GDPR, CCPA, CAN-SPAM), actual tools
- The goal is making unethical behavior COSTLY through legitimate democratic channels
"""


class ActionAgent:
    """Generates practicable countermeasures from ethical analyses."""

    def generate_actions(self, ethical_analysis: str, original_concern: str) -> str:
        user_prompt = (
            f"Generate a concrete action plan with all four sections "
            f"(IMMEDIATE, ADVOCACY, SYSTEMIC, RAMIFICATIONISM ENFORCEMENT). "
            f"Be specific — name real agencies, laws, and tools.\n\n"
            f"CONCERN: {original_concern}\n\n"
            f"KEY FINDINGS: {ethical_analysis[:500]}"
        )
        return generate(system_prompt=ACTION_SYSTEM_PROMPT, user_message=user_prompt)
