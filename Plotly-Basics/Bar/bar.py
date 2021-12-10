import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\2018WinterOlympics.csv')

##simple bar chart

# data = [
#     go.Bar(
#         x=df['NOC'],
#         y=df['Total']
        
#     )
# ]

# layout = go.Layout(
#     title="Winter olympics tally",
#     xaxis={"title":"x-axis"},
#     yaxis={"title":"y-axis"}
# )

# fig = go.Figure(data=data,layout=layout)

# pyo.plot(fig,filename="bar.html")

trace0 = go.Bar(
    x = df['NOC'],
    y=df['Gold'],
    marker=dict(
        color="#FFD700"
    ),
    name="Gold"
)

trace1 = go.Bar(
    x=df['NOC'],
    y=df['Silver'],
    marker=dict(
        color="#9EA0A1"
    ),
    name="Silver"
)

trace2 = go.Bar(
    x=df['NOC'],
    y=df['Bronze'],
    marker=dict(
        color="#CD7F32"
    ),
    name="Bronze"
)

data = [trace0,trace1,trace2]

##if we want to create a stacked bar plot, then in layout we add a component called "barmode" and give it's value stacked
layout = go.Layout(
    title="Winter Olympics tally of 2018",
    xaxis={"title":"Country"},
    yaxis={"title":"Medal Tally"}
    #barmode="stack"
)

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,"bar.html")
