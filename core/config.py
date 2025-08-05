import google.generativeai as genai

# --- 🔐 OPENAI / Gemini Config ---
OPENAI_API_KEY = "your_openai_api_key"  # Replace with your actual OpenAI API key

def configure_gemini(api_key: str = OPENAI_API_KEY, model_name: str = "gemini-1.5-flash"):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name=model_name)
    return model.start_chat()

# --- 📧 SMTP Email Config ---
SMTP_CONFIG = {
    "sender_email": "your_email",  # Replace with your actual email
    "app_password": "your_app_password",  # Replace with your actual app password
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 465
}