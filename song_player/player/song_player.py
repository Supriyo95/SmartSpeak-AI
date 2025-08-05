import subprocess
import os
import platform
import shutil

class SongPlayer:
    def __init__(self):
        self.system_platform = platform.system()
        self.player_process = None

        if self.system_platform == 'Windows':
            self.ffplay_path = r"C:\ffmpeg\bin\ffplay.exe"
            if not os.path.isfile(self.ffplay_path):
                raise FileNotFoundError(f"ffplay not found at {self.ffplay_path}. Please install FFmpeg and update the path.")
        elif self.system_platform == 'Linux':
            self.ffplay_path = shutil.which("ffplay")
            if self.ffplay_path is None:
                raise FileNotFoundError("ffplay not found. Please install FFmpeg using: sudo apt install ffmpeg")
        else:
            raise EnvironmentError(f"Unsupported OS: {self.system_platform}. Only Windows and Linux are supported.")

    def play(self, url):
        self.stop()  # Ensure no previous playback is running

        command = [
            self.ffplay_path,
            '-nodisp',        # No video display
            '-autoexit',      # Exit when done
            '-loglevel', 'quiet',  # Suppress console output
            url
        ]
        self.player_process = subprocess.Popen(command)

    def stop(self):
        if self.player_process and self.player_process.poll() is None:
            self.player_process.terminate()
            self.player_process = None

    def is_playing(self):
        return self.player_process is not None and self.player_process.poll() is None
