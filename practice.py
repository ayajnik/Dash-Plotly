import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\gapminderDataFiveYear.csv')

year = []
for years in df['year'].unique():
    year.append({'label':str(years),'value':years})

app = dash.Dash()

app.layout = html.Div([
    html.H1("Life Expectancy for population across Globe",id="header",style={'textAlign':'center','color':'cyan'})
    ,html.P(html.Div(
        [dcc.Dropdown(id='year-selector',options=year,value=df['year'].min(),style=dict(color='indigo',border='solid',bordercolor='black'))]
        ))
    ])

#app.layout = html.P(dcc.Dropdown(id='year-selector',options=year,value=df['year'].min()))



if __name__ == "__main__":
    app.run_server()