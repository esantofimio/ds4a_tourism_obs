from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc

from components import navbar
from lib.crimes import crimes_city, indicators as crime_indicators
from components.airbnb.city_sectors_airbnb import CitySectorsAirbnb
from components.airbnb.clustering_airbnb import ClusteringAirbnb
from components.airbnb.prediction_model import PredictionModel
from components.airbnb.cost_per_sector import CostPerSector
from components.hosting.gastro_zones import GastroZones
from components.hosting.touristic_atractions import TouristicAtractions
from components.hosting.hosting_per_sector import HostingPerSecond
from components.hosting import datatable



gastro_zones = GastroZones('Gastro zones', 'id_gastro_zones')
city_sectors_airbnb = CitySectorsAirbnb('City zones', 'id_city_sectors_airbnb')
clustering_airbnb = ClusteringAirbnb('Clustering zones', 'id_clustering_airbnb')
cost_per_sector = CostPerSector('Pricing airbnb', 'cost_per_sector')
touristic_atractions = TouristicAtractions('Touristic zones', 'id_touristic')
hosting_per_sector = HostingPerSecond('Hosting per sector', 'id_hosting_per_sector')
prediction_model = PredictionModel('Prediction', 'id_prediction_model')

pricing_airbnb = html.Div([
    dbc.Row([
        dbc.Col([
            navbar.navbar,
            dbc.Row([
                dbc.Col([
                    dbc.Row(
                        [
                            dbc.Col(
                                crime_indicators.card_indicators,
                                width={"size": 3, "order": 5},
                            ),
                            dbc.Col(
                                crime_indicators.card_indicators,
                                width={"size": 3, "order": 5},
                            ),
                            dbc.Col(
                                crime_indicators.card_indicators,
                                width={"size": 3, "order": 5},
                            ),
                            dbc.Col(
                                crime_indicators.card_indicators,
                                width={"size": 3, "order": 5},
                            ),
                        ],
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Row(
                                    [
                                        prediction_model.display(),
                                    ]
                                ),
                                width={"size": 6, "order": 5},
                            ),
                            dbc.Col(
                                dbc.Row(
                                    [
                                        city_sectors_airbnb.display(),
                                        clustering_airbnb.display(),
                                        cost_per_sector.display(),
                                    ]
                                ),
                                width={"size": 6, "order": 5}
                            )
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