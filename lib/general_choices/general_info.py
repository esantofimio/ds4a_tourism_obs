from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df_pie_plot = px.data.tips()
fig_pie_plot = px.pie(df_pie_plot, values='tip', names='day', color_discrete_sequence=px.colors.sequential.Blues)
fig_pie_plot.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height = 145)
fig_pie_plot.update(layout_showlegend=False)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig.update_layout(
    margin=dict(l=10, r=10, t=10, b=10),
)

df_boxplot = px.data.tips()

fig_boxplot = px.box(df_boxplot, x="day", y="total_bill", color="smoker")
fig_boxplot.update_traces(quartilemethod="exclusive")
fig_boxplot.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


card = dbc.Card(
    children=[
        dbc.CardHeader("This is the header"),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P("This is some card text", className="card-text"),
            ]
        ),
        dbc.CardFooter("This is the footer"),
    ],
    style={"width": "100%",  "margin": 20, "height": "12rem", },
)



card_indicators_pie_plot = dbc.Card(
    children=[
        dbc.CardBody(
            [
                dcc.Graph(
                    id='example-graph_pie_plot',
                    figure=fig_pie_plot
                )
            ],
            className="card-primary"
        ),
    ],
    style={"width": "100%",  "margin": 20, "height": "12rem"},

)

card_statistics_bar = dbc.Card(
    children=[
        dbc.CardHeader("This is the header"),
        dbc.CardBody(
            [
                dcc.Graph(
                    id='example-graph_bar',
                    figure=fig
                )
            ]
        ),
    ],
    style={"width": "100%",  "margin": 20, "height": "auto", },
)


card_statistics_line = dbc.Card(
    children=[
        dbc.CardHeader("This is the header"),
        dbc.CardBody(
            [
                dcc.Graph(
                    id='example-graph_line',
                    figure=fig_boxplot
                )
            ]
        ),
    ],
    style={"width": "100%",  "margin": 20, "height": "auto", },
)
card_statistics_violin = dbc.Card(
    children=[
        dbc.CardHeader("This is the header"),
        dbc.CardBody(
            [
                dcc.Graph(
                    id='example-graph_violin',
                    figure=fig
                )
            ]
        ),
    ],
    style={"width": "100%",  "margin": 20, "height": "auto", },
)
