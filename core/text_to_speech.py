import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import platform
import tempfile
from datetime import datetime
from gtts import gTTS
import pygame
from googletrans import Translator
from email_send.utils.language_selector import get_language

def speak(text):
    lang = get_language()
    print(f"Bot ({lang}): {text}")

    try:
        if lang in ['hi', 'bn']:
            translator = Translator()
            translated_text = translator.translate(text, src='en', dest=lang).text
        else:
            translated_text = text

        audio_dir = "audio"
        os.makedirs(audio_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(audio_dir, f"audio_{timestamp}.mp3")

        tts = gTTS(text=translated_text, lang=lang, tld="co.in")
        tts.save(file_path)

        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()

    except Exception as e:
        print(f"[TTS ERROR] {e}")
        print(f"[Fallback] {text}")