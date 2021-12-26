import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import base64

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
    dcc.RangeSlider(       # this is the input
        id="Ranger",
        marks={i:str(i) for i in range(-10, 10)},
        min=-5,
        max=5,
        value=[-3, 4]
    ),
    html.Div(id='result')  # this is the output
], style={'width':'50%'})

# Create a Dash callback:
@app.callback(Output(component_id="result",component_property="children"),[Input(component_id="Ranger",component_property="value")])
def update_value(value_list):
    result = "Result: {}".format(value_list[0]+value_list[1])
    return result  

if __name__ == "__main__":
    app.run_server()