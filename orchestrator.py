"""
Orchestrator Agent — Coordinates the three-phase ethical reasoning pipeline.

Phase I:   Dialogue Agent (Socratic discussion)
Phase II:  Ethics Agent (multi-framework analysis + RAMIFICATIONISM verdict)
Phase III: Action Agent (practicable countermeasures)
"""

from enum import Enum, auto
from agents.dialogue_agent import DialogueAgent
from agents.ethics_agent import EthicsAgent
from agents.action_agent import ActionAgent


class Phase(Enum):
    DIALOGUE = auto()
    ANALYSIS = auto()
    ACTION = auto()
    COMPLETE = auto()


class Orchestrator:
    """
    Routes user input through the three-phase ethical reasoning pipeline.

    The orchestrator manages state transitions and passes structured data
    between agents. It supports both automatic pipeline flow and manual
    user-controlled progression.
    """

    def __init__(self):
        self.dialogue_agent = DialogueAgent()
        self.ethics_agent = EthicsAgent()
        self.action_agent = ActionAgent()

        self.phase = Phase.DIALOGUE
        self.original_concern: str = ""
        self.dialogue_summary: str = ""
        self.ethical_analysis: str = ""
        self.action_plan: str = ""

    def process(self, user_input: str) -> tuple[str, Phase]:
        """
        Process user input according to the current phase.

        Args:
            user_input: The user's spoken or typed input.

        Returns:
            Tuple of (response_text, current_phase)
        """
        # Handle meta-commands
        lower = user_input.strip().lower()
        if lower in ("skip", "next", "analyze", "move on"):
            return self._advance_phase()
        if lower in ("reset", "start over", "new question"):
            return self._reset()

        # Route to current phase
        if self.phase == Phase.DIALOGUE:
            return self._handle_dialogue(user_input)
        elif self.phase == Phase.ANALYSIS:
            return self._handle_analysis(user_input)
        elif self.phase == Phase.ACTION:
            return self._handle_action(user_input)
        else:
            return self._reset()

    def _handle_dialogue(self, user_input: str) -> tuple[str, Phase]:
        """Phase I: Socratic dialogue."""
        # Capture the original concern on the first turn
        if not self.original_concern:
            self.original_concern = user_input

        response = self.dialogue_agent.respond(user_input)

        # Check if dialogue is mature enough to suggest moving forward
        if self.dialogue_agent.is_ready_for_analysis:
            response += (
                "\n\n---\n"
                "[You can say 'analyze' to move to formal ethical analysis, "
                "or continue the dialogue.]"
            )

        return response, self.phase

    def _handle_analysis(self, user_input: str) -> tuple[str, Phase]:
        """Phase II: Multi-framework ethical analysis."""
        # If user provides additional input during analysis, incorporate it
        if user_input and user_input.lower() not in ("analyze", "yes", "go"):
            self.dialogue_summary += f"\n\nADDITIONAL USER CONTEXT: {user_input}"

        print("\n⏳ Generating multi-framework ethical analysis...")
        print("   (This may take 30-90 seconds on CPU — please be patient)\n")

        self.ethical_analysis = self.ethics_agent.analyze(self.dialogue_summary)
        self.phase = Phase.ACTION

        response = self.ethical_analysis + (
            "\n\n---\n"
            "[Say 'action' or 'next' for practicable countermeasures, "
            "or ask follow-up questions about the analysis.]"
        )
        return response, self.phase

    def _handle_action(self, user_input: str) -> tuple[str, Phase]:
        """Phase III: Actionable countermeasures."""
        print("\n⏳ Generating action plan...")
        print("   (This may take 30-60 seconds on CPU)\n")

        self.action_plan = self.action_agent.generate_actions(
            ethical_analysis=self.ethical_analysis,
            original_concern=self.original_concern,
        )
        self.phase = Phase.COMPLETE

        response = self.action_plan + (
            "\n\n═══════════════════════════════════════════════════\n"
            "DR. FANON has completed the three-phase analysis.\n"
            "Say 'new question' to start a new ethical inquiry,\n"
            "or ask follow-up questions about any phase.\n"
            "═══════════════════════════════════════════════════"
        )
        return response, self.phase

    def _advance_phase(self) -> tuple[str, Phase]:
        """Move to the next phase in the pipeline."""
        if self.phase == Phase.DIALOGUE:
            # Generate summary and advance to analysis
            print("\n⏳ Summarizing dialogue for ethical analysis...")
            self.dialogue_summary = self.dialogue_agent.get_summary_for_analysis()
            self.phase = Phase.ANALYSIS
            return self._handle_analysis("")

        elif self.phase == Phase.ANALYSIS:
            return self._handle_action("")

        elif self.phase in (Phase.ACTION, Phase.COMPLETE):
            return self._reset()

        return "I'm not sure what to do next. Say 'reset' to start over.", self.phase

    def _reset(self) -> tuple[str, Phase]:
        """Reset all state for a new ethical inquiry."""
        self.dialogue_agent.reset()
        self.phase = Phase.DIALOGUE
        self.original_concern = ""
        self.dialogue_summary = ""
        self.ethical_analysis = ""
        self.action_plan = ""

        return (
            "Ready for a new ethical inquiry. What concern would you like to explore?",
            self.phase,
        )

    def quick_analysis(self, concern: str) -> str:
        """
        Skip dialogue and run a direct analysis (for quick queries).
        Useful for demo purposes or when the user wants fast results.
        """
        self.original_concern = concern
        print("\n⏳ Running quick ethical analysis (all frameworks + RAMIFICATIONISM)...")
        print("   (This may take 60-120 seconds on CPU)\n")

        self.ethical_analysis = self.ethics_agent.quick_analyze(concern)
        self.action_plan = self.action_agent.generate_actions(
            ethical_analysis=self.ethical_analysis,
            original_concern=concern,
        )

        return (
            f"{'='*55}\n"
            f"QUICK ETHICAL ANALYSIS\n"
            f"{'='*55}\n\n"
            f"{self.ethical_analysis}\n\n"
            f"{'='*55}\n"
            f"ACTION PLAN\n"
            f"{'='*55}\n\n"
            f"{self.action_plan}"
        )
