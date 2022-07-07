from dash import html, dcc
from dir import DirOpt
from components.migrate.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import plotly.express as px

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
df = data_treatment.migration_to_info()

class TouristRegion:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_travel_reason():
        # Creamos df para realizar el gráfico

        # Filtrar
        df2 = df.loc[df['Reason for trip'] == 'Tourism']

        procedencia = df2.groupby(['Reason for trip', 'Año', 'Region Nacionalidad'])['Fac Exp'].sum()
        procedencia = procedencia.to_frame().reset_index().sort_values(
            by=['Reason for trip', 'Año', 'Region Nacionalidad'])

        dic = {'América del Sur': 'South America', 'América del Norte': 'North America', 'Europa': 'Europa',
               'América Central y el Caribe': 'Central America and the Caribbean', 'Asia': 'Asia',
               'Naciones Unidas': 'United Nations',
               'Oceanía': 'Oceania', 'Sin Especificar': 'Unspecified', 'África': 'Africa'}

        shape_before = procedencia.shape
        procedencia['Region Nacionalidad'] = procedencia['Region Nacionalidad'].replace(dic)
        shape_after = procedencia.shape

        # renombramos columnas
        procedencia = procedencia.rename(columns={'Fac Exp': 'Number of travelers', 'Año': 'Year',
                                                  'Region Nacionalidad': 'Nationality'})

        # Validar que en la aplicacion del diccionario no se hayan perdido datos
        if shape_before != shape_after:
            print("Wrong")
        else:
            print("OK")

        # Hacer el grafico
        fig = px.pie(procedencia, values='Number of travelers', names='Nationality', \
                     color='Nationality',
                     title='# tourists by region, 2017 - 2021', hole=.4,
                     color_discrete_sequence=px.colors.qualitative.Set2)

        fig.update_layout(font_family="Century Gothic", paper_bgcolor='rgb(255, 255, 255)',
                          plot_bgcolor='rgb(255, 255, 255)',
                          width=450, height=400)

        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

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

