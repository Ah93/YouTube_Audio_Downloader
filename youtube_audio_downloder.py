from pytube import YouTube
import os
from tkinter import *

root=Tk()
root.geometry('600x200')
root.title('Youtube Audio Downloder')
Label_1 = Label(root,text="Paste The Youtube Link Here", font=("bold",20))
Label_1.place(x=120,y=20)

mylink=StringVar()
pastelink=Entry(root, width=60, textvariable=mylink)
pastelink.place(x=140,y=80)
# youtube_video_url = 'https://www.youtube.com/watch?v=DkU9WFj8sYo'
# youtube_video_url = input("Please enter your URL here:")

def downloadAudio():
    youtube_audio_url=str(mylink.get())
    try:
        yt_obj = YouTube(youtube_audio_url)
    
        yt_obj.streams.get_audio_only().download(output_path='./MyYoutubeAudios')
        print(f'Video Title is {yt_obj.title}')
        print(f'Video Length is {yt_obj.length} seconds')
        print(f'Video Description is {yt_obj.description}')
        print(f'Video Rating is {yt_obj.rating}')
        print(f'Video Views Count is {yt_obj.views}')
        print(f'Video Author is {yt_obj.author}')

    

        print('YouTube audio downloaded successfully')
    except Exception as e:
        print(e)
Button(root,text="Download Audio", width=20, bg='green', fg='white', command=downloadAudio).place(x=220,y=110)

root.mainloop()