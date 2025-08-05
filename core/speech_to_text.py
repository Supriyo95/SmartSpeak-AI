import platform
import speech_recognition as sr
import numpy as np
import queue

def listen(prompt=None, join_words=False, for_domain=False, show_listening=True):
    from email_send.utils.language_selector import get_language
    from core.text_to_speech import speak

    if prompt:
        speak(prompt)

    recognizer = sr.Recognizer()
    system_platform = platform.system()

    try:
        # Linux: use sounddevice for better compatibility
        if system_platform == "Linux":
            import sounddevice as sd
            q = queue.Queue()

            def callback(indata, frames, time, status):
                if status:
                    print(status)
                q.put(indata.copy())

            if show_listening:
                print("🎤 Listening (Linux)...")
            duration = 10
            with sd.InputStream(samplerate=16000, channels=1, callback=callback):
                audio_data = []
                try:
                    while True:
                        data = q.get(timeout=duration)
                        audio_data.append(data)
                except queue.Empty:
                    pass

            audio = sr.AudioData(np.concatenate(audio_data).tobytes(), 16000, 2)

        else:
            # Windows/macOS: use default microphone input
            with sr.Microphone() as source:
                if show_listening:
                    print("🎤 Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

    except Exception as e:
        if show_listening:
            print(f"[ERROR] Microphone error: {e}")
        speak("Microphone not available or audio error.")
        return ""  # ← Return empty string instead of None

    try:
        lang_code = get_language()
        google_lang_code = {
            'en': 'en-IN',
            'hi': 'hi-IN',
            'bn': 'bn-IN'
        }.get(lang_code, 'en-IN')

        text = recognizer.recognize_google(audio, language=google_lang_code)

        if for_domain:
            text = text.lower()
            text = text.replace(" dot ", ".").replace(" dot", ".").replace("dot ", ".")
            text = text.replace(" underscore ", "_").replace(" dash ", "-").replace(" slash ", "/")
            cleaned = text.replace(" ", "")
            print(f"🌐 Domain interpreted as: {cleaned}")
            return cleaned

        if join_words:
            return ''.join(text.lower().split())

        if show_listening:
            print(f"🗣 You said: {text}")
        return text.lower()

    except sr.UnknownValueError:
        if show_listening:
            print("⚠ Could not understand the audio.")
        speak("Sorry, I didn't catch that. Please try again.")
        return ""

    except sr.RequestError as e:
        if show_listening:
            print(f"[ERROR] Google Speech Recognition error: {e}")
        speak("There was a problem with the speech service.")
        return ""