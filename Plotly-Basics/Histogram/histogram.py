import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\mpg.csv')

##histogram are used only for continous data
data = [
    go.Histogram(
        x = df['mpg'],
        xbins=dict(
            start = 10,
            end=50,
            size=2
        ),
        name="MPG"
    )
]

layout = go.Layout(
    title="My first Histogram"
)

fig=go.Figure(
    data=data,
    layout=layout
)

pyo.plot(fig,"histogram.html")