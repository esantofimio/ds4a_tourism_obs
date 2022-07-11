from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc

from components import navbar
from components.airbnb.city_sectors_airbnb import CitySectorsAirbnb
from components.airbnb.clustering_airbnb import ClusteringAirbnb
from components.airbnb.prediction_model import PredictionModel
from components.airbnb.cost_per_sector import CostPerSector
from components.airbnb.airbnb_occupation import AirbnbOccupation
from components.airbnb.hotel_occupation import HotelOccupation

city_sectors_airbnb = CitySectorsAirbnb('City zones', 'id_city_sectors_airbnb')
clustering_airbnb = ClusteringAirbnb('Clustering zones', 'id_clustering_airbnb')
cost_per_sector = CostPerSector('Pricing airbnb', 'cost_per_sector')
prediction_model = PredictionModel('Prediction', 'id_prediction_model')
airbnb_occupation = AirbnbOccupation('AirbnbOccupation', 'id_airbnb_occupation')
hotel_occupation = HotelOccupation('HotelOccupation', 'id_hotel_occupation')

pricing_airbnb = html.Div([
    dbc.Row([
        dbc.Col([
            navbar.navbar,
            dbc.Row([
                dbc.Col([
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Row(
                                ),
                                width={"size": 1, "order": 5},
                            ),
                            dbc.Col(
                                dbc.Row(
                                    [
                                        prediction_model.display(),
                                    ]
                                ),
                                width={"size": 5, "order": 5},
                            ),
                            dbc.Col(
                                dbc.Row(
                                    [
                                        airbnb_occupation.display(),
                                        hotel_occupation.display(),
                                    ]
                                ),
                                width={"size": 5, "order": 5}
                            ),
                            dbc.Col(
                                dbc.Row(
                                ),
                                width={"size": 1, "order": 5},
                            ),
                        ]
                    ),

                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Row(
                                ),
                                width={"size": 1, "order": 5},
                            ),
                            dbc.Col(
                                dbc.Row(
                                    [
                                        city_sectors_airbnb.display(),
                                        cost_per_sector.display(),

                                    ]
                                ),
                                width={"size": 5, "order": 5},
                            ),
                            dbc.Col(
                                dbc.Row(
                                    [
                                        clustering_airbnb.display(),
                                    ]
                                ),
                                width={"size": 5, "order": 5}
                            ),
                            dbc.Col(
                                dbc.Row(
                                ),
                                width={"size": 1, "order": 5},
                            ),
                        ]
                    ),
                ],
                    width={"size": 12, "order": 2},
                ),
            ]),
        ]),
    ]),
],
    style={'backgroundColor': '#fafafa'}
)