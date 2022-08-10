import streamlit as st
import pandas as pd
from pytube import YouTube
import youtube_dl
import base64
from io import BytesIO

def main():
    path = st.text_input('Enter URL of youtube video')
    option = st.selectbox('select type of download', ('audio', 'video'))
    # matches = ['audio', 'video'] 
    if st.button("download", data=path): 
        video_object =  YouTube(path)
        st.write("Title of Video: " + str(video_object.title))
        st.write("Number of Views: " + str(video_object.views))
        if option=='audio':
            video_info = youtube_dl.YoutubeDL().extract_info(url = path, download=False)
            filename = f"{video_info['title']}.mp3"
            options={
                    'format':'bestaudio/best',
                    'keepvideo':False,
                    'outtmpl':filename,
                    }

            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])

            # video_object.streams.get_audio_only().download() 	
            st.write("Audio downloaded")	
            #base64.b64encode("if file is too large").decode()	
        elif option=='video':
            video_object.streams.get_highest_resolution().download()
            st.write("Video downloaded") 

    if st.button("view"): 
        st.video(path) 

if __name__ == '__main__':
    main()
