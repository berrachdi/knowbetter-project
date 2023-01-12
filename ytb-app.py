import streamlit as st
import youtube_dl
import yt_dlp
import random
import string
import time
st.set_page_config(page_title="Youtube downloader", page_icon="🔻")







def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

#Not good uri exemples
#https://www.youtube.com/watch?v=1cQvGhUZWF8&ab_channel=CURSED
#https://youtu.be/1cQvGhUZWF8
def get_good_uri(uri):
    if uri.find('watch?v') != -1: return uri.split('&')[0]
    else: return 'https://www.youtube.com/watch?v='+uri.split("/")[3]






st.image("./videos/logo.png", width=300)
st.title("Download video from youtube ")
st.text('Get video url from youtube and add it into this input field 👇')
video_url = st.text_input(
        
        label="",
        label_visibility="hidden",
        key='text_key',
        disabled=False,
        placeholder="Enter video url..",
        
        
        
    )


if st.button('Get video download link'):

    # Get a url from the input field
    

    # Verify that is a valid url

    # Download video from the server using this url
    video_title_in_server = get_random_string(6)

    
    ydl_opts = {
        'outtmpl': './videos/'+video_title_in_server+'.%(ext)s'
    }
    

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(get_good_uri(video_url), download=False)
        video_title = info['title']
        thumbnail_url = info['thumbnail']
        durations = info['duration']
        width, height = 300, 200
        col1, col2 = st.columns(2)
        # Display the image
        with col1:
            
            st.image(thumbnail_url, width=width)
        with col2:
            st.write(video_title)
            st.write(str(durations/60) + ' min')
            
            st.markdown("""
            <style>
            .stProgress .st-bo {
                background-color: green;
            }
            </style>
            """, unsafe_allow_html=True)
            progress_bar = st.progress(0)
            progress_bar.progress(30)
            progress_bar.progress(70)

            ydl.download([get_good_uri(video_url)])
       
            progress_bar.progress(100)
            file_directory = "./videos/"+ video_title_in_server +".mp4"
            with open(file_directory, "rb") as file:
                btn = st.download_button(
                label="Download video to your device",
                data=file,
                file_name=video_title+'.mp4',
                mime="video/mp4"
            )
        
        
       

        
        
    
    



