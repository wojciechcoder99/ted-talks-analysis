import plotly.express as px
import pandas as pd

df=pd.read_csv('..\\ted-talks-dataset/data.csv')

liked_speaker=df.groupby(['author']).sum()
views = liked_speaker.sort_values(by ='views',ascending=True).tail(10)

fig5 = px.bar(data_frame=views,y='views',x=views.index,orientation='v', width=700, height=600,
              color_discrete_sequence=['orange'],template='simple_white')
fig5.update_layout(
    autosize=True,
    title ={'text': "<b style:'color:blue;'>Top 10 najczęściej oglądanych mówców </b>", 'font': {'size': 30}},title_x=0.5,

    title_font_family="Times New Roman",
    title_font_color="black",
    # font_color='blue',

    xaxis_title={'text': "<b style:'color:blue;'>Wyświetlenia</b>", 'font': {'size':15}},
    yaxis_title={'text': "<b style:'color:blue';></b>", 'font': {'size': 15}}, paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
fig5.update_traces(showlegend=False)
fig5.write_html('most_viewed_speaker.html', auto_open=True)