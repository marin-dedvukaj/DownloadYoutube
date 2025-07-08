import yt_dlp
class DownloadYoutube:
    def __init__(self, youtube_url, output_path='.'):
        self.youtube_url = youtube_url
        self.OutputPath = output_path

    def download_mp3(self, youtubeURL=None):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.OutputPath}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': r'\ffmpeg\bin',
            'quiet': False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtubeURL])

    def download_mp4(self, youtubeURL=None):
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{self.OutputPath}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'ffmpeg_location': r'\ffmpeg\bin',
            'quiet': False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtubeURL])