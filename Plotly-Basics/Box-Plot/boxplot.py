import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#df = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\mpg.csv')

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [
    go.Box(
        y=y,
        boxpoints='all',  ###show points along with box-plot
        jitter=0.8, ## values lie between 0 to 1
        pointpos=2 ## positioning datapoints on left or right, if left, then enter negative
    )
]

layout = go.Layout(
    title="Box Plot"
)

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,"boxplot.html")