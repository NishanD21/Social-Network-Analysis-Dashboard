#..............................UI design of User Engagement Page.....................................

import streamlit as st # for data visualization in the web application
import pandas as pd # for dataframe manipulation
import plotly.express as px # for data visualization
from googleapiclient.discovery import build # for data extraction via API
import seaborn as sns # for data visualization
from PIL import Image # to import images to User Interface (UI)
import requests # to assist importing images to User Interface (UI)
from io import BytesIO # to assist importing images to User Interface (UI)

#Importing Images to user interface (UI)

url0 = "https://raw.githubusercontent.com/NishanD21/SNA/main/Images/Minimal%20Modern%20Elegant%20Background%20Technology%20Facebook%20Cover.png"
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

#.......Extraction of A/L Kuppiya YouTube channel user engagement data..................

api_key = 'AIzaSyBUWWG2nDyNjy_dsMaetj56tc5IPa1feVE'  # API key for YouTube data extraction


channel_ids = ['UCaI8gOmwQZJpganFN4-SZlg', # A/L Kuppiya YT channel
               'UC0CXMeU0432EMgBnlBaY_yA', # DP Education YT channel
               'UCsYca35tV6JJLNWJdqHQiDw', # Guru.lk YT channel
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


channel_data['Subscribers'] = pd.to_numeric(channel_data['Subscribers'])
channel_data['Views'] = pd.to_numeric(channel_data['Views'])
channel_data['Total_videos'] = pd.to_numeric(channel_data['Total_videos'])

playlist_id = channel_data.loc[channel_data['Channel_name']=='AL Kuppiya', 'playlist_id'].iloc[0]

def get_video_ids(youtube, playlist_id):
    
    request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId = playlist_id,
                maxResults = 50)
    response = request.execute()
    
    video_ids = []
    
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken')
    more_pages = True
    
    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                        part='contentDetails',
                        playlistId = playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token)
            response = request.execute()
    
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
            next_page_token = response.get('nextPageToken')
        
    return video_ids

video_ids = get_video_ids(youtube, playlist_id)

def get_video_details(youtube, video_ids):
    all_video_stats = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
                    part='snippet,statistics',
                    id=','.join(video_ids[i:i+50]))
        response = request.execute()
        
        for video in response['items']:
            video_stats = dict(Title = video['snippet']['title'],
                               Published_date = video['snippet']['publishedAt'],
                               Views = video['statistics']['viewCount'],
                               Likes = video['statistics']['likeCount'],
                               #Dislikes = video['statistics']['dislikeCount'],
                               Comments = video['statistics']['commentCount']
                               )
            all_video_stats.append(video_stats)
    
    return all_video_stats

video_details = get_video_details(youtube, video_ids)

video_data = pd.DataFrame(video_details)

video_data['Published_date'] = pd.to_datetime(video_data['Published_date']).dt.date
video_data['Views'] = pd.to_numeric(video_data['Views'])
video_data['Likes'] = pd.to_numeric(video_data['Likes'])
video_data['Views'] = pd.to_numeric(video_data['Views'])

video_data['Comments'] = video_data['Comments'].astype('int')

top10_videos = video_data.sort_values(by='Views', ascending=False).head(10)

video_data['Month'] = pd.to_datetime(video_data['Published_date']).dt.strftime('%b')

videos_per_month = video_data.groupby('Month', as_index=False).size()

sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

videos_per_month.index = pd.CategoricalIndex(videos_per_month['Month'], categories=sort_order, ordered=True)

videos_per_month = videos_per_month.sort_index()
videos_per_month['Months'] = ['January','February','March','April','May','June','July','August','September','October','November','December']

# KPIs visualization

subscibers = channel_data['Subscribers'][0]
total_likes = video_data['Likes'].sum()
total_comments = video_data['Comments'].sum()

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Subscribers:")
    st.subheader(subscibers)
with middle_column:
    st.subheader("Total Likes:")
    st.subheader(total_likes)
with right_column:
    st.subheader("Total Comments:")
    st.subheader(total_comments)


#........................YouTube Data Visualization...................................

# chart of posted videos in each month 
vids_per_month_chart = videos_per_month.groupby(by=["Months"]).sum()[["size"]]
fig_vids_month= px.line(
    vids_per_month_chart,
    x= videos_per_month.index,
    y= "size",
    title="<b>Number of Posted Videos in each month</b>",
    color_discrete_sequence=["#0073B8"] * len(vids_per_month_chart),
    template="plotly_dark",
    text="size",
    markers=True
)

# A/L Kuppiya top10 videos chart
top10_vids_chart = top10_videos.groupby(by=["Title"]).sum()[["Views"]]
fig_top10_vids= px.bar(
    top10_vids_chart,
    x= "Views",
    y= top10_videos['Title'],
    title="<b>Top Ten Videos with most number of Views</b>",
    color_discrete_sequence=["#0073B8"] * len(top10_vids_chart),
    template="plotly_dark",
)

