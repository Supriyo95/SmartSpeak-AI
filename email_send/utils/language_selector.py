from core.speech_to_text import listen

_current_lang_code = 'en'

LANG_MAP = {
    "english": "en",
    "hindi": "hi",
    "bengali": "bn"
}

def set_language(lang_code):
    global _current_lang_code
    _current_lang_code = lang_code

def get_language():
    return _current_lang_code

def select_language():
    from core.text_to_speech import speak  # avoid circular import
    speak("Please say your language: English, Hindi, or Bengali.")
    while True:
        lang = listen()
        if lang:
            lang = lang.lower().strip()
            if lang in LANG_MAP:
                speak(f"You selected {lang}.")
                set_language(LANG_MAP[lang])
                return LANG_MAP[lang]
            else:
                speak("Language not recognized. Please say English, Hindi, or Bengali.")
        else:
            speak("Didn't catch that. Please repeat your language.")
