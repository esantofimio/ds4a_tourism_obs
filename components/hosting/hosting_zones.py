from dash import html, dcc
from dir import DirOpt
from components.migrate.data_treatment import DataTreatment
from components.hosting.hosting_geo_data import HostingGeoData
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from urllib.request import urlopen
import json
import plotly.graph_objs as go
from plotly.offline import iplot

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
df = data_treatment.migration_to_info()
hosting_geo_data = HostingGeoData()
bogota_geo_ok = hosting_geo_data.geo_data()

class HostingZones:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_hosting_zones():
        tab_geo = pd.read_csv(f'{base_dir}/tab_geo.csv')
        hosting_spots = pd.read_excel(f'{base_dir}/hosting.xlsx')

        hosting_spots['BARRIO'] = hosting_spots['BARRIO'].str.upper()
        hosting_spots = hosting_spots[~hosting_spots['BARRIO'].isna()]
        hosting_spots = hosting_spots.reset_index(drop=True)
        hosting_spots['id'] = list(hosting_spots.index)
        hosting_spots['id'] = hosting_spots['id'] + 1
        hosting_spots_neighborhoods = hosting_spots.groupby('BARRIO')['id'].count()
        hosting_spots_neighborhoods = hosting_spots_neighborhoods.to_frame().reset_index()
        print(hosting_spots_neighborhoods)

        trace1 = go.Scattermapbox(
            lat=list(tab_geo["LATITUD_Y"]),
            lon=list(tab_geo["LONGITUD_X"]),
            marker=dict(size=10, color='#ff0000', opacity=0.5)
        )

        trace2 = go.Choroplethmapbox(
            geojson=bogota_geo_ok,
            locations=hosting_spots_neighborhoods['BARRIO'],
            z=hosting_spots_neighborhoods['id'],
            colorscale="Viridis",
            marker_opacity=0.5,
            zmin=0,
            zmax=80
        )

        layout = dict(margin=dict(l=0, t=0, r=0, b=0, pad=0),
                      height=1100,
                      mapbox=dict(
                          accesstoken="pk.eyJ1Ijoia2FyZW5yb2phcyIsImEiOiJja25tMmw3OWQwbXl6MnBvNTdjam5xdW9jIn0.GkuAPjGFBNUEvZcZ8_-uTw",
                          center=dict(lat=4.704121, lon=-74.042742),
                          style='light',
                          zoom=11))
        data = [trace2]
        fig = go.Figure(data=data, layout=layout)
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_hosting_zones())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

