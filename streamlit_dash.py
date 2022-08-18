#...............Import Libraries..................

import pandas as pd
import plotly.express as px
import streamlit as st
from googleapiclient.discovery import build # for data extraction
import seaborn as sns # for data visualization

st.set_page_config(page_title = "Social Network Analysis Dashboard",    
                    page_icon=':chart_with_upwards_trend:',
                    layout="wide")


def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

#.......Import A/L Kuppiya YouTube page data...........

api_key = 'AIzaSyBUWWG2nDyNjy_dsMaetj56tc5IPa1feVE'  #YouTube data extration is done using an API


channel_ids = ['UCaI8gOmwQZJpganFN4-SZlg', # A/L Kuppiya
               'UC0CXMeU0432EMgBnlBaY_yA', # DP Education
               'UCsYca35tV6JJLNWJdqHQiDw', # Guru.lk
              ] 


youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_stats(youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=','.join(channel_ids))
    response = request.execute() 
    
    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount'],
                    playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    
    return all_data

channel_statistics = get_channel_stats(youtube, channel_ids)

channel_data = pd.DataFrame(channel_statistics)



#..........Main page....................

st.title(":bar_chart: A/L Kuppiya SNA Dashboard ")
st.markdown("##")

st.dataframe(channel_data)

channel_data['Subscribers'] = pd.to_numeric(channel_data['Subscribers'])
channel_data['Views'] = pd.to_numeric(channel_data['Views'])
channel_data['Total_videos'] = pd.to_numeric(channel_data['Total_videos'])


sub_chart = channel_data.groupby(by=["Channel_name"]).sum()[["Subscribers"]]
fig_shares = px.bar(
    sub_chart,
    x=sub_chart.index,
    y="Subscribers",
    title="<b>Subscribers</b>",
    color_discrete_sequence=["#0083B8"] * len(sub_chart),
    template="plotly_white",
)

view_chart = channel_data.groupby(by=["Channel_name"]).sum()[["Views"]]
fig_views = px.bar(
    view_chart,
    x=view_chart.index,
    y="Views",
    title="<b>Views</b>",
    color_discrete_sequence=["#0083B8"] * len(view_chart),
    template="plotly_white",
)

left_column,right_column = st.columns(2)
left_column.plotly_chart(fig_shares, use_container_width=True)
right_column.plotly_chart(fig_views,use_container_width=True)

