import os
import subprocess
from yt_dlp import YoutubeDL

class downloader:
    def __init__(self, url):
        if len(url) > 0:
            self.url = url
        else:
            self.url = 'http://youtube.com/watch?v=dQw4w9WgXcQ'
        info = self.get_info()
        
        self.title = info.get('title')
        self.artist = info.get('artist')
        self.album = info.get('album')
        self.release_year = info.get('release_year')

    def get_info(self):
        song_ydl_opts = {
            'format': 'bestaudio',
            'quiet': True,
            'no_warnings': True
        }
        with YoutubeDL(song_ydl_opts) as ydl:         
            info = ydl.extract_info(self.url, False)
        return {
            'title': info.get('title'),
            'artist': info.get("artist") or info.get("uploader"),
            'album': info.get("album") or "Unknown Album",
            'release_year': info.get('release_year')
        }

    def download(self, file_path):
        file_path = file_path[:-4]
        song_ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': f'{file_path}.mp3',
            'quiet': True,
            'no_warnings': True
        }
        with YoutubeDL(song_ydl_opts) as ydl:         
            ydl.download(self.url)

        # Download thumbnail
        thumbnail_ydl_opts = {
            'skip_download': True,  
            'writethumbnail': True,  
            'outtmpl': f'{file_path}',
            'quiet': True,
            'no_warnings': True
        }
        try: 
            with YoutubeDL(thumbnail_ydl_opts) as ydl: 
                ydl.download([self.url])
            print("Thumbnail downloaded successfully.")
        except Exception as e:
            print(f"Failed to download thumbnail: {e}")

        # Convert the image
        webp_path = f"{file_path}.webp"
        jpg_path = f"{file_path}.jpg"

        if os.path.exists(webp_path):
            command = ['ffmpeg', "-loglevel", "quiet", '-i', webp_path, jpg_path]
            subprocess.run(command, check=True)
            os.remove(webp_path)

        # Embed the album cover and metadata
        if os.path.exists(jpg_path):
            output_file = f"{file_path}_tagged.mp3"
            command = [
                'ffmpeg',
                "-loglevel", "quiet",
                '-i', f"{file_path}.mp3",
                '-i', jpg_path,
                '-map_metadata', '0',
                '-map', '0',
                '-map', '1',
                '-id3v2_version', '3',
                '-metadata', f'title={self.title}',  
                '-metadata', f'artist={self.artist}',  
                '-metadata', f'album={self.album}',   
                '-metadata', f'release_year={self.release_year}',  
                output_file
            ]
            subprocess.run(command, check=True)

            # Replace original file with the tagged file
            os.replace(output_file, f"{file_path}.mp3")
            os.remove(jpg_path)