# Competitor analysis charts
sub_chart = channel_data.groupby(by=["Channel_name"]).sum()[["Subscribers"]]
fig_subs= px.bar(
    sub_chart,
    x=sub_chart.index,
    y="Subscribers",
    title="<b>Subscribers</b>",
    color_discrete_sequence=["#0083B8"] * len(sub_chart),
    template="plotly_dark",
)

view_chart = channel_data.groupby(by=["Channel_name"]).sum()[["Views"]]
fig_views = px.bar(
    view_chart,
    x=view_chart.index,
    y="Views",
    title="<b>Views</b>",
    color_discrete_sequence=["#0083B8"] * len(view_chart),
    template="plotly_dark",
)

vid_chart = channel_data.groupby(by=["Channel_name"]).sum()[["Total_videos"]]
fig_vids = px.bar(
    vid_chart,
    x=vid_chart.index,
    y="Total_videos",
    title="<b>Total Videos</b>",
    color_discrete_sequence=["#0083B8"] * len(vid_chart),
    template="plotly_dark",
)


st.plotly_chart(fig_top10_vids,use_container_width=True)
st.plotly_chart(fig_vids_month,use_container_width=True)

st.markdown('Competitor Analysis')

st.dataframe(channel_data[['Channel_name','Subscribers','Views','Total_videos']])

left_column,middle_column,right_column = st.columns(3)
left_column.plotly_chart(fig_subs, use_container_width=True)
middle_column.plotly_chart(fig_vids, use_container_width=True)
right_column.plotly_chart(fig_views,use_container_width=True)

#..................A/L Kuppiya Facebook Page Data Analysis and Data Visualization.................

st.image(img1)

#KPIs visualization

followers = "26,507"

st.subheader(f"Facebook Page Followers: {followers}") 

st.subheader("") 


df_fb_ue_summary = pd.read_json('https://raw.githubusercontent.com/NishanD21/SNA/main/User%20Engagement/fb_ue/comp_fb_ue_summary.json')
df_fb_al_ue = pd.read_json('https://raw.githubusercontent.com/NishanD21/SNA/main/User%20Engagement/fb_ue/al_fb_ue_data.json')
df_fb_dp_ue = pd.read_json('https://raw.githubusercontent.com/NishanD21/SNA/main/User%20Engagement/fb_ue/dp_fb_ue_data.json')
df_fb_gr_ue = pd.read_json('https://raw.githubusercontent.com/NishanD21/SNA/main/User%20Engagement/fb_ue/gr_fb_ue_data.json')

#......................A/L Kuppiya Facebook User Engagement........................

fb_al_likes_chart = df_fb_al_ue.groupby(by=["post_id"]).sum()[["likes"]]
fig_fb_al_likes= px.bar(
    fb_al_likes_chart,
    x=df_fb_al_ue.index,
    y="likes",
    title="<b>Likes recieved for each post</b>",
    color_discrete_sequence=["#0083B8"] * len(fb_al_likes_chart),
    template="plotly_dark",
)

fb_al_shares_chart = df_fb_al_ue.groupby(by=["post_id"]).sum()[["shares"]]
fig_fb_al_shares= px.bar(
    fb_al_shares_chart,
    x=df_fb_al_ue.index,
    y="shares",
    title="<b>Shares recieved for each post</b>",
    color_discrete_sequence=["#0083B8"] * len(fb_al_shares_chart ),
    template="plotly_dark",
)

fb_al_comments_chart = df_fb_al_ue.groupby(by=["post_id"]).sum()[["comments"]]
fig_fb_al_comments= px.bar(
    fb_al_comments_chart,
    x=df_fb_al_ue.index,
    y="comments",
    title="<b>Comments recieved for each post</b>",
    color_discrete_sequence=["#0083B8"] * len(fb_al_comments_chart ),
    template="plotly_dark",
)


st.markdown('For user engagement analysis, only last 18 posts which posted on each page were considered')

col12,col13,col14= st.columns(3)

col12.plotly_chart(fig_fb_al_likes,use_container_width=True)
col13.plotly_chart(fig_fb_al_shares,use_container_width=True)
col14.plotly_chart(fig_fb_al_comments,use_container_width=True)



#...............................Facebook Competitor Analysis..................................

st.markdown("<h5 style='text-align: left;'>Competitor Analysis</h5>", unsafe_allow_html=True)

fb_summary_ue_lchart = df_fb_ue_summary.groupby(by=["Product"]).sum()[["Likes"]]
fig_fb_lsummary= px.bar(
    fb_summary_ue_lchart,
    x=fb_summary_ue_lchart.index,
    y="Likes",
    title="<b>Likes</b>",
    color_discrete_sequence=["#0083B8"] * len(fb_summary_ue_lchart),
    template="plotly_dark",
)

