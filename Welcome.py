import streamlit as st
from PIL import Image
from streamlit_card import card




st.set_page_config(
    page_title="KnowBetter - Home",
    layout="wide"
    
)


      


col1,col2,col3= st.columns([4,1,1])
with col1:
    

    #st.markdown(f"<div style='display:flex;justify-content:center;align-items:center;'><img src='{resource_path}' style='max-width:100%;height:auto;'></div>", unsafe_allow_html=True)
    # display the front end aspect
    st.image("./videos/logo.png", width=300)
    st.subheader("Greetings and welcome to our website! We hope you find what you're looking for, and we encourage you to get in touch if you have any questions or need further assistance")
    
    st.subheader("Amazing tools with source code ⚒️")
   
    

    
    #st.write("We are glad that you have stopped by to visit us. We hope that you will find our site informative, helpful, and enjoyable.")


cl1,cl2,cl3= st.columns([2,2,2])
with cl1:
   st.markdown(f'<a href="http://localhost:8501/Youtube-downloader" target="_top"><img src="https://www.linkpicture.com/q/Rose-Lumiere-noire-Vaporwave-E-sports-YouTube-Vignette-300-t-150-px_1.png" style="border-radius: 7%;box-shadow: 0 2px 20px rgba(0, 0, 0, 0.2);"></a>', unsafe_allow_html=True)
   st.markdown(f'<h5 style="width:300px;">Very fast tool to download a videos from youtube</h5>', unsafe_allow_html=True)
   st.markdown(f'<p style="width:300px;">Developed by: KnowBetter team</p>', unsafe_allow_html=True)
   st.markdown(f'<p style="width:300px; color:#008037;font-weight: bold;">Tool verified <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-patch-check-fill" viewBox="0 0 16 16"><path d="M10.067.87a2.89 2.89 0 0 0-4.134 0l-.622.638-.89-.011a2.89 2.89 0 0 0-2.924 2.924l.01.89-.636.622a2.89 2.89 0 0 0 0 4.134l.637.622-.011.89a2.89 2.89 0 0 0 2.924 2.924l.89-.01.622.636a2.89 2.89 0 0 0 4.134 0l.622-.637.89.011a2.89 2.89 0 0 0 2.924-2.924l-.01-.89.636-.622a2.89 2.89 0 0 0 0-4.134l-.637-.622.011-.89a2.89 2.89 0 0 0-2.924-2.924l-.89.01-.622-.636zm.287 5.984-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7 8.793l2.646-2.647a.5.5 0 0 1 .708.708z"/></svg>  </p>', unsafe_allow_html=True)
   button_html = """
      <style>
      .button {
      background-color: #008037;
      border: none;
      color: white;
      
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 12px;
      margin: 4px 2px;
      cursor: pointer;
      border-radius: 10px;
      }
      </style>
   
   <button class="button">python</button>
   
   """

   st.markdown(button_html, unsafe_allow_html=True)




col11,col22,col33= st.columns([2,2,2])
with col11:
    st.subheader("Best tutorial available for free 🔥")

   
cll1,cll2,cll3 = st.columns([2,2,2])
with cll1:
   st.markdown(f'<a href="http://localhost:8501/Youtube-downloader" target="_top"><img src="https://www.linkpicture.com/q/mPPhcU7oWDU-H3D.jpg" style="border-radius: 7%;box-shadow: 0 2px 20px rgba(0, 0, 0, 0.2);"></a>', unsafe_allow_html=True)
   
   st.markdown(f'<h5 style="width:300px;">Spring Boot Microservice Project Full Course</h5>', unsafe_allow_html=True)
   st.markdown(f'<p style="width:300px;">+6 hours | +45k views | 1.8k likes</p>', unsafe_allow_html=True)

   st.markdown(f'<p style="width:300px; color:#008037;font-weight: bold;">Content verified <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-patch-check-fill" viewBox="0 0 16 16"><path d="M10.067.87a2.89 2.89 0 0 0-4.134 0l-.622.638-.89-.011a2.89 2.89 0 0 0-2.924 2.924l.01.89-.636.622a2.89 2.89 0 0 0 0 4.134l.637.622-.011.89a2.89 2.89 0 0 0 2.924 2.924l.89-.01.622.636a2.89 2.89 0 0 0 4.134 0l.622-.637.89.011a2.89 2.89 0 0 0 2.924-2.924l-.01-.89.636-.622a2.89 2.89 0 0 0 0-4.134l-.637-.622.011-.89a2.89 2.89 0 0 0-2.924-2.924l-.89.01-.622-.636zm.287 5.984-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7 8.793l2.646-2.647a.5.5 0 0 1 .708.708z"/></svg>  </p>', unsafe_allow_html=True)
   button_html = """
      <style>
      .button {
      background-color: #008037;
      border: none;
      color: white;
      
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 12px;
      margin: 4px 2px;
      cursor: pointer;
      border-radius: 10px;
      }
      </style>
   <button class="button">java</button>
   <button class="button">spring boot</button>
   <button class="button">spring cloud</button>
   <button class="button">microservices</button>
   """

   st.markdown(button_html, unsafe_allow_html=True)
