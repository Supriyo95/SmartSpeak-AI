from googletrans import Translator
from email_send.utils.language_selector import get_language

translator = Translator()

LANG_MAP = {
    'en': 'en',
    'hi': 'hi',
    'bn': 'bn'
}

def translate(text, src=None, dest=None):
    try:
        src_lang = src if src else get_language()
        dest_lang = dest if dest else get_language()
        result = translator.translate(text, src=src_lang, dest=dest_lang)
        return result.text
    except Exception as e:
        print(f"[Translation Error] {e}")
        return text
