#!/usr/bin/env python3
"""
DR. FANON — Agentic Ethics Reasoning System
==========================================
A voice-controlled, multi-agent AI system that reasons through ethical
dilemmas using frameworks from COSC 643 (Ethics of AI) with
RAMIFICATIONISM as the final arbiter.

Named in homage to Dr. Frantz Fanon, M.D. (1925-1961).

Three-phase pipeline:
  Phase I:   Socratic Dialogue (surface moral stakes)
  Phase II:  Multi-Framework Ethical Analysis + RAMIFICATIONISM Verdict
  Phase III: Practicable Countermeasures & Action Plan

Usage:
  python main.py              # Full voice-enabled interactive mode
  python main.py --text       # Text-only mode (no voice)
  python main.py --quick "Is facial recognition ethical?"  # Quick analysis
  python main.py --demo       # Run a built-in demo scenario

Requirements:
  - Ollama running locally with a model pulled (e.g., phi3:mini)
  - Python 3.10+
  - See requirements.txt for Python packages
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import SYSTEM_NAME, GREETING
from agents.orchestrator import Orchestrator, Phase
from agents.llm_client import check_ollama_available


BANNER = f"""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   ██████╗ ██████╗    ███████╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗║
║   ██╔══██╗██╔══██╗   ██╔════╝██╔══██╗████╗  ██║██╔═══██╗████╗  ██║║
║   ██║  ██║██████╔╝   █████╗  ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║║
║   ██║  ██║██╔══██╗   ██╔══╝  ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║║
║   ██████╔╝██║  ██║██╗██║     ██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║║
║   ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝║
║                                                                   ║
║   Agentic Ethics Reasoning System                                 ║
║   Powered by RAMIFICATIONISM                                      ║
║   In homage to Dr. Frantz Fanon, M.D. (1925-1961)                 ║
║                                                                   ║
║   COSC 643: Ethics of Artificial Intelligence                     ║
║   Maryville University — Spring 2026                              ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
"""

PHASE_LABELS = {
    Phase.DIALOGUE: "Phase I: Dialogue",
    Phase.ANALYSIS: "Phase II: Analysis",
    Phase.ACTION: "Phase III: Action",
    Phase.COMPLETE: "Complete",
}

COMMANDS_HELP = """
Commands:
  analyze / next  — Move to the next phase
  reset           — Start a new ethical inquiry
  quick <concern> — Skip dialogue, run full analysis directly
  help            — Show this help
  quit / exit     — Exit DR. FANON
