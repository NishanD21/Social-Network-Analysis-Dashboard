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

#....................Polarity Analysis of YouTube Comments..............................

url0 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/pOLARITY.png"
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


df_yt_com = pd.read_json('https://raw.githubusercontent.com/NishanD21/SNA/main/Information%20Diffusion/YT_Comments.json')

#Polarity Analysis using NLP

comments = df_yt_com["Comment"]
polarity =[]

for comment in comments:
    review_1 = TextBlob(comment)
    rev1 = review_1.sentiment.polarity
    polarity.append(rev1)

x= {"No":np.arange(len(comments)),"Comments": comments,"Polarity":polarity}

df_yt_pol = pd.DataFrame(x)

#KPIs
avg_polarity_yt = df_yt_pol['Polarity'].sum()/len(polarity)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Average Polarity:")
    st.subheader(avg_polarity_yt)
with middle_column:
    st.subheader("")
    st.subheader("")
with right_column:
    st.subheader("")
    st.subheader("")

yt_polarity_chart = df_yt_pol.groupby(by=["No"]).sum()[["Polarity"]]
fig_yt_pol= px.bar(
   yt_polarity_chart,
    x=df_yt_pol["No"],
    y="Polarity",
    title="<b>Polarity of YouTube Comments</b>",
    color_discrete_sequence=["#0083B8"] * len(yt_polarity_chart),
    template="plotly_dark",
)

st.plotly_chart(fig_yt_pol,use_container_width=True,)                  


#....................Polarity Analysis of Facebook Comments..............................

st.image(img1)

df_fb_com = pd.read_json('https://raw.githubusercontent.com/NishanD21/SNA/main/Information%20Diffusion/fb_comments.json')

#Polarity Analysis using NLP

comments_fb = df_fb_com["Comment"]
polarity_fb =[]

for comment_fb in comments_fb:
    review_fb1 = TextBlob(comment_fb)
    rev_fb1 = review_fb1.sentiment.polarity
    polarity_fb.append(rev_fb1)

y= {"No":np.arange(len(comments_fb)),"Comments": comments_fb,"Polarity":polarity_fb}

df_fb_pol = pd.DataFrame(y)

#KPIs
avg_polarity_fb = df_fb_pol['Polarity'].sum()/len(polarity_fb)

left_column1, middle_column2, right_column3 = st.columns(3)
with left_column1:
    st.subheader("Average Polarity:")
    st.subheader(avg_polarity_fb)
with middle_column2:
    st.subheader("")
    st.subheader("")
with right_column3:
    st.subheader("")
    st.subheader("")

fb_polarity_chart = df_fb_pol.groupby(by=["No"]).sum()[["Polarity"]]
fig_fb_pol= px.bar(
   fb_polarity_chart,
    x=df_fb_pol["No"],
    y="Polarity",
    title="<b>Polarity of Facebook Comments</b>",
    color_discrete_sequence=["#0083B8"] * len(yt_polarity_chart),
    template="plotly_dark",
)

st.plotly_chart(fig_fb_pol,use_container_width=True,)   
