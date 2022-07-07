from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

card_indicators = dbc.Card(
    children=[
        dbc.CardBody(
            [
                html.H2("38.72", className="card-title"),
                html.P(
                    "Data"
                ),
            ],
            className="card-primary"
        ),
    ],
    style={"width": "100%",  "margin": 20, "height": "8rem", "padding": "1rem"},

)