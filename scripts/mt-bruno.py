import plotly.graph_objects as go
import pandas as pd

z_data = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv"
)

fig = go.Figure(
    data=go.Surface(z=z_data.values),
    layout=go.Layout(
        title="Mt Bruno Elevation",
        width=500,
        height=500,
    ),
)

fig.update_layout(template="plotly_dark", title="Mt Bruno Elevation")
# fig.show()
fig.write_json("plots/json/mtbruno.json")
