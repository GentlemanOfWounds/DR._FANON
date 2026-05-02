# DR. FANON — Agentic Ethics Reasoning System

**COSC 643: Ethics of Artificial Intelligence | Maryville University | Spring 2026**

A voice-controlled, multi-agent AI system that reasons through ethical dilemmas using philosophical frameworks from the course, with **RAMIFICATIONISM** as the final arbiter.

## What It Does

DR. FANON guides users through a three-phase ethical reasoning pipeline:

| Phase | Agent | Function |
|-------|-------|----------|
| **I. Dialogue** | Dialogue Agent | Socratic conversation to surface moral stakes |
| **II. Analysis** | Ethics Reasoner | Multi-framework analysis + RAMIFICATIONISM verdict |
| **III. Action** | Action Agent | Practicable, lawful countermeasures |

### Ethical Frameworks Encoded

**Foundational:** Utilitarianism, Deontology, Existentialism, Egotism & Altruism, Legalism

**Course-Central:** Todd May's Decency Principle (applied to self, others, non-humans, the world)

**AI-Specific:** Five Principles (Floridi & Cowls), Asilomar Principles, Montreal Declaration, OECD AI Principles

**Personal Framework (Final Arbiter):** **RAMIFICATIONISM** — a realist, consequence-centered, power-aware ethical framework that insists on enforceable ramifications over voluntary compliance. Every analysis concludes with the Five Ramificationist Questions.

---

## Setup Instructions (Windows 11)

### 1. Install Ollama

Ollama runs local LLMs on your machine. Download from: https://ollama.com/download/windows

After installation, open a terminal and run:

```powershell
# Start the Ollama server
ollama serve

# In a NEW terminal, pull a lightweight model (suitable for CPU)
ollama pull phi3:mini
```

> **Why phi3:mini?** At ~2.3GB, it fits comfortably in 16GB RAM on CPU while providing strong instruction-following for ethical reasoning. Alternatives: `gemma2:2b` (smaller, faster), `qwen2.5:3b` (good multilingual support).

### 2. Install Python Dependencies

Requires Python 3.10+. Open a terminal in the project directory:

```powershell
# Install core packages
pip install SpeechRecognition pyttsx3

# Install PyAudio for microphone access (Windows)
pip install PyAudio
```

> **If PyAudio fails to install**, download the appropriate `.whl` from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio and install with `pip install <filename>.whl`

### 3. Run ETHICA

```powershell
# Full interactive mode with voice
python main.py

# Text-only mode (no microphone/speaker needed)
python main.py --text

# Quick analysis (skip dialogue, get straight to the verdict)
python main.py --quick "Is facial recognition in public spaces ethical?"

# Demo mode (runs a built-in dark-patterns scenario)
python main.py --demo
```

---

## Usage

### Interactive Mode

1. **Speak or type** your ethical concern
2. DR. FANON engages you in **Socratic dialogue** (Phase I), asking probing questions
3. After 3-5 exchanges, say **"analyze"** to trigger formal analysis
4. DR. FANON applies **all ethical frameworks** and renders the **RAMIFICATIONISM verdict** (Phase II)
5. Say **"next"** for **practicable countermeasures** (Phase III)
6. Say **"new question"** to start a fresh inquiry

### Commands

| Command | Action |
|---------|--------|
| `analyze` / `next` | Advance to the next phase |
| `reset` / `new question` | Start a new ethical inquiry |
| `quick <concern>` | Skip dialogue, full analysis directly |
| `help` | Show available commands |
| `quit` / `exit` | Exit DR. FANON |

---

## Architecture

```
ethics-ai/
├── main.py                    # Entry point & interactive loop
├── config.py                  # All configurable settings
├── requirements.txt           # Python dependencies
├── agents/
│   ├── llm_client.py          # Ollama API wrapper
│   ├── orchestrator.py        # Three-phase pipeline coordinator
│   ├── dialogue_agent.py      # Phase I:  Socratic dialogue
│   ├── ethics_agent.py        # Phase II: Multi-framework analysis
│   └── action_agent.py        # Phase III: Countermeasures
├── knowledge/
│   ├── frameworks.py          # All course ethical frameworks
│   └── ramificationism.py     # RAMIFICATIONISM personal framework
└── voice/
    └── interface.py           # STT (SpeechRecognition) + TTS (pyttsx3)
```

### How the Multi-Agent Architecture Works

The system uses a **single local LLM** (via Ollama) with **specialized system prompts** for each agent role. This is architecturally equivalent to running multiple fine-tuned models but feasible on CPU-only hardware:

- The **Dialogue Agent** gets a system prompt encoding Socratic method + all ethical frameworks
- The **Ethics Reasoner** gets a system prompt enforcing structured multi-framework analysis with RAMIFICATIONISM as final arbiter
- The **Action Agent** gets a system prompt focused on lawful, proportional, practicable countermeasures
- The **Orchestrator** manages state transitions and data flow between agents

### RAMIFICATIONISM in the Pipeline

RAMIFICATIONISM is not just another framework in the list — it is the **final word**. After every other framework has been applied, the Ethics Reasoner asks:

1. **Who controls** this technology?
2. **Who profits** from it?
3. **Who is made vulnerable** by it?
4. **What happens when** it causes harm — is there real recourse?
5. **What kind of social order** is it helping to create?

The verdict is direct, unflinching, historically informed, and always concludes with what **enforceable ramifications** would make ethical behavior more likely than voluntary compliance.

---

## Ethical Design of This System

This system embodies the ethical principles it analyzes:

- **Local-First Privacy**: All processing runs on your hardware. No voice data or ethical queries leave your machine.
- **Philosophical Pluralism**: Six frameworks presented before RAMIFICATIONISM renders judgment — never dogmatic.
- **Transparent Reasoning**: Every verdict shows its chain of reasoning across all frameworks.
- **Proportional Action**: The Action Agent is constrained to lawful, constructive countermeasures only.
- **Open Source**: All code, prompts, and knowledge bases are inspectable and modifiable.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Ollama not running" | Open a terminal and run `ollama serve` |
| "Model not found" | Run `ollama pull phi3:mini` |
| Slow responses | Normal for CPU inference. phi3:mini takes 30-90s per response. Reduce `num_predict` in config.py for shorter responses |
| PyAudio install fails | See the PyAudio section in Setup above |
| Voice not detected | Check Windows microphone permissions in Settings > Privacy > Microphone |
| No audio output | Check Windows sound settings; ensure pyttsx3 can find SAPI5 voices |

---

## License

Educational project — COSC 643 Final Project, Spring 2026.
