import pytubefix
from Downloader import downloader
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from time import time


def take_user_input(promt):
    while True : 
        inp = input(promt)

        if  inp.startswith('https://music.youtube.com') or inp.startswith('https://youtube.com') : 
            break
        else : 
            print("Invalid Input (url starts with 'https://youtube.com' )")
      
    return inp.replace("music.","")

url = take_user_input("Enter the desired Song url (yt/ytmusic) : ")

# Open a Save As dialog
Tk().withdraw()
save_path = asksaveasfilename(
    title="Save File As",
    defaultextension=".mp3", 
    filetypes=[("Audio","*.mp3 *.m4a")]
)


try : 
    # intializing the downloader class 
    song = downloader(url)

    # calculating the time it takes to download 
    start_time = time()
    print(f"Downloading {song.title}")

    # downloads the song 
    song.download(save_path)

    final_time = time()

    print(f"Download completed succesfully \nat {save_path}\nin {final_time-start_time}")
except pytubefix.exceptions.BotDetection as e:
    print(f"youtube thinks you're a bot ): , try again later .")
except Exception as e : 
    print(f"something went wrong {e}")
