import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1("Welcome to Dash"),
     html.Div(children='Dash: A web application framework for Python.'),

     dcc.Graph(
         id = "My first Graph",
         figure={
             "data":[
                 {'x':['1','2','3'], 'y':['4','5','6'],'type':'bar','name':'SF'},
                 {'y':['2','3','4'], 'y':['5','6','7'], 'type':'bar','name':"NYC"}
             ],
             "layout": {"title":"My first Dash plot"}
         }
     )
])

if __name__ =="__main__":
    app.run_server()