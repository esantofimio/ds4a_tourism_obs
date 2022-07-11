from dash import html, dcc
from dir import DirOpt
from components.airbnb.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
Airbnb_clean = data_treatment.airbnb_info()

class CitySectorsAirbnb:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_sectors_airbnb():
        fig = px.scatter(Airbnb_clean, x="Latitude", y="Longitude", color="Localidad")
        fig.update_layout(font_family="Century Gothic",
                          paper_bgcolor='rgb(255, 255, 255)',
                          plot_bgcolor='rgb(255, 255, 255)')
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_sectors_airbnb())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

