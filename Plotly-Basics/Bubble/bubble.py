import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\mpg.csv')

data = [
    go.Scatter(
        x=df['horsepower'],
        y=df['mpg'],
        text=df['name'],
        mode='markers',
        marker=dict(
            color=df['cylinders'],
            size=df['weight']/100,
            showscale=True
        )
    )
]

layout=go.Layout(
    title="MPG Analysis",
    xaxis=dict(title="x-axis"),
    yaxis=dict(title="y-axis")
)

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,"bubble.html")