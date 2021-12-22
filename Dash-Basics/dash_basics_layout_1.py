import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo
import dash
from dash import dcc
from dash import html
import pandas as pd

df = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\OldFaithful.csv')

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(
        
        "Analyzing the next eruption",
        style={
            'textAlign':'center',
            'color': '#7FDBFF'    
        }
    ),

    dcc.Graph(
        id="Scatter plot",
        figure={
            'data':[
                go.Scatter(
                    x=df['X'],y=df['Y'],mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                        }
                )
            ],
            'layout':go.Layout(
                xaxis=dict(title='x-axis'),
                yaxis=dict(title='y-axis')
            )})])


if __name__ == "__main__":
    app.run_server()
