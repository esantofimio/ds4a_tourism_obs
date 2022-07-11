from dash import html, dcc
from dir import DirOpt
from components.crimes.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import plotly.express as px

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
Base_delitos = data_treatment.crimes_to_info()

class GenderVictimsAge:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_gender_victims_per_age():
        # Creamos df para realizar el gráfico

        # Filtrar
        obj = Base_delitos[["GENERO", "EDAD"]].value_counts(normalize=False).reset_index()
        women_bins = np.array(-obj[obj['GENERO'] == 'FEMENINO'][0])
        men_bins = np.array(obj[obj['GENERO'] == 'MASCULINO'][0])
        Age = np.array(obj[obj['GENERO'] == 'MASCULINO']['EDAD'])

        layout = go.Layout(margin=dict(l=0, t=0, r=0, b=0, pad=0),
                           height=800,
                           yaxis=go.layout.YAxis(title='Age'),
                           paper_bgcolor='rgb(255, 255, 255)',
                           plot_bgcolor='rgb(255, 255, 255)',
                           xaxis=go.layout.XAxis(
                               range=[-20, 20],
                               tickvals=[-20, -10, 0, -10, -20],
                               ticktext=[-20, -10, 0, 10, 20],
                               title='Number'),
                           barmode='overlay',
                           bargap=0.1)

        data = [go.Bar(y=Age,
                       x=men_bins,
                       orientation='h',
                       name='Men',
                       hoverinfo='x',
                       marker=dict(color='powderblue')
                       ),
                go.Bar(y=Age,
                       x=women_bins,
                       orientation='h',
                       name='Women',
                       text=-1 * women_bins.astype('int'),
                       hoverinfo='text',
                       marker=dict(color='seagreen')
                       )]
        fig = go.Figure(data=data, layout=layout)
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_gender_victims_per_age())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

