from dash import html, dcc
from dir import DirOpt
from components.migrate.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
df = data_treatment.migration_to_info()

class TravelReason:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_travel_reason():
        # Validación de la limpieza realizada, y de que no se haya perdido información
        x = df.groupby('Motivo Viaje')['Fac Exp'].sum().to_frame().reset_index().sort_values(by=['Fac Exp'],
                                                                                             ascending=False)
        y = df.groupby('Reason for trip')['Fac Exp'].sum().to_frame().reset_index().sort_values(by=['Fac Exp'],
                                                                                                ascending=False)
        z = pd.merge(x, y, left_on='Motivo Viaje', right_on='Reason for trip', how='outer')
        valida = (z.loc[z['Reason for trip'] != 'Otros', 'Fac Exp_x'] - z.loc[
            z['Reason for trip'] != 'Otros', 'Fac Exp_y']).sum()
        valida1 = df['Reason for trip'].value_counts().to_frame().reset_index()['Reason for trip'].sum()
        if (valida == 0) & (valida1 - df.shape[0] == 0):
            print("Ranking OK\n")
        else:
            print("Ranking Wrong\n")

        # Creamos el df para graficar
        df_graph = df.groupby(['Año', 'Reason for trip'])['Fac Exp'].sum().to_frame() \
            .sort_values(by=['Fac Exp'], ascending=False).reset_index()
        # ordenamos el df
        df_graph = df_graph.sort_values(by=['Año', 'Reason for trip'], ascending=[True, True])
        # renombramos columnas
        df_graph = df_graph.rename(columns={'Fac Exp': 'Number of travelers', 'Año': 'Year'})

        # realizamos grafico
        fig = px.bar(df_graph, x='Reason for trip', y='Number of travelers',\
                     text_auto='.2s', animation_frame='Year', range_y=[0, df_graph['Number of travelers'].max()],\
                     color='Reason for trip', color_discrete_sequence=px.colors.qualitative.Bold,
                     width=650, height=300)

        fig.update_layout(font_family="Century Gothic",
                          paper_bgcolor='rgb(255, 255, 255)',
                          plot_bgcolor='rgb(255, 255, 255)',
                          showlegend=False)

        fig.update_yaxes(visible=False)
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

