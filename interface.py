"""
Voice Interface — Speech-to-Text and Text-to-Speech.

STT: SpeechRecognition + Google Web API.
TTS: Windows COM SAPI.SpVoice via a tiny VBScript file.
     No pyttsx3. No .NET assembly. No PowerShell System.Speech.
     Just the raw Windows speech COM object — the fastest possible path.
"""

import os
import subprocess
import sys
import tempfile
import time
from config import STT_ENGINE, TTS_RATE, TTS_VOLUME


# ── Speech-to-Text ──────────────────────────────────────────────────────────

class SpeechToText:

    def __init__(self):
        try:
            import speech_recognition as sr
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            self.sr = sr
            self.available = True

            self.recognizer.pause_threshold = 6.0
            self.recognizer.non_speaking_duration = 2.0
            self.recognizer.dynamic_energy_threshold = True
            self.recognizer.energy_threshold = 300

            print("🎤 Calibrating microphone...")
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=3)
            print("🎤 Microphone ready. (pause threshold: 6s)\n")

        except (ImportError, OSError) as e:
            print(f"⚠️  Voice input unavailable: {e}")
            self.available = False

    def listen(self, timeout=20, phrase_time_limit=60):
        if not self.available:
            return None

        for attempt in range(2):
            try:
                if attempt == 0:
                    print("\n🎤 Listening... (speak when ready, up to 60 seconds)")
                else:
                    print("🎤 Trying again...")

                with self.microphone as source:
                    if attempt > 0:
                        self.recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = self.recognizer.listen(
                        source, timeout=timeout, phrase_time_limit=phrase_time_limit
                    )

                print("⏳ Transcribing...")
                text = self.recognizer.recognize_google(audio)
                print(f'📝 Heard: "{text}"')
                return text

            except self.sr.WaitTimeoutError:
                if attempt == 0:
                    print("⏰ No speech detected. Trying once more...")
                else:
                    print("⏰ No speech detected after two attempts.")
            except self.sr.UnknownValueError:
                if attempt == 0:
                    print("❓ Couldn't catch that. Trying once more...")
                else:
                    print("❓ Couldn't understand after two attempts.")
            except Exception as e:
                print(f"⚠️  Error: {e}")

        return None


# ── Text-to-Speech ──────────────────────────────────────────────────────────

def _clean_for_speech(text):
    for old, new in [
        ("═", " "), ("─", " "), ("**", ""), ("##", ""), ("---", " "),
        ("***", ""), ("[", ""), ("]", ""), ("•", ""), ("\n", " "),
        ("DR. FANON", "Doctor Fanon"), ("Dr. FANON", "Doctor Fanon"),
        ("DR.", "Doctor"), ("Dr.", "Doctor"), ("M.D.", "M D"),
        ("vs.", "versus"), ("e.g.", "for example"), ("i.e.", "that is"),
        ("etc.", "etcetera"), ("FTC", "F T C"), ("FCC", "F C C"),
        ("GDPR", "G D P R"), ("CCPA", "C C P A"),
    ]:
        text = text.replace(old, new)
    # Remove characters that break VBScript strings
    text = text.replace('"', "").replace("'", "").replace("`", "")
    while "  " in text:
        text = text.replace("  ", " ")
    return text.strip()


class TextToSpeech:
    """
    TTS using a tiny VBScript that calls SAPI.SpVoice directly.
    This is the absolute simplest speech path on Windows.
    No Python library. No .NET. No assembly loading.
    Just: write a .vbs file → run it with cscript → speech comes out.
    """

    def __init__(self):
        self.available = False
        # Test: can we run cscript?
        try:
            result = subprocess.run(
                ["cscript", "//Nologo", "//?"],
                capture_output=True, timeout=5
            )
            self.available = True
            print("🔊 TTS ready (Windows SAPI.SpVoice via VBScript)")
        except Exception:
            # Fallback: try with full path
            try:
                self._cscript = r"C:\Windows\System32\cscript.exe"
                result = subprocess.run(
                    [self._cscript, "//Nologo", "//?"],
                    capture_output=True, timeout=5
                )
                self.available = True
                print("🔊 TTS ready (Windows SAPI.SpVoice via VBScript)")
            except Exception as e:
                print(f"⚠️  TTS unavailable: {e}")
                self._cscript = "cscript"

        if not hasattr(self, "_cscript"):
            self._cscript = "cscript"

    def speak(self, text):
        if not self.available:
            return

        clean = _clean_for_speech(text)
        if not clean or len(clean) < 3:
            return

        # Write a tiny VBScript that speaks the text
        # SAPI.SpVoice rate: -10 to 10. Convert from WPM.
        rate = max(-10, min(10, (TTS_RATE - 150) // 25))
        volume = int(TTS_VOLUME * 100)

        vbs_content = (
            f'Set oVoice = CreateObject("SAPI.SpVoice")\n'
            f'oVoice.Rate = {rate}\n'
            f'oVoice.Volume = {volume}\n'
            f'oVoice.Speak "{clean}"\n'
        )

        tmp_path = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".vbs", delete=False, encoding="ascii",
                errors="replace"
            ) as f:
                f.write(vbs_content)
                tmp_path = f.name

            result = subprocess.run(
                [self._cscript, "//Nologo", tmp_path],
                capture_output=True, text=True, timeout=120
            )
            if result.returncode != 0 and result.stderr.strip():
                print(f"   ⚠️ TTS: {result.stderr.strip()[:100]}")

        except subprocess.TimeoutExpired:
            print("   ⚠️ Speech timed out")
        except Exception as e:
            print(f"   ⚠️ TTS error: {e}")
        finally:
            if tmp_path:
                try:
                    os.unlink(tmp_path)
                except OSError:
                    pass

    def stop(self):
        pass


# ── Combined Voice Interface ────────────────────────────────────────────────

class VoiceInterface:

    def __init__(self):
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.voice_enabled = self.stt.available

    def get_input(self, prompt=""):
        if prompt:
            print(prompt)
        if self.voice_enabled:
            text = self.stt.listen()
            if text:
                return text
            print("(Type your input instead)")
        return input("> You: ").strip()

    def output(self, text, speak=True):
        print(f"\n{text}\n")

        if speak and self.tts.available:
            lines = []
            for line in text.split("\n"):
                s = line.strip()
                if (s and not s.startswith("═") and not s.startswith("─")
                    and not s.startswith("[") and not s.startswith("---")
                    and "new question" not in s.lower()
                    and "follow-up" not in s.lower()
                    and "Say '" not in s):
                    lines.append(s)

            speakable = " ".join(lines)
            if len(speakable) > 12_000:
                cutoff = speakable[:12_000].rfind(". ")
                if cutoff > 400:
                    speakable = speakable[:cutoff + 1]
                else:
                    speakable = speakable[:1000]

            self.tts.speak(speakable)
