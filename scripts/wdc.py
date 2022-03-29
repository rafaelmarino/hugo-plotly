import plotly.graph_objects as go
import pandas as pd


def plot_wdc(df, title_type="full"):
    """Create a plotly chart of cumulative points for F1WDC"""
    flags1 = ["🇧🇭", "🇮🇹", "🇵🇹", "🇪🇸", "🇲🇨", "🇦🇿", "🇫🇷", "🇦🇹"]
    flags2 = ["🇦🇹2 ", "🇬🇧", "🇭🇺", "🇧🇪", "🇳🇱", "🇮🇹2 ", "🇷🇺", "🇹🇷"]
    flags3 = ["🇺🇸", "🇲🇽", "🇧🇷", "🇶🇦", "🇸🇦", "🇦🇪"]
    flags = flags1 + flags2 + flags3

    fig = go.Figure()
    # Add traces
    for driver in df.index:
        fig.add_trace(
            go.Scatter(
                x=flags,
                y=df.loc[driver],
                mode="lines+markers",
                name=driver,
                # marker_symbol="circle",
                # marker=dict(
                #     size=5,
                #     line=dict(width=2),
                # ),
            )
        )
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
            text="Cumulative Points",
            font=dict(family="Ubuntu", size=18, color="white"),
        ),
        tickfont=dict(family="Ubuntu", size=16, color="white"),
    )
    if title_type == "full":
        title_text = "🏁 F1 World Drivers' Championship 2021 🏁"
    elif title_type == "top10":
        title_text = "F1 World Drivers' Championship 2021 (Top10) 🏁"
    elif title_type == "rest":
        title_text = "F1 World Drivers' Championship 2021 (Pos11+) 🏁"
    fig.update_layout(
        paper_bgcolor="#0e1317",
        plot_bgcolor="#0e1317",
        title=dict(
            text=title_text,
            font=dict(family="Ubuntu", size=20, color="white"),
            xanchor="center",
            x=0.5,
        ),
        legend=dict(
            font=dict(family="Sans", size=11, color="white"),
        ),
    )
    return fig


if __name__ == "__main__":
    df = pd.read_csv("data/wdc_points.csv", index_col=0)
    # all drivers
    fig = plot_wdc(df)
    fig.write_image("plots/f1wdc2021.png")
    fig.write_json("plots/f1wdc2021.json")
    # top 10 drivers
    fig = plot_wdc(df.iloc[:10], title_type="top10")
    fig.write_image("plots/f1wdc2021-top10.png")
    fig.write_json("plots/f1wdc2021-top10.json")
    # rest
    fig = plot_wdc(df.iloc[10:], title_type="rest")
    fig.write_image("plots/f1wdc2021-rest.png")
    fig.write_json("plots/f1wdc2021-rest.json")
