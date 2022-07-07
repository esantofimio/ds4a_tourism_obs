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

class ClusteringAirbnb:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_clustering_airbnb():
        X = Airbnb_clean[['Latitude', 'Longitude']]
        kmeans = KMeans(n_clusters=4).fit(X)
        labels = kmeans.predict(X)
        Airbnb_clean['labels'] = labels
        Airbnb_clean['labels'] = Airbnb_clean['labels'].astype("category")
        labels = kmeans.predict(X)
        fig = px.scatter(Airbnb_clean, x="Latitude", y="Longitude", color=labels)
        return fig

    def display(self):
        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dcc.Graph(figure=self.fig_clustering_airbnb())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

