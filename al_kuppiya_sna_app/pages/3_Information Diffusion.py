#..............................UI design of Information Diffusion Page.....................................

# Importing necessary libraries

import streamlit as st # for User Interface design and visualization
import networkx as nx # for networkx graphs visualization
import matplotlib.pyplot as plt #for data manipulation and visualization of social media networks
import pandas as pd # for data frames manipulation
import plotly.express as px # for data visualization
from PIL import Image # to import images to User Interface (UI)
import requests # to assist importing images to User Interface (UI)
from io import BytesIO # to assist importing images to User Interface (UI)

import warnings
warnings.filterwarnings("ignore")



#.....................Polarity analysis of A/L Kuppiya Youtube channel comments...................

#Data extraction 

df_full = pd.read_json("https://raw.githubusercontent.com/NishanD21/SNA/main/Information%20Diffusion/YT_Comments.json")

df = df_full[['Commented by','Replied by']]

df = df.replace(to_replace="",
           value="A/L Kuppiya")

#................Importing Images for UI..................................

url0 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Information%20Diffusion.png"
url1 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Facebook-logo-PSD-1.jpg"
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

# Visualization of Networkx Graphs

G = nx.from_pandas_edgelist(df,source='Commented by',target="Replied by",create_using = nx.Graph())

fig_nx=nx.draw(G,with_labels=True,font_weight='normal',font_size=6)


pos = nx.spring_layout(G)
betCent = nx.betweenness_centrality(G, normalized=True, endpoints=True)
node_color = [20000.0 * G.degree(v) for v in G]
node_size = [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20,20))
fig_bet= nx.draw_networkx(G, pos=pos, with_labels=True,
node_color=node_color,
node_size=node_size )
x = sorted(betCent, key=betCent.get, reverse=True)[:8]


pos2 = nx.spring_layout(G)
betCent2 = nx.degree_centrality(G)
node_color2 = [20000.0 * G.degree(v) for v in G]
node_size2 = [v * 10000 for v in betCent2.values()]
plt.figure(figsize=(20,20))
fig_deg = nx.draw_networkx(G, pos=pos2, with_labels=True,
node_color=node_color2,
node_size=node_size2 )

y = sorted(betCent2, key=betCent2.get, reverse=True)[:8]
degree = pd.DataFrame({"Identified list of Influencers":y})


degree

st.pyplot(fig_nx, use_container_width=True)
st.pyplot(fig_bet, use_container_width=True)

st.set_option('deprecation.showPyplotGlobalUse', False)
