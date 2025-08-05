import smtplib
from email.mime.text import MIMEText
from email_send.secret import GMAIL_EMAIL, GMAIL_APP_PASSWORD

def send_email(to_email, subject, message):
    try:
        print(f"\nPreparing to send email to: {to_email}")
        print(f"Subject: {subject}")
        print(f"Body: {message}\n")

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = GMAIL_EMAIL
        msg['To'] = to_email

        # print("[DEBUG] Connecting to Gmail SMTP...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            # print("[DEBUG] Logging into Gmail SMTP...")
            server.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)

            # print("[DEBUG] Sending email...")
            server.send_message(msg)
            # print("[DEBUG] SMTP send response: {}")

        print("Email sent successfully.\n")
        return "Email sent successfully."

    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
        return f"Failed to send email: {e}"
