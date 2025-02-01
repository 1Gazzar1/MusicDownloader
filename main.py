from Downloader import downloader
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from time import time
from os import path


def take_user_input(promt):
    while True : 
        inp = input(promt)

        if  inp.startswith('https://music.youtube.com') or inp.startswith('https://youtube.com') or inp == "" : 
            break
        else : 
            print("Invalid Input (url starts with 'https://youtube.com' )")
      
    return inp

if __name__=="__main__" : 
    while True :
        url = take_user_input("Enter the desired Song url (yt/ytmusic) : ")
        

        home = path.expanduser("~")
        downloads_folder = path.join(home, "Downloads")

        # intializing the downloader class 
        song = downloader(url)

        # Open a Save As dialog
        Tk().withdraw()
        save_path = asksaveasfilename(
            title="Save File As",
            defaultextension="", 
            filetypes=[("Audio","*.mp3 *.m4a")],
            initialfile=f"{song.title}" if len(url) > 0 else "easter egg",
            initialdir=f"{downloads_folder}"
        )

        # calculating the time it takes to download 
        start_time = time()

        # downloads the song 
        print("Starting Download")
        song.download(save_path)

        final_time = time()

        if save_path : 
            print(f"Download completed succesfully \nat {save_path}\nin {round((final_time-start_time),2)} s")

