import plotly.express as px
import pandas as pd

df=pd.read_csv('..\\ted-talks-dataset/data.csv')
most_viewed_ted_talk=df.sort_values('views',ascending=False).head(25)

fig1 = px.bar(data_frame=most_viewed_ted_talk,y='title',x='views',orientation='h', color='title', width=800, height=600,
              color_discrete_sequence=['red'],template='simple_white')
fig1.update_layout(
    autosize=True,
    title ={'text': "<b style:'color:black;'>25 najczęściej oglądanych ted talks </b>", 'font': {'size': 30}},title_x=0.6,

    title_font_family="Times New Roman",
    title_font_color="black",
    # font_color='blue',

    xaxis_title={'text': "<b style:'color:blue;'>Wyświetlenia</b>", 'font': {'size':15}},
    yaxis_title={'text': "<b style:'color:blue';></b>", 'font': {'size': 15}}, paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
fig1.update_traces(showlegend=False)
fig1.write_html('most_viewed_ted_talk.html', auto_open=True)