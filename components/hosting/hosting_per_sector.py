from dash import html, dcc
from dir import DirOpt
from components.migrate.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np


dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
df = data_treatment.migration_to_info()

class HostingPerSecond:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID


    @staticmethod
    def fig_hosting_sector():
        hosting_spots = pd.read_excel(f'{base_dir}/hosting.xlsx')
        fig = px.bar(hosting_spots, x='LOCALIDAD', height=400,
                     title='Crimes Frequency by month of the year')

        fig.update_layout(font_family="Century Gothic", paper_bgcolor='rgb(255, 255, 255)',
                          plot_bgcolor='rgb(255, 255, 255)')
        fig.update_traces(texttemplate='%{text:0.0%}', textposition='outside')
        fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide')
        fig.update_yaxes(visible=False)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_hosting_sector())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

