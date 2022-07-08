from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc

from components import navbar
from lib.crimes import crimes_city, indicators as crime_indicators, filters as crime_filters, datatable_crimes
from components.migrate.travel_reason import TravelReason
from components.migrate.travel_reason_month import TravelReasonMonth
from components.migrate.tourist_region import TouristRegion
from components.migrate.age_tourism import AgeTourism
from components.migrate.year_age import YearAge
from components.migrate import datatable




travel_reason = TravelReason('Travel Reason', 'id_travel_reason')
year_age = YearAge('Age Tourism', 'id_year_age')
travel_reason_month = TravelReasonMonth('Travel Reason Month', 'id_travel_reason_month')
tourist_region = TouristRegion('Tourist Region', 'id_tourist_region')
age_tourism = AgeTourism('Age Tourism', 'id_age_tourism')

migrate = html.Div([
    dbc.Row([
        dbc.Col([
            navbar.navbar,
            dbc.Row([

                dbc.Col([
                    dbc.Row(
                        [
                            tourist_region.display(),
                        ]
                    ),
                ],
                    width={"size": 3, "order": 1}),
                dbc.Col([
                    # dbc.Row(
                    #     [
                    #         dbc.Col(
                    #             crime_indicators.card_indicators,
                    #             width={"size": 3, "order": 5},
                    #         ),
                    #         dbc.Col(
                    #             crime_indicators.card_indicators,
                    #             width={"size": 3, "order": 5},
                    #         ),
                    #         dbc.Col(
                    #             crime_indicators.card_indicators,
                    #             width={"size": 3, "order": 5},
                    #         ),
                    #         dbc.Col(
                    #             crime_indicators.card_indicators,
                    #             width={"size": 2, "order": 5},
                    #         ),
                    #     ],
                    # ),
                    dbc.Row(
                        [
                            dbc.Col([
                                html.H4("TOURISM AND MIGRATION",
                                        style={"color": "#606060",
                                               "text-align": "center"}
                                        ),
                                html.Hr(style={"width": "calc(100% - 2em)",
                                                "height": "1px",
                                                "background-color": "#606060"}),
                            ],
                                width={"size": 11, "order": 5},
                                style={"margin": 20},
                            ),
                        ]),
                    dbc.Row(
                        [
                            dbc.Col(
                                travel_reason.display(),
                                width={"size": 6, "order": 5},
                            ),
                            dbc.Col(
                                age_tourism.display(),
                                width={"size": 5, "order": 5},
                            ),

                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                travel_reason_month.display(),
                                width={"size": 11, "order": 5},
                            ),

                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                datatable.migration_table,
                                width={"size": 11, "order": 5},
                            ),
                        ]
                    ),
                ],
                    width={"size": 9, "order": 2},
                    #style={'margin-left': '2px'}
                ),
            ]),
        ]),
    ]),
],
    style={'backgroundColor': '#fafafa'}
)