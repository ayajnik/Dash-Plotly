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
    html.H1("Life Expectancy for population across Globe",id="header",style={'textAlign':'center','color':'cyan'}),

    html.P(dcc.Dropdown(id='year-selector',options=year,value=df['year'].min())),

    dcc.Graph(id='scatter-plot')
],style={'backgroundColor':'black'})

@app.callback(Output(component_id='scatter-plot',component_property='figure'),[Input(component_id='year-selector',component_property='value')])
def update_figure(selected_year):

    filtered_df = df[df['year'] == selected_year]

    trace = []

    for continent_name in filtered_df['continent'].unique():
        new_filtered_df = filtered_df[filtered_df['continent'] == continent_name]

        trace.append(go.Scatter(x=new_filtered_df['gdpPercap'],y=new_filtered_df['lifeExp'],name=continent_name,mode='markers',opacity=0.7,marker=dict(size=10)))

    return {'data':trace,'layout':go.Layout(
        xaxis=dict(title="GDP per Capita",type='log'),
        yaxis=dict(title="Life Expectancy"),
        hovermode='closest'
    ),'paper_bgcolor': 'black','plot_bgcolor': 'black'}
    
if __name__ == "__main__":
    app.run_server()
