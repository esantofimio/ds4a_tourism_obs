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

class AgeVictim:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_age_victim():
        tab_edad = Base_delitos.groupby(['Año', 'EDAD'])['Dia'].count().to_frame().reset_index()
        tab_edad = tab_edad.rename(columns={'Año': 'Year', 'EDAD': 'Age', 'Dia': 'Number of cases'})

        fig = px.bar(tab_edad, y='Number of cases', x='Age', text='Number of cases', animation_frame='Year',
                     range_y=[0, tab_edad['Number of cases'].max() + 2], title='Number of crimes by age of the victim',
                     width=1200, height=600)

        fig.update_traces(texttemplate='%{text:.0s}', textposition='outside')
        fig.update_layout(font_family="Century Gothic")
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_age_victim())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

