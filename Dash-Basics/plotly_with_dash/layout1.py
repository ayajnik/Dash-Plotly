import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo
import dash
from dash import dcc
from dash import html

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(
        "Welcome to Plotly with Dash",
        style={'textAlign': 'center',
            'color': '#7FDBFF'
        }),

    html.Div("My first Dashboard",
            style={'textAlign':'center',
            'color': '#7FDBFF'}
    ),

    dcc.Graph(
        id="Scatter plot",
        figure={
            'data':[
                go.Scatter(
                    x=random_x, y=random_y,mode = 'markers',
                    marker = {
                        'size': 12,
                        #'color': 'rgb(51,204,153)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                        }
                )
            ],
            'layout': go.Layout(
                title = 'Random Data Scatterplot',
                xaxis = {'title': 'Some random x-values'},
                yaxis = {'title': 'Some random y-values'},
                hovermode='closest'
            ),'paper_bgcolor': colors['background'],'plot_bgcolor': colors['background']
        }
    )

], style={'backgroundColor': colors['background']})

if __name__ == "__main__":
    app.run_server()