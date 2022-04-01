# import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import json


# import datetime
# import numpy as np

# demo1
# np.random.seed(1)
# programmers = ["Alex", "Nicole", "Sara", "Etienne", "Chelsea", "Jody", "Marianne"]
# base = datetime.datetime.today()
# dates = base - np.arange(180) * datetime.timedelta(days=1)
# z = np.random.poisson(size=(len(programmers), len(dates)))
# fig = go.Figure(data=go.Heatmap(z=z, x=dates, y=programmers, colorscale="Viridis"))
# fig.update_layout(title="GitHub commits per day", xaxis_nticks=36)
# fig.update_layout(
#     paper_bgcolor="#0e1317",
#     plot_bgcolor="#0e1317",
# )
# fig.update_layout(font=dict(color="white"))
# fig.write_image("plots/heatmap_github.png")

# demo2
# fig = go.Figure(
#     data=go.Heatmap(
#         z=[[1, 20, 30], [20, 1, 60], [30, 60, 1]],
#         text=[
#             ["one", "twenty", "thirty"],
#             ["twenty", "one", "sixty"],
#             ["thirty", "sixty", "one"],
#         ],
#         texttemplate="%{text}",
#         textfont={"size": 20},
#     )
# )


def plot_heatmap(df):
    """Plot heatmap of raw scored points for F1 WDC 2021"""
    # fig = go.Figure(
    #     data=go.Heatmap(z=df, x=flags, y=drivers, colorscale="Viridis"),
    #     # labels=dict(color="Points"),
    #     text_auto=True,
    # )
    flags = json.load(open("data/flags.json", "r"))["flags"]
    x_axis = [" ".join(z) for z in zip(df.columns, flags)]
    # print(x_axis)
    fig = px.imshow(
        df,
        x=x_axis,
        labels=dict(x="Grand Prix", y="Driver", color="Points"),
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Viridis",
    )
    fig.update_xaxes(
        title=dict(
            text="",
            font=dict(family="Ubuntu", size=18, color="white"),
        ),
        tickfont=dict(family="Ubuntu", size=16, color="white"),
        tickangle=90,
        side="bottom",
    )
    fig.update_yaxes(
        title=dict(text=""),
        tickfont=dict(family="Ubuntu", size=16, color="white"),
        autorange="reversed",
    )
    fig.update_layout(
        paper_bgcolor="#0e1317",
        plot_bgcolor="#0e1317",
        title=dict(
            text="F1 World Driver's Championship 2021 \u2013 Scored Points Heatmap",
            font=dict(family="Ubuntu", size=22, color="white"),
            xanchor="center",
            x=0.5,
        ),
        legend_title=dict(text="Points"),
        legend=dict(
            font=dict(family="Sans", size=11, color="white"),
        ),
    )
    fig.update_layout(font=dict(color="white"))
    return fig


if __name__ == "__main__":
    df = pd.read_csv("data/wdc_points1.csv", index_col=0)
    fig = plot_heatmap(df)
    fig.write_image("plots/png/heatmap2.png")
    # fig.write_html("plots/html/heatmap.html")
    # fig.write_json("plots/json/heatmap2.json")
    fig.write_json(json.load(open("data/paths.json", "r"))["heatmap2path"])
    # fig.show()
