import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df_map = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

fig_choropleth = px.choropleth(df_map, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
fig_choropleth.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

card_map = dbc.Card(
    children=[
        dbc.CardBody(
            [
                dcc.Graph(
                    id='example-graph_map',
                    figure=fig_choropleth
                )
            ]
        ),
    ],
    style={"width": "100%",  "margin": 20, "height": "auto", },
)