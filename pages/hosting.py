from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc

from components import navbar
from lib.crimes import crimes_city, indicators as crime_indicators
from components.hosting.hosting_zones import HostingZones
from components.hosting.gastro_zones import GastroZones
from components.hosting.touristic_atractions import TouristicAtractions
from components.hosting.hosting_per_sector import HostingPerSecond
from components.hosting import datatable



gastro_zones = GastroZones('Gastro zones', 'id_gastro_zones')
hosting_zones = HostingZones('Hosting zones', 'id_hosting_zones')
touristic_atractions = TouristicAtractions('Touristic zones', 'id_touristic')
hosting_per_sector = HostingPerSecond('Hosting per sector', 'id_hosting_per_sector')

hosting = html.Div([
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
                                        hosting_zones.display()
                                    ]
                                ),
                                width={"size": 6, "order": 5}
                            ),
                            dbc.Col([
                                dbc.Row(
                                    [
                                        datatable.hosting_table,
                                        hosting_per_sector.display()
                                    ])
                            ],
                                width={"size": 6, "order": 5}
                            )
                        ]
                    ),
                ],
                    width={"size": 12, "order": 2},
                    #style={'margin-left': '2px'}
                ),
            ]),
        ]),
    ]),
],
    style={'backgroundColor': '#fafafa'}
)