from dash import html, dcc
from dir import DirOpt
from components.crimes.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np


dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
Base_delitos = data_treatment.crimes_to_info()

class TimeDay:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID


    @staticmethod
    def fig_time_day():
        tab_moment = Base_delitos.groupby(['Año', 'MOMENTO_DIA'])['Dia'].count().to_frame().reset_index()
        dicc_moment = {'Tarde': 'Afternoon', 'Madrugada': 'Dawn', 'Mañana': 'Morning', 'Noche': 'Night'}
        tab_moment["MOMENTO_DIA"] = tab_moment["MOMENTO_DIA"].map(dicc_moment)
        tab_moment = tab_moment.rename(columns={'Año': 'Year', 'MOMENTO_DIA': 'Time of Day', 'Dia': 'Number of cases'})

        fig = px.bar(tab_moment, x='Year', y='Number of cases', color='Time of Day', height=500, text='Number of cases',
                     range_y=[0, tab_moment['Number of cases'].max() + 250], width=1200)

        fig.update_layout(font_family="Century Gothic")
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide')
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_time_day())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

