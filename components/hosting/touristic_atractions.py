from dash import html, dcc
from dir import DirOpt
from components.migrate.data_treatment import DataTreatment
from components.hosting.hosting_geo_data import HostingGeoData
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from urllib.request import urlopen
import json

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
df = data_treatment.migration_to_info()
hosting_geo_data = HostingGeoData()
bogota_geo_ok = hosting_geo_data.geo_data()

class TouristicAtractions:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_touristic_atractions():
        touristic_atractions = pd.read_excel(f'{base_dir}/atractivos_turisticos.xlsx')

        fig = px.scatter_mapbox(touristic_atractions, lat="Latitud", lon="Longitud",
                                color_continuous_scale=px.colors.cyclical.IceFire, size_max=20, zoom=10,
                                mapbox_style="carto-positron")
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_touristic_atractions())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

