import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\abalone.csv')

first_sample = np.random.choice(df['rings'],10,replace=False)
second_sample = np.random.choice(df['rings'],10,replace=False)

trace0 = go.Box(
    y=first_sample,
    boxpoints='outliers',
    jitter = 1.0,
)

trace1 = go.Box(
    y=second_sample,
    boxpoints='outliers',
    jitter=1.0
)

data = [trace0,trace1]

layout = go.Layout(
    title="Rings Analysis from ABALONE"
)

fig=go.Figure(
    data=data,layout=layout
)

pyo.plot(fig,
    filename="Boxplot-exercise.html")
