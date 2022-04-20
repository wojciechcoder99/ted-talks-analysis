import plotly.express as px
import pandas as pd

df=pd.read_csv('..\\ted-talks-dataset/data.csv')

df['month'] = df['date'].apply(lambda x: x.split(' ')[0])
df['year'] =df['date'].apply(lambda x: x.split(' ')[1])

fig10 = px.bar(y=df.year.value_counts(),x=df.year.value_counts().index,orientation='v', width=800, height=600,
               color_discrete_sequence=['purple'],template='simple_white')
'''fig.update_xaxes(categoryorder='array', categoryarray= ['1970','1972','1983','1984','1990', '1991', '1994', '1998',
                                                        '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                                                        '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
                                                        '2017', '2018', '2019', '2020', '2021', '2022'])'''
fig10.update_layout(
    autosize=True,
    title ={'text': "<b style:'color:blue;'> Częstotliwość ted talks w poszczególnych latach</b>", 'font': {'size': 30}},title_x=0.55,

    title_font_family="Times New Roman",
    title_font_color="black",
    # font_color='blue',

    xaxis_title={'text': "<b style:'color:blue;'>Rok</b>", 'font': {'size':15}},
    yaxis_title={'text': "<b style:'color:blue;'>Liczba wystąpień</b>", 'font': {'size': 15}}, paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
fig10.update_traces(showlegend=False)
fig10.write_html('year-wise_ted_talks_frequency.html', auto_open=True)