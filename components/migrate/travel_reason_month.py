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

class TravelReasonMonth:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID


    @staticmethod
    def fig_travel_reason():
        # Limpieza de datos
        # 2. Normalizamos los nombres de los meses, para que sea un campo ordinal, y así poder analizarlo adecuadamente
        diccionario = {"Enero": "01-Jan", "Febrero": "02-Feb", "Marzo": "03-Mar", "Abril": "04-Apr", "Mayo": "05-May",
                       "Junio": "06-Jun", "Julio": "07-Jul", "Agosto": "08-Aug", "Septiembre": "09-Sep",
                       "Octubre": "10-Oct",
                       "Noviembre": "11-Nov", "Diciembre": "12-Dec"}

        df["Month"] = df["Meses1"].replace(diccionario)

        # Agrupar para hacer el gráfico
        meses = df.groupby(['Año', 'Month', 'Reason for trip'])['Fac Exp'].sum().to_frame().reset_index()

        # ordenamos el df
        meses = meses.sort_values(by=['Año', 'Month', 'Reason for trip'], ascending=[True, True, True])
        # renombramos columnas
        meses = meses.rename(columns={'Fac Exp': 'Number of travelers', 'Año': 'Year'})

        # realizamos grafico
        fig = px.line(meses, x='Month', y='Number of travelers', animation_frame='Year',
                      range_y=[0, meses['Number of travelers'].max()],
                      markers=True, color='Reason for trip', color_discrete_sequence=px.colors.qualitative.Bold,
                      width=1200, height=500)

        fig.update_layout(font_family="Century Gothic", paper_bgcolor='rgb(255, 255, 255)',
                          plot_bgcolor='rgb(255, 255, 255)')
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_travel_reason())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

