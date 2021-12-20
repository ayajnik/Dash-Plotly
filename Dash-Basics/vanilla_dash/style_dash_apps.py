import dash
from dash import dcc
from dash import html

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1("Welcome to Dash",
    style={'textAlign':'center','color':'#7FDBFF'}),

     html.Div(
        children='Dash: A web application framework for Python.',
        style={
            'textAlign': 'center',
            'color': '#7FDBFF'
        }
    ),
    dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    },
                    'title': 'Dash Data Visualization'
                }
            }
    )
    ],
     style={'backgroundColor': colors['background']}
     )


if __name__=="__main__":
    app.run_server()