"""
Configuration for the Agentic Ethics Reasoning System.
Tuned for CPU-only deployment on a Dell Inspiron 3501 (i5-1035G1, 16GB RAM).
"""

# ---------------------------------------------------------------------------
# LLM Configuration (Ollama)
# ---------------------------------------------------------------------------
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "phi3:mini"

# Generation parameters — tuned for CPU-only i5-1035G1
OLLAMA_OPTIONS = {
    "temperature": 0.7,
    "top_p": 0.9,
    "num_predict": 512,      # Modulation alters length of responses
    "repeat_penalty": 1.15,
    "num_ctx": 2048,
}

# ---------------------------------------------------------------------------
# Voice Configuration
# ---------------------------------------------------------------------------
STT_ENGINE = "google"
VOSK_MODEL_PATH = "vosk-model-small-en-us-0.15"
TTS_ENGINE = "pyttsx3"
TTS_RATE = 175
TTS_VOLUME = 0.9

# ---------------------------------------------------------------------------
# Agent Configuration
# ---------------------------------------------------------------------------
MAX_DIALOGUE_TURNS = 8
AUTO_PIPELINE = True

# ---------------------------------------------------------------------------
# System Behavior
# ---------------------------------------------------------------------------
SYSTEM_NAME = "DR. FANON"
GREETING = (
    f"I am {SYSTEM_NAME}, an agentic ethics reasoning system built on the "
    f"ethical frameworks studied in COSC 643 — including utilitarianism, "
    f"deontology, existentialism, Todd May's decency principle, and the "
    f"personal framework of RAMIFICATIONISM.\n\n"
    f"This system is named in homage to Dr. Frantz Fanon, M.D. (1925-1961), the "
    f"Martinican psychiatrist, philosopher, and revolutionary whose work "
    f"deeply influenced post-colonial studies, critical theory, and national "
    f"liberation movements worldwide. Dr. Fanon is best known for his "
    f"psychological analysis of the effects of colonial subjugation on the "
    f"human psyche and his advocacy for revolutionary action as a means of "
    f"decolonization and healing for the oppressed. His insistence that "
    f"liberation requires both structural change and psychological "
    f"transformation mirrors RAMIFICATIONISM's demand that ethics be rooted "
    f"in enforceable consequence, not mere sentiment.\n\n"
    f"I reason through ethical dilemmas and help you arrive at actionable "
    f"conclusions.\n\n"
    f"Speak or type your ethical concern, and I will:\n"
    f"  I.   Discuss it with you through Socratic dialogue\n"
    f"  II.  Analyze it through multiple ethical lenses\n"
    f"  III. Help you formulate a practicable response\n\n"
    f"What ethical question is on your mind?"
)
