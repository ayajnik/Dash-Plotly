import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\SourceData\nst-est2017-alldata.csv')

# grab just the six Northeast states:
df2 = df[df['DIVISION']=='2']
# set the index to state name:
df2.set_index('NAME', inplace=True)

##getting the population colums
columns = [cols for cols in df2.columns if cols.startswith('POP')]

df_final = df2[columns]

##plotting the data

data = [
    go.Scatter(
        x = df_final.columns,
        y = df_final.loc[name],
        mode = 'lines',
        name = "Population trend"
    )
    for name in df_final.index
]

layout = go.Layout(
    title="Population trend in Northeast States",
    xaxis={"title":"x-axis"},
    yaxis={"title":"y-axis"}
)

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,filename='lines2.html')