fb_summary_ue_schart = df_fb_ue_summary.groupby(by=["Product"]).sum()[["Shares"]]
fig_fb_ssummary= px.bar(
    fb_summary_ue_schart,
    x=fb_summary_ue_schart.index,
    y="Shares",
    title="<b>Shares</b>",
    color_discrete_sequence=["#0083B8"] * len(fb_summary_ue_schart),
    template="plotly_dark",
)

fb_summary_ue_cchart = df_fb_ue_summary.groupby(by=["Product"]).sum()[["Comments"]]
fig_fb_csummary= px.bar(
    fb_summary_ue_cchart,
    x=fb_summary_ue_cchart.index,
    y="Comments",
    title="<b>Comments</b>",
    color_discrete_sequence=["#0083B8"] * len(fb_summary_ue_cchart ),
    template="plotly_dark",
)

st.markdown('For competitor analysis, only last 18 posts which posted on each page were considered')

col9,col10,col11= st.columns(3)

col9.plotly_chart(fig_fb_lsummary,use_container_width=True)
col10.plotly_chart(fig_fb_ssummary,use_container_width=True)
col11.plotly_chart(fig_fb_csummary,use_container_width=True)

#......................A/L Kuppiya Instagram User Engagement...................

#..........Importing images for UI...............................

st.image(img3)

df_insta_ue_summary = pd.read_json('https://raw.githubusercontent.com/NishanD21/SNA/main/User%20Engagement/insta_ue/com_insta_ue_summary.json')
df_insta_al_ue = pd.read_json('https://raw.githubusercontent.com/NishanD21/SNA/main/User%20Engagement/insta_ue/al_insta_ue_data.json')

# KPIs Visualization

followers = df_insta_ue_summary['Followers'][0]
total_likes_insta = df_insta_ue_summary['Total Likes'][0]
total_comments_insta = df_insta_ue_summary['Total Comments'][0]

left_column_insta, middle_column_insta, right_column_insta = st.columns(3)
with left_column_insta:
    st.subheader("Followers:")
    st.subheader(followers)
with middle_column_insta:
    st.subheader("Total Likes:")
    st.subheader(total_likes_insta)
with right_column_insta:
    st.subheader("Total Comments:")
    st.subheader(total_comments_insta)

#............. A/L Kuppiya Instagram User engagement and Data Visualization..................

insta_like_ue_chart = df_insta_al_ue.groupby(by=["Post"]).sum()[["Likes"]]
fig_insta_likes= px.bar(
    insta_like_ue_chart,
    x=df_insta_al_ue["Post"],
    y="Likes",
    title="<b>Number of Likes received for last 20 posts</b>",
    color_discrete_sequence=["#0083B8"] * len(insta_like_ue_chart ),
    template="plotly_dark",
)

insta_fol_sum_chart = df_insta_ue_summary.groupby(by=["Product"]).sum()[["Followers"]]
fig_insta_fol= px.bar(
    insta_fol_sum_chart,
    x=df_insta_ue_summary["Product"],
    y="Followers",
    title="<b>Instagram Followers</b>",
    color_discrete_sequence=["#0083B8"] * len(insta_fol_sum_chart),
    template="plotly_dark",
)

insta_like_sum_chart = df_insta_ue_summary.groupby(by=["Product"]).sum()[["Total Likes"]]
fig_insta_sum_likes= px.bar(
    insta_like_sum_chart,
    x=df_insta_ue_summary["Product"],
    y="Total Likes",
    title="<b>Total Likes for Instagram Posts</b>",
    color_discrete_sequence=["#0083B8"] * len(insta_like_sum_chart),
    template="plotly_dark",
)

insta_comments_sum_chart = df_insta_ue_summary.groupby(by=["Product"]).sum()[["Total Comments"]]
fig_insta_sum_comments= px.bar(
    insta_comments_sum_chart,
    x=df_insta_ue_summary["Product"],
    y="Total Comments",
    title="<b>Total Comments for Instagram Posts</b>",
    color_discrete_sequence=["#0083B8"] * len(insta_comments_sum_chart),
    template="plotly_dark",
)

st.plotly_chart(fig_insta_likes,use_container_width=True,)

st.markdown("<h5 style='text-align: left;'>Competitor Analysis</h5>", unsafe_allow_html=True)

col16,col17,col18= st.columns(3)

col16.plotly_chart(fig_insta_fol,use_container_width=True)
col17.plotly_chart(fig_insta_sum_likes,use_container_width=True)
col18.plotly_chart(fig_insta_sum_comments,use_container_width=True)