with cll2:
   st.markdown(f'<a href="http://localhost:8501/Youtube-downloader" target="_top"><img src="https://www.linkpicture.com/q/mPPhcU7oWDU-H3D.jpg" style="border-radius: 7%;box-shadow: 0 2px 20px rgba(0, 0, 0, 0.2);"></a>', unsafe_allow_html=True)
   
   st.markdown(f'<h5 style="width:300px;">Spring Boot Angular Full Stack Project - Youtube Clone</h5>', unsafe_allow_html=True)
   st.markdown(f'<p style="width:300px;">+8 hours | +45k views | 1.8k likes</p>', unsafe_allow_html=True)

   st.markdown(f'<p style="width:300px; color:#008037;font-weight: bold;">Content verified <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-patch-check-fill" viewBox="0 0 16 16"><path d="M10.067.87a2.89 2.89 0 0 0-4.134 0l-.622.638-.89-.011a2.89 2.89 0 0 0-2.924 2.924l.01.89-.636.622a2.89 2.89 0 0 0 0 4.134l.637.622-.011.89a2.89 2.89 0 0 0 2.924 2.924l.89-.01.622.636a2.89 2.89 0 0 0 4.134 0l.622-.637.89.011a2.89 2.89 0 0 0 2.924-2.924l-.01-.89.636-.622a2.89 2.89 0 0 0 0-4.134l-.637-.622.011-.89a2.89 2.89 0 0 0-2.924-2.924l-.89.01-.622-.636zm.287 5.984-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7 8.793l2.646-2.647a.5.5 0 0 1 .708.708z"/></svg>  </p>', unsafe_allow_html=True)
   button_html = """
      <style>
      .button {
      background-color: #008037;
      border: none;
      color: white;
      
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 12px;
      margin: 4px 2px;
      cursor: pointer;
      border-radius: 10px;
      }
      </style>
   <button class="button">java</button>
   <button class="button">spring boot</button>
   <button class="button">Angular</button>
   <button class="button">AWS</button>
   """

   st.markdown(button_html, unsafe_allow_html=True)

with cll3:
   st.markdown(f'<a href="http://localhost:8501/Youtube-downloader" target="_top"><img src="https://www.linkpicture.com/q/mPPhcU7oWDU-H3D.jpg" style="border-radius: 7%;box-shadow: 0 2px 20px rgba(0, 0, 0, 0.2);"></a>', unsafe_allow_html=True)
   
   st.markdown(f'<h5 style="width:300px;">Spring Boot Microservice Project Full Course</h5>', unsafe_allow_html=True)
   st.markdown(f'<p style="width:300px;">+6 hours | +45k views | 1.8k likes</p>', unsafe_allow_html=True)

   st.markdown(f'<p style="width:300px; color:#008037;font-weight: bold;">Content verified <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-patch-check-fill" viewBox="0 0 16 16"><path d="M10.067.87a2.89 2.89 0 0 0-4.134 0l-.622.638-.89-.011a2.89 2.89 0 0 0-2.924 2.924l.01.89-.636.622a2.89 2.89 0 0 0 0 4.134l.637.622-.011.89a2.89 2.89 0 0 0 2.924 2.924l.89-.01.622.636a2.89 2.89 0 0 0 4.134 0l.622-.637.89.011a2.89 2.89 0 0 0 2.924-2.924l-.01-.89.636-.622a2.89 2.89 0 0 0 0-4.134l-.637-.622.011-.89a2.89 2.89 0 0 0-2.924-2.924l-.89.01-.622-.636zm.287 5.984-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7 8.793l2.646-2.647a.5.5 0 0 1 .708.708z"/></svg>  </p>', unsafe_allow_html=True)
   button_html = """
      <style>
      .button {
      background-color: #008037;
      border: none;
      color: white;
      
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 12px;
      margin: 4px 2px;
      cursor: pointer;
      border-radius: 10px;
      }
      </style>
   <button class="button">java</button>
   <button class="button">spring boot</button>
   <button class="button">spring cloud</button>
   <button class="button">microservices</button>
   """

   st.markdown(button_html, unsafe_allow_html=True)
    

col111,col222,col333= st.columns([2,2,2])
with col111:
    st.button("+20 tutorials available..")

st.sidebar.markdown(
    """
    Copyright © 2023, knowbetter Inc.
    """
)

st.markdown("<footer>Copyright 2021</footer>", unsafe_allow_html=True)


        