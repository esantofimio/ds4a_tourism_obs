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

class Hour:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_hour():
        tab_hora = Base_delitos["HORA_HECHO"].value_counts(normalize=True).reset_index().sort_values(by="index",
                                                                                                     ascending=True)
        tab_hora = tab_hora.rename(columns={'index': 'Hour', 'HORA_HECHO': 'Cases (%)'})
        tab_hora['Cases (%)'] = tab_hora['Cases (%)'] * 100
        fig = px.area(tab_hora, x='Hour', y="Cases (%)", title="Crimes by time of day")
        fig.update_layout(font_family="Century Gothic")
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_hour())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

