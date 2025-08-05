from core.speech_to_text import listen
from core.text_to_speech import speak
from email_send.utils.language_selector import select_language
from email_send.agent import EmailAgent
from song_player.agents.song_agent import SongAgent
from llm.chatbot import get_bot_response

# From summarizer bot
from core.scraper import scrape_homepage
from core.summarizer import summarize_content_with_openai
from emailer.sender import send_email_to_ceo

# email sending 
def handle_email(agent):
    agent.reset()
    speak("Tell me the recipient's email address.")
    while True:
        raw_email = listen()
        if not raw_email:
            speak("Didn't catch that. Try again.")
            continue
        email = agent.parse_email(raw_email)
        if email:
            agent.recipient = email
            break
        speak("Invalid email. Say it like 'john dot doe at gmail dot com'.")

    speak("What is the subject?")
    while True:
        subject = listen()
        if subject:
            agent.subject = subject
            break
        speak("Please repeat the subject.")

    speak("Tell me the message.")
    while True:
        message = listen()
        if message:
            agent.message = message
            break
        speak("Please say the message again.")

    while True:
        speak(f"You're sending to {agent.recipient} with subject '{agent.subject}' and message: {agent.message}. Should I send it?")
        confirm = listen()
        if not confirm:
            speak("Didn't catch that. Say 'yes', 'no', or what you want to change.")
            continue

        confirm = confirm.lower()
        if any(word in confirm for word in ["yes", "confirm", "okay", "ok", "send"]):
            speak("Sending your email.")
            response_message = agent.send_email()
            speak(response_message)
            agent.reset()
            break
        elif any(word in confirm for word in ["no", "cancel", "don't"]):
            speak("Okay, the email has not been sent.")
            break
        elif "change" in confirm:
            if "recipient" in confirm or "email" in confirm:
                speak("Tell me the new recipient's email address.")
                while True:
                    raw_email = listen()
                    if not raw_email:
                        speak("Try again.")
                        continue
                    email = agent.parse_email(raw_email)
                    if email:
                        agent.recipient = email
                        break
                    speak("Invalid email.")
            if "subject" in confirm:
                speak("What is the new subject?")
                while True:
                    subject = listen()
                    if subject:
                        agent.subject = subject
                        break
                    speak("Please repeat the subject.")
            if "message" in confirm or "body" in confirm:
                speak("Tell me the new message.")
                while True:
                    message = listen()
                    if message:
                        agent.message = message
                        break
                    speak("Please say the message again.")
        else:
            speak("Didn't understand. Please say 'yes', 'no', or change something.")

    speak("Do you want to send another email?")
    response = listen()
    if response and any(word in response.lower() for word in ["yes", "okay", "send", "continue"]):
        speak("Say 'send email' to begin.")
    else:
        speak("Alright. Say 'send email' or 'play song' to do something else.")

# domain summary and scraping
def handle_domain_summary():
    domain = listen("Please say the domain you want to scan.", for_domain=True)
    scraped = scrape_homepage(domain)

    if isinstance(scraped, dict):
        speak("Scraping completed. Here's what I found.")
        summary = summarize_content_with_openai(scraped)
        speak("Here is the summary:")
        speak(summary)

        print("\n📄 Scraped Info:")
        print(f"🌐 URL: {scraped['url']}")
        print(f"📧 Email(s): {scraped['email']}")
        print(f"📞 Phone(s): {scraped['phone']}")
        print(f"👤 CEO Line(s): {scraped['ceo']}")

        speak("Here is the contact information.")

        decision = listen("Do you want to send an email to the CEO?")
        if decision and any(word in decision.lower() for word in ["yes", "sure", "okay", "go ahead"]):
            send_email_to_ceo(scraped.get('email', ''))
        else:
            speak("Okay, no email will be sent.")
    else:
        speak(scraped)

    speak("Website assistant task complete.")

# main function to run the assistant
def main():
    select_language()
    # speak("Hi, I am Laxmi. What can I do for you?")

    email_agent = EmailAgent()
    song_agent = SongAgent()

    speak("What you want to do? 'send email', 'play song', 'summarize website', or ask a question. Say 'exit' to quit.")

    while True:
        user_input = listen()
        if not user_input:
            speak("Didn't catch that. Please say again.")
            continue

        command = user_input.lower().strip()

        if "send email" in command:
            handle_email(email_agent)

        elif any(word in command for word in ["play", "song", "music"]):
            song_agent.handle_song_request()

        elif "summarize" in command or "domain" in command or "website" in command:
            handle_domain_summary()

        elif command in ["exit", "quit", "thank you", "thanks"]:
            speak("Do you want to perform another task?")
            response = listen()
            if response and response.lower() in ["no", "exit", "quit"]:
                speak("Goodbye!")
                break
            else:
                speak("Okay. Say 'send email', 'play song', or 'summarize website' to begin.")

        else:
            bot_reply = get_bot_response(command)
            speak(bot_reply or "Sorry, I couldn't think of a good answer.")


if __name__ == "__main__":
    main()