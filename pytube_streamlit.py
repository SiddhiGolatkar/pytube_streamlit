import streamlit as st
import pandas as pd
from pytube import YouTube 
import base64
from io import BytesIO

def main():
    path = st.text_input('Enter URL of youtube video')
    option = st.selectbox('select type of download', ('audio', 'video'))
    matches = ['audio', 'video'] 
    if st.button("download"): 
        video_object =  YouTube(path)
        st.write("Title of Video: " + str(video_object.title))
        st.write("Number of Views: " + str(video_object.views))
        if option=='audio':
            video_object.streams.get_audio_only().download() 	
            st.write("Audio downloaded")	
            #base64.b64encode("if file is too large").decode()	
        elif option=='video':
            video_object.streams.get_highest_resolution().download()
            st.write("Video downloaded")
    
    if st.button("view"): 
        st.video(path) 

if __name__ == '__main__':
    main()
