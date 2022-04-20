import plotly.express as px
import pandas as pd

df=pd.read_csv('..\\ted-talks-dataset/data.csv')
most_liked_ted_talk=df.sort_values('likes',ascending=False).head(25)

fig2 = px.bar(data_frame=most_liked_ted_talk,y='title',x='likes',orientation='h', color='title', width=800, height=600,
              color_discrete_sequence=['black'],template='simple_white'
              #color_continuous_scale='darkmint'
              )
fig2.update_layout(
    autosize=True,
    title ={'text': "<b style:'color:blue;'>Top 25 najbardziej lubianych ted talks</b>", 'font': {'size': 30}},title_x=0.6,

    title_font_family="Times New Roman",
    title_font_color="black",
    # font_color='blue',

    xaxis_title={'text': "<b style:'color:blue;'>Polubienia</b>", 'font': {'size':15}},
    yaxis_title={'text': "<b style:'color:blue';></b>", 'font': {'size': 15}}, paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')

fig2.update_traces(showlegend=False)
fig2.write_html('most_liked_ted_talks.html', auto_open=True)