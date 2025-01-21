from pytubefix import YouTube 
import os 

class downloader : 
    def __init__(self,url = 'http://youtube.com/watch?v=dQw4w9WgXcQ'):
        self.url = url
        yt = YouTube(url=self.url)
        self.title = yt.title
        self.stream = yt.streams.filter(only_audio=True).order_by("abr").last()

    def download(self,file_path) : 
        if os.path.isdir(file_path):
            file_path = os.path.join(file_path, self.stream.default_filename)
        
        # Download the file
        self.stream.download(output_path=os.path.dirname(file_path), filename=os.path.basename(file_path))

    