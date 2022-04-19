import plotly.express as px
import pandas as pd

df=pd.read_csv('..\\ted-talks-dataset/data.csv')

liked_speaker=df.groupby(['author']).sum()
likes=liked_speaker.sort_values(by ='likes',ascending=True).tail(10)

fig4 = px.bar(data_frame=likes,y=likes.index,x='likes',orientation='h', width=700, height=600,
              color_discrete_sequence=['green'],template='simple_white')
fig4.update_layout(
    autosize=True,
    title ={'text': "<b style:'color:blue;'>Top 10 najbardziej lubianych mówców </b>", 'font': {'size': 30}},title_x=0.5,

    title_font_family="Times New Roman",
    title_font_color="black",
    # font_color='blue',

    xaxis_title={'text': "<b style:'color:blue;'>Polubienia</b>", 'font': {'size':15}},
    yaxis_title={'text': "<b style:'color:blue';></b>", 'font': {'size': 15}}, paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')

fig4.update_traces(showlegend=False)
fig4.write_html('liked_speaker.html', auto_open=True)