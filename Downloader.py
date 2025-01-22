from yt_dlp import YoutubeDL

class downloader : 
    def __init__(self,url):
         # If no valid URL is provided, default to a fun Easter egg
        if len(url) > 0 : 
            self.url = url
        else :
            #RICKROLLED
            self.url = 'http://youtube.com/watch?v=dQw4w9WgXcQ'

    def download(self,file_path) : 
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': f'{file_path}',
            'quiet': True,
            'no_warnings': True
        }
        try : 
            with YoutubeDL(ydl_opts) as ydl : 
                ydl.download(self.url)
        except Exception as e:
            print(f"Failed to download: {e}")

            