#..............................UI design of Polarity Analysis.....................................

#Importing necessary Libraries

import pandas as pd # for Dataframes manipulation
import numpy as np # for arrays manipulation
import seaborn as sns # foe data visualization
import plotly.express as px # for data visualization
from PIL import Image # to import images to User Interface (UI)
import requests # to assist importing images to User Interface (UI)
from io import BytesIO # to assist importing images to User Interface (UI)
from textblob import TextBlob #For natural language processing
import streamlit as st # for UI design

#Importing Images to user interface (UI)

url0 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Keyword%20Analysis.png"
url1 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/FB1.png"
url2 = "https://raw.githubusercontent.com/NishanD21/SNA/d4d282cba51f29e11e4cb91c61fe4431ef88f7fd/Images/YT1.png"
url3 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Insta.png"
url00 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Sidebar/SM%20Logos.png"

response0 = requests.get(url0)
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
response00 = requests.get(url00)

img0 = Image.open(BytesIO(response0.content))
img1 = Image.open(BytesIO(response1.content))
img2 = Image.open(BytesIO(response2.content))
img3 = Image.open(BytesIO(response3.content))
img00 = Image.open(BytesIO(response00.content))

st.image(img0)
st.image(img2)

st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)

st.sidebar.image(img00)
