from dash import html, dcc
from dir import DirOpt
from components.migrate.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import plotly.express as px

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
df = data_treatment.migration_to_info()

class YearAge:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_year_age():
        df_graph = df.groupby(['Año', 'Reason for trip'])['Fac Exp'].sum().to_frame() \
            .sort_values(by=['Fac Exp'], ascending=False).reset_index()
        # ordenamos el df
        df_graph = df_graph.sort_values(by=['Año', 'Reason for trip'], ascending=[True, True])
        # renombramos columnas
        df_graph = df_graph.rename(columns={'Fac Exp': 'Number of travelers', 'Año': 'Year'})

        historico = df.groupby(['Año', 'Reason for trip'])['Fac Exp'].sum().to_frame().reset_index()
        historico['Año'] = historico['Año'].astype(str)
        # renombramos columnas
        historico = df_graph.rename(columns={'Fac Exp': 'Number of travelers', 'Año': 'Year'})
        historico['Year'] = historico['Year'].astype(str)

        # realizamos grafico
        fig = px.line(historico, x='Year', y='Number of travelers', animation_frame='Reason for trip', \
                      range_y=[0, historico['Number of travelers'].max() + 120000], \
                      markers=True, text='Number of travelers',
                      color='Reason for trip', color_discrete_sequence=px.colors.qualitative.Bold,
                      width=500, height=500)

        fig.update_layout(font_family="Century Gothic",
                          paper_bgcolor='rgb(255, 255, 255)',
                          plot_bgcolor='rgb(255, 255, 255)',
                          showlegend=False)

        fig.update_traces(textposition="top center", texttemplate="%{y:,.0f}")

        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_year_age())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

