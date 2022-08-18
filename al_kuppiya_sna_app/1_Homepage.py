#...............Import Libraries..................

import pandas as pd # for dataframe manipulation
import plotly.express as px # for data visualization
import streamlit as st # for User Interface (UI) design
from googleapiclient.discovery import build # for data extraction
import seaborn as sns # for data visualization
from PIL import Image # to import images to User Interface (UI)
import requests # to assist importing images to User Interface (UI)
from io import BytesIO # to assist importing images to User Interface (UI)

st.set_page_config(
    page_title="A/L Kuppiya SNA",
    page_icon="💻",
    layout="wide"
)

#Importing Images to user interface (UI)

url0 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Dashboard%20Cover.png"
url00 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Sidebar/SM%20Logos.png"

response0 = requests.get(url0)
response00 = requests.get(url00)

img0 = Image.open(BytesIO(response0.content))
img00 = Image.open(BytesIO(response00.content))

st.image(img0)

st.sidebar.success("SELECT A PAGE ABOVE")
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)

st.sidebar.image(img00)

st.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
url = "https://raw.githubusercontent.com/NishanD21/SNA/9a094aa31f177e729d6ac3d6a7855c28c3ec46a7/Images/AL_kuppiya_logo.png"

response = requests.get(url)

img = Image.open(BytesIO(response.content))

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(img)

with col3:
    st.write(' ')


url1 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Facebook-logo-PSD-1.jpg"
url2 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/502px-Logo_of_YouTube_2015-2017.svg_.png"
url3 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Instagram-Icon.png"
url4 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/502px-Logo_of_YouTube_2015-2017.svg_%20-%20Copy.png"

response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
response4 = requests.get(url4)

img1 = Image.open(BytesIO(response1.content))
img2 = Image.open(BytesIO(response2.content))
img3 = Image.open(BytesIO(response3.content))
img4 = Image.open(BytesIO(response4.content))


st.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'> ⬅️ USE THE SIDE BAR MENU TO VIEW THE ANALYTICS </h3>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Note: Social Media Analytics Dashboard for A/L Kuppiya Mobile Application is designed as a part of the assignment of Social Media Analytics for Business module of MSc Data Science program. Data used to present in this dashboard are only used for educational purposes and any of the data used here will not be used for any other purposes.   </h6>", unsafe_allow_html=True)

#col4, col5, col6 = st.columns(3)

#with col4:
    #st.image(img1,caption='Facebook')

#with col5:
    #st.image(img2,caption='YouTube')

#with col6:
    #st.image(img3,caption='Instagram')