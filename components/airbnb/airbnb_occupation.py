from dash import html, dcc
from dir import DirOpt
from components.airbnb.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
Airbnb_clean = data_treatment.airbnb_info()

class AirbnbOccupation:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_airbnb_occupation():
        Indicadores = pd.read_excel(f'{base_dir}/tourism_indicators.xlsx')
        diccionario1 = {"Enero": "Ene", "Febrero": "Feb", "Marzo": "Mar", "Abril": "Abr", "Mayo": "May",
                        "Junio": "Jun", "Julio": "Jul", "Agosto": "Ago", "Septiembre": "Sep", "Octubre": "Oct",
                        "Noviembre": "Nov", "Diciembre": "Dic", 1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr", 5: "May",
                        6: "Jun", 7: "Jul", 8: "Ago", 9: "Sep", 10: "Oct",
                        11: "Nov", 12: "Dic"}

        diccionario2 = {"Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6, "Julio": 7,
                        "Agosto": 8, "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12,
                        1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12}

        Indicadores['Mes_norm'] = Indicadores['Mes'].replace(diccionario1)
        Indicadores['Mes_num'] = Indicadores['Mes'].replace(diccionario2)
        Indicadores['AÑO_norm'] = Indicadores['AÑO'].astype(str)
        # Creamos df para realizar el gráfico
        Ocupación_Airbnb = Indicadores.loc[(Indicadores.TEMA == 'Tasa de ocupación Airbnb') &
                                           (Indicadores.SUBTEMA == 'Mensual')].sort_values(by='AÑO')

        Ocupación_Airbnb['Mes_num'] = Ocupación_Airbnb['Mes_num'].astype(int)
        Ocupación_Airbnb['dia'] = 1
        Ocupación_Airbnb['AÑO'] = Ocupación_Airbnb['AÑO'].astype(int)

        # Concatenamos las columnas del año, mes y día
        Ocupación_Airbnb['Date'] = Ocupación_Airbnb.AÑO.apply(str) + '/' + Ocupación_Airbnb.Mes_num.apply(
            str) + '/' + Ocupación_Airbnb.dia.apply(str)
        # Convertimos la nueva columna al tipo fecha
        Ocupación_Airbnb['Date'] = pd.to_datetime(Ocupación_Airbnb['Date'], format='%Y/%m/%d',
                                                  infer_datetime_format=True)
        Ocupación_Airbnb['Value'] = (Ocupación_Airbnb['Valor'] * 100)
        Ocupación_Airbnb = Ocupación_Airbnb.sort_values(by=['Date'])

        fig = px.line(Ocupación_Airbnb, x='Date', y='Value',
                      title='Historical behavior of the Airbnb occupancy rate (%)', \
                      width=750, height=600, color_discrete_sequence=px.colors.qualitative.Set1)

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(buttons=list([dict(count=1, label="1y", step="year", stepmode="todate"),
                                             dict(count=2, label="2y", step="year", stepmode="todate"),
                                             dict(count=3, label="3y", step="year", stepmode="todate"),
                                             dict(count=4, label="4y", step="year", stepmode="todate"),
                                             dict(step="all")])))

        fig.update_layout(font_family="Century Gothic",
                          paper_bgcolor='rgb(255, 255, 255)',
                          plot_bgcolor='rgb(255, 255, 255)',
                          showlegend=False)
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_airbnb_occupation())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

