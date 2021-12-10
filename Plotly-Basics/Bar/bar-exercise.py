import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#reading the dataframe
df = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\mocksurvey.csv',index_col=0)

data = [
    go.Bar(
        x=df.index,
        y=df[responses],
        name=responses
    )
    for responses in df.columns
]

layout = go.Layout(
    title="Bar chart plot",
    xaxis=dict(title="x-axis"),
    yaxis=dict(title="y-axis"),
    barmode='stack'
)

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,filename="barchart.html")