import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dir import DirOpt

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()


tab_geo = pd.read_csv(f"{base_dir}/tab_geo.csv")
px.set_mapbox_access_token("pk.eyJ1Ijoia2FyZW5yb2phcyIsImEiOiJja25tMmw3OWQwbXl6MnBvNTdjam5xdW9jIn0.GkuAPjGFBNUEvZcZ8_-uTw")
fig_map_box = px.scatter_mapbox(tab_geo,
                        lat="LATITUD_Y",
                        lon="LONGITUD_X",
                        hover_name="COMUNAS_ZONAS_DESCRIPCION",
                        color="n",
                        size="n",
                        zoom=10,title="Cantidad de delitos por sector",
                        opacity=0.4)
fig_map_box.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

filters = dbc.Card(
    children=[
        dbc.CardBody(
            [
                html.Div(children=[
                    html.Label('Dropdown'),
                    dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),

                    html.Br(),
                    html.Br(),
                    html.Label('Multi-Select Dropdown'),
                    dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'],
                                 ['Montréal', 'San Francisco'],
                                 multi=True),
                ], style={'padding': 15, 'flex': 1, 'width': '100%'}),

                html.Div(children=[
                    html.Label('Slider'),
                    dcc.Slider(
                        min=0,
                        max=9,
                        marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
                        value=5,
                    ),
                ], style={'padding': 10, 'flex': 1})
            ]
        ),
    ],
    style={"width": "100%",  "margin": 20, "height": "auto", },
)


