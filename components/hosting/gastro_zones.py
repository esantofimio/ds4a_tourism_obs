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

class GastroZones:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_gastro_zones():
        hosting_spots = pd.read_excel(f'{base_dir}/hosting.xlsx')

        hosting_spots['BARRIO'] = hosting_spots['BARRIO'].str.upper()
        hosting_spots = hosting_spots[~hosting_spots['BARRIO'].isna()]
        hosting_spots = hosting_spots.reset_index(drop=True)
        hosting_spots['id'] = list(hosting_spots.index)
        hosting_spots['id'] = hosting_spots['id'] + 1
        hosting_spots_neighborhoods = hosting_spots.groupby('BARRIO')['id'].count()
        hosting_spots_neighborhoods = hosting_spots_neighborhoods.to_frame().reset_index()
        filter_hosting_spots_gastro = [
            'Establecimiento de gastronomía y similares',
        ]
        hosting_spots_gastro = hosting_spots[hosting_spots['CATEGORIA'].isin(filter_hosting_spots_gastro)]
        hosting_spots_gastro = hosting_spots_gastro.reset_index(drop=True)
        hosting_spots_gastro_neighborhoods = hosting_spots_gastro.groupby('BARRIO')['id'].count()
        hosting_spots_gastro_neighborhoods = hosting_spots_gastro_neighborhoods.to_frame().reset_index()
        fig = px.choropleth_mapbox(hosting_spots_gastro_neighborhoods,
                                   geojson=bogota_geo_ok,
                                   locations='BARRIO',
                                   color='id',
                                   color_continuous_scale="Viridis",
                                   range_color=(0, 80),
                                   mapbox_style="carto-positron",
                                   zoom=10,
                                   center={"lat": 4.704121, "lon": -74.042742},
                                   opacity=0.5,
                                   labels={'id': 'hosting places'}
                                   )
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                          height=1100)
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_gastro_zones())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

