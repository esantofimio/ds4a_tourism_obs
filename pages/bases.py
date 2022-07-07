from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc

from components import navbar
from lib.crimes import crimes_city, indicators as crime_indicators, filters as crime_filters, datatable_crimes
from lib.hosting import hosting_city, datatable_hosting_city
from lib.general_choices import general_info, indicators as general_indicators

bases = html.Div([
    dbc.Row([
        dbc.Col([
            navbar.navbar,
            dbc.Row([
                dbc.Col(
                    crime_filters.filters,
                    width={"size": 3, "order": 1},
                ),
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
                                crimes_city.card_map,
                                width={"size": 4, "order": 5},
                            ),
                            dbc.Col(
                                hosting_city.card_map,
                                width={"size": 8, "order": 5},
                            ),
                        ]
                    ),
                    dbc.Row(
                        [
                            datatable_crimes.crimes_table
                        ]
                    ),
                ],
                width={"size": 9, "order": 2}),
            ]),
        ]),
    ]),
],
    style={'backgroundColor': '#fafafa'}
)