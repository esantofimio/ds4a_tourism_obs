from dash import html, dcc
from dir import DirOpt
from components.airbnb.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from scipy import stats


dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
Airbnb_clean = data_treatment.airbnb_info()

class CostPerSector:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    @staticmethod
    def fig_travel_reason():
        ADR_USD_trans, lambdat = stats.boxcox(Airbnb_clean['Average Daily Rate (USD) Def'])
        Airbnb_clean['ADR_USD_trans'] = ADR_USD_trans
        X = Airbnb_clean[['Latitude', 'Longitude']]
        kmeans = KMeans(n_clusters=4).fit(X)
        labels = kmeans.predict(X)
        Airbnb_clean['labels'] = labels
        Airbnb_clean['labels'] = Airbnb_clean['labels'].astype("category")

        fig = px.box(Airbnb_clean, x='labels', y='ADR_USD_trans', \
                     range_y=[Airbnb_clean['ADR_USD_trans'].min(),
                              Airbnb_clean['ADR_USD_trans'].max() + 0.5], \
                     color_discrete_sequence=['salmon'],
                     width=800, height=400)

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
                        dcc.Graph(figure=self.fig_travel_reason())
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )
        return layout

