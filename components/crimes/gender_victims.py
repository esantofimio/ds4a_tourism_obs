from dash import html, dcc
from dir import DirOpt
from components.crimes.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
Base_delitos = data_treatment.crimes_to_info()

class GenderVictims:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_gender_victims():
        # Creamos df para realizar el gráfico

        # Filtrar
        tabna = pd.DataFrame(Base_delitos.isnull().sum(), columns=["NA's"])
        tabna["%"] = tabna["NA's"] / Base_delitos.shape[0] * 100
        tabna[tabna["%"] > 0]
        Base_delitos_geo = Base_delitos.dropna(subset=["LATITUD_Y", "LONGITUD_X"])
        Base_delitos_geo.shape
        tab_genero = Base_delitos["GENERO"].value_counts(normalize=True).reset_index()
        tab_genero

        dic = {'MASCULINO': 'Man', 'FEMENINO': 'Woman'}
        tab_genero['Gender'] = tab_genero['index'].replace(dic)
        tab_genero = tab_genero.rename(columns={'GENERO': 'Percentage'})

        # Hacer el grafico
        fig = px.pie(tab_genero, values='Percentage', names='Gender', \
                     color='Gender', title='Gender of the victims, accumulated since 2010 to 2022', hole=.4,
                     color_discrete_sequence=px.colors.qualitative.Dark24)

        fig.update_layout(font_family="Century Gothic")
        fig.update_traces(textposition='inside', textinfo='percent+label')

        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_gender_victims())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

