from dash import html, dcc
from dir import DirOpt
from components.migrate.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import plotly.express as px

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
df = data_treatment.migration_to_info()

class AgeTourism:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_age_tourism():
        edad = df.groupby(['Reason for trip', 'Rango Edad'])['Fac Exp'].sum()
        edad = edad.to_frame().reset_index()

        # renombramos columnas
        edad = edad.rename(columns={'Fac Exp': 'Number of travelers', 'Año': 'Year', 'Rango Edad': 'Age Range'})

        # realizamos grafico
        fig = px.bar(edad, x='Age Range', y='Number of travelers', text_auto='.2s', animation_frame='Reason for trip',
                     range_y=[edad['Number of travelers'].min(), edad['Number of travelers'].max()],
                     color='Reason for trip', color_discrete_sequence=px.colors.qualitative.Bold,
                     width=500, height=300)

        fig.update_layout(font_family="Century Gothic", paper_bgcolor='rgb(255, 255, 255)',
                          plot_bgcolor='rgb(255, 255, 255)', showlegend=False)

        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_age_tourism())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

