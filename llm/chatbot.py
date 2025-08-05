from core.config import configure_gemini
from core.text_to_speech import speak
from email_send.utils.language_selector import get_language
from core.translator import translate

API_KEY = "your-gemini-api-key"  # Replace with your actual Gemini API key

chat = configure_gemini(API_KEY)

def get_bot_response(prompt: str) -> str:
    lang_code = get_language()

    # Step 1: Translate prompt to English if needed
    if lang_code != "en":
        try:
            prompt = translate(prompt, src=lang_code, dest="en")
        except Exception as e:
            print(f"[Translation Error - input] {e}")

    # Step 2: Send to Gemini
    try:
        response = chat.send_message(prompt)
        reply = response.text
    except Exception as e:
        print("Gemini Error:", str(e))
        speak("Oops! Something went wrong.")
        return "Sorry, something went wrong."

    # Step 3: Translate response back to selected language (if needed)
    if lang_code != "en":
        try:
            reply = translate(reply, src="en", dest=lang_code)
        except Exception as e:
            print(f"[Translation Error - output] {e}")

    return reply  # final translated reply to be printed + spoken
