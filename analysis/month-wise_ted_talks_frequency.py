import plotly.express as px
import pandas as pd

df=pd.read_csv('..\\ted-talks-dataset/data.csv')

df['month'] = df['date'].apply(lambda x: x.split(' ')[0])
df['year'] =df['date'].apply(lambda x: x.split(' ')[1])

fig12 = px.bar(y=df.month.value_counts(),x=df.month.value_counts().index,orientation='v', width=800, height=600,
               color_discrete_sequence=['darkred'],template='simple_white')
fig12.update_layout(
    autosize=True,
    title ={'text': "<b style:'color:blue;'> Częstotliwość ted talks w poszczególnych miesiącach</b>", 'font': {'size': 30}},title_x=0.55,

    title_font_family="Times New Roman",
    title_font_color="black",
    # font_color='blue',

    xaxis_title={'text': "<b style:'color:blue;'>Miesiąc</b>", 'font': {'size':15}},
    yaxis_title={'text': "<b style:'color:blue;'>Liczba wystąpień</b>", 'font': {'size': 15}}, paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')

fig12.update_xaxes(categoryorder='array', categoryarray= [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
fig12.write_html('month-wise_ted_talks_frequency.html', auto_open=True)