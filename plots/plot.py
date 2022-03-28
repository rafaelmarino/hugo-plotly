from turtle import title
import plotly.express as px

# from plotly.io import write_image
# simple demo
# fig = px.bar(x=["a", "b", "c"], y=[4, 2, 3])
# fig.show()


# life expectancy trendline
# df = px.data.gapminder().query("continent == 'Americas'")
countries = ["Canada", "Japan", "Spain", "Norway"]
df = px.data.gapminder().query(f"country in {countries}")
fig = px.line(df, x="year", y="lifeExp", color="country")

# figure configurations
fig.update_xaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor="#233141",
    color="white",
)
fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor="#233141",
    color="white",
)
fig.update_layout(
    paper_bgcolor="#0e1317",
    plot_bgcolor="#0e1317",
    title=dict(
        text="Life Expectancy 1952–2007",
        font=dict(family="Ubuntu", size=18, color="white"),
    ),
)
# fig.show()
fig.write_image("newplot.png")
