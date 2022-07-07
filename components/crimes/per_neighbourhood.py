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

class Neighbourhood:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_neighboudhood():
        Base_delitos_geo = Base_delitos.dropna(subset=["LATITUD_Y", "LONGITUD_X"])
        Base_delitos_geo["COMUNAS_ZONAS_DESCRIPCION"] = Base_delitos_geo["COMUNAS_ZONAS_DESCRIPCION"].fillna(
            "No registra")
        tab_geo = Base_delitos_geo.groupby(
            ["COMUNAS_ZONAS_DESCRIPCION", "LATITUD_Y", "LONGITUD_X"]).size().reset_index()
        tab_geo.columns = ["COMUNAS_ZONAS_DESCRIPCION", "LATITUD_Y", "LONGITUD_X", "n"]
        tab_geo = tab_geo.sort_values(by="n", ascending=False)

        px.set_mapbox_access_token(
            "pk.eyJ1Ijoia2FyZW5yb2phcyIsImEiOiJja25tMmw3OWQwbXl6MnBvNTdjam5xdW9jIn0.GkuAPjGFBNUEvZcZ8_-uTw")
        fig = px.scatter_mapbox(tab_geo,
                                lat="LATITUD_Y",
                                lon="LONGITUD_X",
                                hover_name="COMUNAS_ZONAS_DESCRIPCION",
                                color="n",
                                size="n",
                                zoom=13,
                                title="Cantidad de delitos por sector",
                                opacity=0.4,
                                height=1100)

        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_neighboudhood())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

