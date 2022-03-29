import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data/wdc_points.csv", index_col=0)

flags1 = ["🇧🇭", "🇮🇹", "🇵🇹", "🇪🇸", "🇲🇨", "🇦🇿", "🇫🇷", "🇦🇹"]
flags2 = ["🇦🇹2 ", "🇬🇧", "🇭🇺", "🇧🇪", "🇳🇱", "🇮🇹2 ", "🇷🇺", "🇹🇷"]
flags3 = ["🇺🇸", "🇲🇽", "🇧🇷", "🇶🇦", "🇸🇦", "🇦🇪"]
flags = flags1 + flags2 + flags3

fig = go.Figure()

# Add traces
for driver in df.iloc[10:].index:
    fig.add_trace(
        go.Scatter(x=flags, y=df.loc[driver], mode="lines+markers", name=driver)
    )

# fig.add_trace(
#     go.Scatter(x=flags, y=df.loc["Verstappen"], mode="lines+markers", name="markers")
# )

fig.update_xaxes(
    showgrid=False,
    gridwidth=0.2,
    gridcolor="#233141",
    color="white",
    title=dict(
        text="",
        font=dict(family="Ubuntu", size=18, color="white"),
    ),
    tickfont=dict(family="Ubuntu", size=16, color="white"),
    tickangle=0,
)
fig.update_yaxes(
    showgrid=True,
    gridwidth=0.5,
    gridcolor="#233141",
    color="white",
    title=dict(
        text="Points",
        font=dict(family="Ubuntu", size=18, color="white"),
    ),
    tickfont=dict(family="Ubuntu", size=16, color="white"),
)
fig.update_layout(
    paper_bgcolor="#0e1317",
    plot_bgcolor="#0e1317",
    title=dict(
        text="🏁 F1 2021 – World Drivers' Championship 🏁",
        font=dict(family="Ubuntu", size=20, color="white"),
        xanchor="center",
        x=0.5,
    ),
    legend=dict(
        font=dict(family="Sans", size=11, color="white"),
    ),
)
fig.write_image("plots/wdc.png")
# fig.show()
fig.write_json("plots/wdc.json")
