import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='my-input', value = 'Initial text', type='text'),

    html.Div(id='input-output')
])

@app.callback(Output(component_id='input-output',component_property='children'),[Input(component_id='my-input',component_property='value')])
def output_variable(input_variable):
    return "You entered {}".format(input_variable)

if __name__ == "__main__":
    app.run_server()