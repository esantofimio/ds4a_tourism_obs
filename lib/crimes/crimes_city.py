import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

tab_geo = pd.read_csv("/Users/esanto/PycharmProjects/DashTutorial/observatorio_turismo/data/tab_geo.csv")
px.set_mapbox_access_token("pk.eyJ1Ijoia2FyZW5yb2phcyIsImEiOiJja25tMmw3OWQwbXl6MnBvNTdjam5xdW9jIn0.GkuAPjGFBNUEvZcZ8_-uTw")
fig_map_box = px.scatter_mapbox(tab_geo,
                        lat="LATITUD_Y",
                        lon="LONGITUD_X",
                        hover_name="COMUNAS_ZONAS_DESCRIPCION",
                        color="n",
                        size="n",
                        zoom=10,title="Cantidad de delitos por sector",
                        opacity=0.4)
fig_map_box.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

card_map = dbc.Card(
    children=[
        dbc.CardBody(
            [
                dcc.Graph(
                    id='example-graph_box',
                    figure=fig_map_box
                )
            ]
        ),
    ],
    style={"width": "100%",  "margin": 20, "height": "auto", },
)