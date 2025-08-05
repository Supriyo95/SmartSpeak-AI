import smtplib
from email.message import EmailMessage
from word2number import w2n
from core.text_to_speech import speak
from core.speech_to_text import listen
from core.config import SMTP_CONFIG

# Send an email to the CEO using the provided email address
def send_email_to_ceo(email_str):
    if not email_str:
        speak("No email address found.")
        return

    email_list = [e.strip() for e in email_str.split(",") if e.strip()]
    chosen_email = ""

    if len(email_list) == 1:
        chosen_email = email_list[0]
    elif len(email_list) > 1:
        speak("Multiple emails found.")
        for idx, email in enumerate(email_list, 1):
            speak(f"Option {idx}: {email}")

        while True:
            choice = listen("Please say the number of your chosen email.")
            cleaned = choice.lower().strip()
            for prefix in ["option ", "number ", "email ", "choice "]:
                if cleaned.startswith(prefix):
                    cleaned = cleaned.replace(prefix, "").strip()
                    break

            try:
                selected_index = w2n.word_to_num(cleaned)
            except:
                selected_index = int(cleaned) if cleaned.isdigit() else None

            if selected_index and 1 <= selected_index <= len(email_list):
                chosen_email = email_list[selected_index - 1]
                break

    else:
        speak("No valid email addresses found.")
        return

    subject = listen("What should be the subject of the email?")
    body = listen("What should the email say?")
    confirmation = listen(f"Do you want to send the email to {chosen_email}? Say yes or no.")

    if "yes" not in confirmation:
        speak("Email sending cancelled.")
        return

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SMTP_CONFIG['sender_email']
    msg['To'] = chosen_email
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL(SMTP_CONFIG['smtp_server'], SMTP_CONFIG['smtp_port']) as smtp:
            smtp.login(SMTP_CONFIG['sender_email'], SMTP_CONFIG['app_password'])
            smtp.send_message(msg)
        speak("Email sent successfully.")
    except Exception as e:
        speak(f"Failed to send email: {e}")
