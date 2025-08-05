import platform
import shutil
from core.speech_to_text import listen
from core.text_to_speech import speak
from song_player.player.song_player import SongPlayer
from song_player.player.yt_extractor import YouTubeAudioExtractor

class SongAgent:
    def __init__(self):
        self.system_platform = platform.system()
        self.player = SongPlayer()
        self.extractor = YouTubeAudioExtractor()

    def handle_song_request(self):
        if not self._check_ffplay():
            return

        speak("Sure! What song do you want to hear?")
        song_name = listen()

        if song_name:
            speak(f"Searching and playing {song_name}")
            url = self.extractor.get_audio_stream_url(song_name)
            if url:
                self.player.play(url)
                self.voice_control()
            else:
                speak("Couldn't fetch the song.")
        else:
            speak("I didn't hear the song name. Please try again.")

    def voice_control(self):
        while self.player.is_playing():
            command = listen(show_listening=False)
            if command:
                command = command.lower()
                if "stop" in command or "exit" in command:
                    self.player.stop()
                    speak("Stopping the music.")
                    break
                elif "pause" in command or "resume" in command:
                    speak("Pause/resume not supported yet.")

    def _check_ffplay(self):
        """
        Ensure ffplay is available on the system.
        On Linux: checks system PATH
        On Windows: assumes path is set correctly inside SongPlayer
        """
        if self.system_platform == "Linux":
            if shutil.which("ffplay") is None:
                speak("FFmpeg is not installed. Please install it with: sudo apt install ffmpeg")
                return False
        elif self.system_platform == "Windows":
            # Assuming the ffplay path is configured correctly in SongPlayer
            return True
        else:
            speak(f"Your operating system ({self.system_platform}) is not supported for playback.")
            return False
        return True
