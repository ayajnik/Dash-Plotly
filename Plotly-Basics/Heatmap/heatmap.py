import plotly.offline as pyo
import plotly.figure_factory as ff
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from plotly import tools

#df = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\2010SantaBarbaraCA.csv')

##SCENARIO 1: Simple heatmap

##In heatmaps, we define x axis, y axis and z axis. The z axis will always be passed as a list since it does not take pandas column
## we can define different colors as well. Inside our Heatmap function, we define a parameter called colorscale. The most widely used is 'Jet'
# data = [
#     go.Heatmap(
#         x=df['DAY'],
#         y=df['LST_DATE'],
#         z=df['T_HR_AVG'].values.tolist(),
#         colorscale='Jet'
#     )
# ]

# layout = go.Layout(
#     title="Santa Barabara,CA temperature distribution"
# )

# fig = go.Figure(data=data,layout=layout)

# pyo.plot(fig, filename="heatmap1.html")

##SCENARIO 2: Including multiple heatmaps by making subplots

## for subplots we need to import a module from plotly called tools

df1 = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\2010SantaBarbaraCA.csv')
df2 = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\2010SitkaAK.csv')
df3 = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\2010YumaAZ.csv')

trace0=go.Heatmap(
        x=df1['DAY'],
        y=df1['LST_DATE'],
        z=df1['T_HR_AVG'].values.tolist(),
        colorscale='Jet')
trace1=go.Heatmap(
        x=df2['DAY'],
        y=df2['LST_DATE'],
        z=df2['T_HR_AVG'].values.tolist(),
        colorscale='Jet')
trace2=go.Heatmap(
        x=df3['DAY'],
        y=df3['LST_DATE'],
        z=df3['T_HR_AVG'].values.tolist(),
        colorscale='Jet')

## now we use subplots with tools module

fig = tools.make_subplots(rows=1,cols=3,subplot_titles=['Sanata Barabara','Sitka','Yuma'],shared_yaxes=True)

fig.append_trace(trace0,1,1)
fig.append_trace(trace0,1,2)
fig.append_trace(trace0,1,3)
layout = go.Layout(title="Tempearture comparisons of three cities")
##we can append layout in fig with simple update module
fig['layout'].update(layout)
pyo.plot(fig,filename="heatmap2.html")
