import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r'E:\Python development\Dash-Plotly\Plotly-Dashboards-with-Dash-master\Data\2010YumaAZ.csv')

#days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MODAY']
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']
data = []
for day in days:
    trace = go.Scatter(
            x=df['LST_TIME'],
            y = df.loc[df['DAY']==day]['T_HR_AVG'],
            mode = 'lines',
            name = day
        )
    
    data.append(trace)

layout = go.Layout(
    title="Average temperature distribution",
    xaxis={"title":"x-axis"},
    yaxis={"title":"y-axis"}
)

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,filename='lines3.html')