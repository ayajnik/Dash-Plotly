import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

##first we plot the graph
data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
    marker = dict(      # change the marker style
        size = 12,
        color = 'rgb(51,204,153)',
        symbol = 'pentagon',
        line = dict(
            width = 2,
        )
    )
)]

##now we create the layout of the plot we just drew above
layout = go.Layout(
    title="My first plotly scatter plot",
    xaxis={"title":"x-axis"},
    yaxis={"title":"y-axis"},
    hovermode="closest"
)

##then we combine the plot and its layout

fig = go.Figure(data = data, layout=layout)
##plot it
pyo.plot(fig,filename="scatter_plot.html")