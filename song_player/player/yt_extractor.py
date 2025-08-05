import platform
import yt_dlp
from core.text_to_speech import speak

class YouTubeAudioExtractor:
    def __init__(self):
        self.system_platform = platform.system()

    def get_audio_stream_url(self, song_name):
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': True,
                'noplaylist': True,
                'default_search': 'ytsearch1',
                'extract_flat': False,
                'source_address': '0.0.0.0'  # helps avoid some network issues
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(song_name, download=False)

                if 'entries' in info and info['entries']:
                    return info['entries'][0].get('url', None)
                return info.get('url', None)

        except yt_dlp.utils.DownloadError:
            speak("There was a problem connecting to YouTube.")
        except Exception as e:
            speak("Failed to find or stream the song.")
            print(f"[YouTubeExtractor][{self.system_platform}] Error: {e}")
        return None
