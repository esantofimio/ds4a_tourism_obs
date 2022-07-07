from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc

from components import navbar
from lib.crimes import crimes_city, indicators as crime_indicators, filters as crime_filters, datatable_crimes
from components.crimes.per_age_victim import AgeVictim
from components.crimes.time_day import TimeDay
from components.crimes.gender_victims import GenderVictims
from components.crimes.per_nationality import CrimeNationality
from components.crimes.per_neighbourhood import Neighbourhood
from components.crimes.per_hour import Hour
from components.crimes import filters as migrate_filters
from components.crimes import datatable



age_victim = AgeVictim('Age Victims', 'id_age_victim')
time_day = TimeDay('Time day', 'id_time_day')
gender_victims = GenderVictims('Gender Victims', 'id_gender_victims')
per_neighbourhood = Neighbourhood('Neighbourhood', 'id_neighbourhood')
per_hour = Hour('Hour', 'id_hour')
per_nationality = CrimeNationality('Nationality', 'id_nationality')

crimes = html.Div([
    dbc.Row([
        dbc.Col([
            navbar.navbar,
            dbc.Row([

                dbc.Col([
                    dbc.Row(
                        [
                            migrate_filters.filters,
                        ],
                    ),
                    dbc.Row(
                        [
                            gender_victims.display(),
                        ]
                    ),
                ],
                    width={"size": 3, "order": 1}),
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
                                width={"size": 2, "order": 5},
                            ),
                        ],
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                per_neighbourhood.display(),
                                width={"size": 6, "order": 5},
                            ),
                            dbc.Col([
                                dbc.Row(
                                    [
                                        datatable.crimes_table,
                                        per_nationality.display()

                                    ]
                                )],
                                width={"size": 5, "order": 5}
                            ),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                per_hour.display(),
                                width={"size": 11, "order": 5},
                            ),

                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                age_victim.display(),
                                width={"size": 11, "order": 5},
                            ),

                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                time_day.display(),
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