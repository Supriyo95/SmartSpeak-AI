from email_send.utils.validators import spoken_to_email, is_valid_email
from email_send.email_sender import send_email

class EmailAgent:
    def __init__(self):
        self.recipient = None
        self.subject = None
        self.message = None
        self.language = "english"  

    def reset(self):
        self.recipient = None
        self.subject = None
        self.message = None

    # --- Setters with Debug ---
    def set_language(self, language):
        self.language = language.lower().strip()
        # print(f"[DEBUG] Language set to: {self.language}")

    def set_recipient(self, email):
        self.recipient = email
        # print(f"[DEBUG] Final recipient email set to: {self.recipient}")

    def set_subject(self, subject):
        self.subject = subject.strip()
        # print(f"[DEBUG] Final subject set to: {self.subject}")

    def set_message(self, message):
        self.message = message.strip()
        # print(f"[DEBUG] Final message set to: {self.message}")

    # --- Email Parsing and Validation ---
    def parse_email(self, raw_email):
        # print(f"[DEBUG] Raw spoken email: {raw_email}")
        parsed = spoken_to_email(raw_email)
        # print(f"[DEBUG] Parsed email: {parsed}")
        return parsed

    def validate_email(self, email):
        valid = is_valid_email(email)
        # print(f"[DEBUG] Email validation result: {valid}")
        return valid

    # --- Intent Detection ---
    def detect_intent(self, user_input):
        text = user_input.lower().strip()

        # Confirmation and exit intents
        if any(word in text for word in ['yes', 'confirm', 'ok', 'okay', 'sure', 'go ahead']):
            return 'confirm'
        elif any(word in text for word in ['exit', 'quit', 'close', 'stop', 'no thanks', 'no thank you']):
            return 'exit'
        elif 'send email' in text:
            return 'send_email'
        elif 'change subject' in text or 'edit subject' in text:
            return 'change_subject'
        elif 'change message' in text or 'edit message' in text:
            return 'change_message'
        elif 'change email' in text or 'change recipient' in text or 'edit email' in text:
            return 'change_recipient'
        else:
            return 'unknown'

    # --- Email Sending Logic ---
    def send_email(self):
        # print("\n[DEBUG] Preparing to send the following email:")
        print(f"To: {self.recipient}")
        print(f"Subject: {self.subject}")
        print(f"Message: {self.message}")

        if not self.recipient or not self.subject or not self.message:
            return "Email details are incomplete."

        if not self.validate_email(self.recipient):
            return f"The email address '{self.recipient}' is invalid."

        success = send_email(self.recipient, self.subject, self.message)
        if success:
            return "Email sent successfully."
        else:
            return "Failed to send email."

