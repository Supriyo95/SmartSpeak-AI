# 🧠 SmartSpeak AI

**SmartSpeak AI** is a **multi-functional voice assistant** powered by voice recognition and AI, enabling you to:

1. 🎤 Listen to spoken user input  
2. 📧 Compose and send emails via Gmail  
3. 🎵 Search and stream songs from YouTube  
4. 🌐 Scrape websites, summarize content, and contact CEOs  
5. 🤖 Ask any type of questions — powered by GPT-4 (Gemini or OpenAI)

---

## 🚀 Features

| Module        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| ✉️ Email Bot   | Voice-controlled email sender (Gmail SMTP with confirmation & editing)     |
| 🎶 Music Player | Plays songs using YouTube streaming and ffmpeg-based playback              |
| 🌐 Web Scanner | Listens for a domain, scrapes homepage info, summarizes it and send email to CEO via Gemini   |
| 💬 AI Chatbot  | Voice Q&A using LLMs like OpenAI or Gemini                                 |

---

## 🗂️ Project Structure

```
SmartSpeakAI/
├── core/
│   ├── speech_to_text.py      ✅ Unified listen()
│   ├── text_to_speech.py      ✅ Unified speak()
│   ├── speech_to_text.py      ✅ speech convert into text
│   ├── config.py              ✅ Combined SMTP + Gemini/OpenAI
│   ├── scraper.py             🌐 Homepage content scraping
│   └── summarizer.py          🧠 GPT-based summarization
├── email_send/
│       ├── language_selector.py
│       ├── validators.py
│   └── utils/
│       ├── agent.py
│       ├── email_sender.py
│       └── secret.py
├── emailer/
│   └── sender.py              📧 send_email_to_ceo()
├── song_player/
│   ├── agents/
│   │   └── song_agent.py      🎵 YouTube-based music player
│   │   └── agent.py      
│   └── player/
│       ├── song_player.py
│       └── yt_extractor.py
├── llm/
│   └── chatbot.py             💬 GPT-based general chatbot
├── main.py                    🧩 Unified entry point
└── requirements.txt
```

---

## 🧪 Installation Setup

### 1. Clone the repository

```bash
git clone https://github.com/Supriyo95/SmartSpeak-AI.git
cd SmartSpeak-AI
```

### 2. 🎙️ Setup FFMPEG

- Download from: https://ffmpeg.org/download.html  
- Set path to `ffplay.exe` in `song_agent.py`:
```python
self.FFPLAY_PATH = r"C:\ffmpeg\bin\ffplay.exe"
```

### 3. Create a virtual environment

```bash
python -m venv venv
# Activate (Windows):
.\venv\Scripts\activate
# Activate (macOS/Linux):
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the assistant

```bash
python main.py
```

#### Then say one of the following:

- 📨 `Send email` → Start the voice email assistant  
- 🎵 `Play a song` → Stream a YouTube song  
- 💬 `Ask question` → Interact with GPT-4 chatbot  
- 🌐 `Summarize Website` → Scrape and summarize website  
- ❌ `Exit` → Quit the assistant  

---

## 📦 Dependencies

- `speechrecognition`, `gtts`, `pygame`  
- `googletrans`, `yt_dlp`, `requests`, `beautifulsoup4`  
- `openai`, `google-generativeai`  
- `ffmpeg` (external system dependency)

---

## 👨‍💻 Created by

**Supriyo Dolui**  
[![Gmail - supriyo](https://img.shields.io/badge/Gmail-supriyo-red?style=for-the-badge&logo=gmail&logoColor=white&labelColor=EA4335)][reach_gmail]

Feel free to use, extend, and contribute to this voice-powered AI productivity assistant.

---

## 📜 License

MIT License – Use freely with attribution.

<!-- CONTACT LINKS -->
[reach_gmail]: mailto:supriyo2001dolui@gmail.com?subject=GitHub