"""


def run_interactive(text_only: bool = False):
    """Run the full interactive voice-enabled loop."""

    # Conditional voice import
    voice = None
    if not text_only:
        try:
            from voice.interface import VoiceInterface
            voice = VoiceInterface()
        except Exception as e:
            print(f"⚠️  Voice interface failed to initialize: {e}")
            print("   Running in text-only mode.\n")

    orchestrator = Orchestrator()

    # Print banner and greeting
    print(BANNER)

    # Check Ollama
    if check_ollama_available():
        from config import OLLAMA_MODEL
        print(f"✅ Ollama is running (model: {OLLAMA_MODEL})")
    else:
        print("❌ Ollama is NOT running!")
        print("   Please start Ollama and pull a model:")
        print("     ollama serve")
        print("     ollama pull phi3:mini")
        print(f"   Then restart {SYSTEM_NAME}.\n")
        print("   (You can still test the interface — LLM calls will show errors)")

    print(f"\n{GREETING}\n")
    print(COMMANDS_HELP)

    # Speak the greeting in separate short sentences so each completes fully
    if voice and voice.tts.available:
        voice.tts.speak(
            "I am Doctor Fanon, named in homage to the psychiatrist "
            "and philosopher Doctor Frantz Fanon."
        )
        voice.tts.speak(
            "I reason through ethical dilemmas using multiple philosophical "
            "frameworks, with Ramificationism as the final arbiter."
        )
        voice.tts.speak(
            "What ethical question is on your mind?"
        )

    # Main loop
    while True:
        # Show current phase
        phase_label = PHASE_LABELS.get(orchestrator.phase, "Unknown")
        print(f"\n[{phase_label}]")

        # Get input
        if voice and voice.voice_enabled:
            user_input = voice.get_input()
        else:
            user_input = input("\n> You: ").strip()

        if not user_input:
            continue

        # Handle meta commands
        lower = user_input.lower().strip()

        if lower in ("quit", "exit", "bye", "stop"):
            farewell_print = (
                "Thank you for engaging in ethical reasoning! As Doctor Fanon taught "
                "us, liberation requires both structural change and psychological "
                "transformation. And as RAMIFICATIONISM insists: transparency "
                "without power is toothless, fairness without remedy is theater, "
                "accountability without punishment is fiction! "
                "Now, endeavor forth to forcibly forge a more just and equitable world!!!"
            )
            print(f"\n{farewell_print}\n")
            if voice and voice.tts.available:
                voice.tts.speak(
                    "Thank you for engaging in ethical reasoning."
                )
                voice.tts.speak(
                    "As Doctor Fanon taught us, liberation requires both "
                    "structural change and psychological transformation."
                )
                voice.tts.speak(
                    "And as Ramificationism insists: transparency without power "
                    "is toothless, fairness without remedy is theater, "
                    "accountability without punishment is fiction."
                )
                voice.tts.speak(
                    "Now, endeavor forth to forcibly forge a more just and equitable world!"
                )
            break

        if lower == "help":
            print(COMMANDS_HELP)
            continue

        if lower.startswith("quick "):
            concern = user_input[6:].strip()
            if concern:
                result = orchestrator.quick_analysis(concern)
                print(f"\n{result}\n")
                if voice and voice.tts.available:
                    if "RAMIFICATIONISM" in result:
                        verdict_start = result.find("RAMIFICATIONISM")
                        voice.tts.speak(result[verdict_start:verdict_start + 800])
                orchestrator._reset()
                continue

        # Process through pipeline
        response, phase = orchestrator.process(user_input)

        # Output
        if voice:
            voice.output(response, speak=True)
        else:
            print(f"\n{response}\n")


def run_demo():
    """Run a built-in demo scenario for presentation purposes."""
    print(BANNER)
    print("═══ DEMO MODE ═══\n")

    # Check Ollama
    if not check_ollama_available():
        print("❌ Ollama is NOT running. Demo requires Ollama.")
        print("   Please run: ollama serve && ollama pull phi3:mini")
        return

    orchestrator = Orchestrator()

    demo_concern = (
        "An e-commerce website makes it nearly impossible to unsubscribe "
        "from their mailing list. They use dark patterns like tiny grey "
        "unsubscribe links, multi-step confirmation flows, and guilt-trip "
        "language like 'Are you sure you want to miss out on savings?' "
        "Is this ethical?"
    )

    print(f"DEMO CONCERN:\n\"{demo_concern}\"\n")
    print("Running full quick analysis...\n")

    result = orchestrator.quick_analysis(demo_concern)
    print(result)


def main():
    """Entry point — parse arguments and run appropriate mode."""
    args = sys.argv[1:]

    if "--demo" in args:
        run_demo()
    elif "--quick" in args:
        idx = args.index("--quick")
        concern = " ".join(args[idx + 1:])
        if concern:
            print(BANNER)
            if check_ollama_available():
                orchestrator = Orchestrator()
                result = orchestrator.quick_analysis(concern)
                print(result)
            else:
                print("❌ Ollama is not running. Please start it first.")
        else:
            print("Usage: python main.py --quick \"Your ethical concern here\"")
    else:
        text_only = "--text" in args
        run_interactive(text_only=text_only)


if __name__ == "__main__":
    main()
