import plotly.offline as pyo
import plotly.figure_factory as ff
import plotly.graph_objs as go
import numpy as np

x1 = np.random.randn(100)
x2 = np.random.randn(200)

##creating a list and storing the data into this list so that we can pass it into figure_factory module

hist_data = [x1,x2]
group_labels = ['First Sample','Second Sample']

data = ff.create_distplot(hist_data=hist_data,group_labels=group_labels,bin_size=[0.2,0.1])  ##you can also define the size of the bins for each sample by passing the parameter 'bins'. 
#This will be a list and each value of this list will correspond to the bin size of each sample

layout=go.Layout(title="My first distribution plot")

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,filename="distplot.html")