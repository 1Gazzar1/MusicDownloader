from yt_dlp import YoutubeDL
class downloader:
    def __init__(self, url):
        if len(url) > 0:
            self.url = url
        else:
            self.url = 'http://youtube.com/watch?v=dQw4w9WgXcQ'

        song_ydl_opts = {
            'format': 'bestaudio',
            'quiet': True,
            'no_warnings': True
        }
        with YoutubeDL(song_ydl_opts) as self.ydl:         
            info = self.ydl.extract_info(self.url,False)
            self.title = info.get('title')

    def download(self,file_path):
        file_path = file_path[:-4]
        song_ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': f'{file_path}.mp3',
            'quiet': True,
            'no_warnings': True
        }
        with YoutubeDL(song_ydl_opts) as self.ydl:         
            
            self.ydl.download(self.url)



        # Download thumbnail
        # thumbnail_ydl_opts = {
        #     'skip_download': True,  
        #     'writethumbnail': True,  
        #     'outtmpl': f'{file_path}',
        #     'quiet': True,
        #     'no_warnings': True
        # }
        # try: 
        #     with YoutubeDL(thumbnail_ydl_opts) as ydl: 
        #         ydl.download([self.url])
        #     print("Thumbnail downloaded successfully.")
        # except Exception as e:
        #     print(f"Failed to download thumbnail: {e}")

        # webp_path = f"{file_path}.webp"
        # jpg_path = f"{file_path}.jpg"

        # # Convert the img to jpg if it exists
        # if os.path.exists(webp_path):
        #     img = Image.open(webp_path)
        #     img.save(jpg_path, "JPEG")
        #     os.remove(webp_path)
        