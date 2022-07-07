from dash import html, dcc
from dir import DirOpt
from components.crimes.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
Base_delitos = data_treatment.crimes_to_info()

class CrimeNationality:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_per_nationality():
        tab_pais = Base_delitos["PAIS_PERSONA"].value_counts(normalize=True).reset_index().sort_values(
            by="PAIS_PERSONA", ascending=False).head(15)

        fig = px.bar(tab_pais, x="PAIS_PERSONA", y="index", orientation='h',
                     height=600, width=500,
                     title='Crimes per nationality',
                     text_auto='.4s')

        fig.update_layout(font_family="Century Gothic",
                          paper_bgcolor='rgb(255, 255, 255)',
                          plot_bgcolor='rgb(255, 255, 255)')
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_per_nationality())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

