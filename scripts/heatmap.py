import plotly.graph_objects as go
import datetime
import pandas as pd
import numpy as np

np.random.seed(1)

programmers = ["Alex", "Nicole", "Sara", "Etienne", "Chelsea", "Jody", "Marianne"]

base = datetime.datetime.today()
dates = base - np.arange(180) * datetime.timedelta(days=1)
z = np.random.poisson(size=(len(programmers), len(dates)))

fig = go.Figure(data=go.Heatmap(z=z, x=dates, y=programmers, colorscale="Viridis"))

fig.update_layout(title="GitHub commits per day", xaxis_nticks=36)


fig.write_image("plots/heatmap.png")

df = pd.read_csv("data/wdc_points.csv", index_col=0)
drivers = df.iloc[:10].index
tracks = df.columns
fig = go.Figure(data=go.Heatmap(z=df, x=tracks, y=drivers, colorscale="Magma"))
fig.write_image("plots/heatmap.png")
