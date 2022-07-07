from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc

from components import navbar
from lib.crimes import crimes_city, indicators as crime_indicators, filters as crime_filters, datatable_crimes
from lib.hosting import hosting_city, datatable_hosting_city
from lib.general_choices import general_info, indicators as general_indicators

home = html.Div([
    dbc.Row([
        dbc.Col([
            navbar.navbar,
            dbc.Row(
                [
                    dbc.Col(
                        general_info.card_indicators_pie_plot,
                        width={"size": 3, "order": 5},
                    ),
                    dbc.Col(
                        general_indicators.card_indicators,
                        width={"size": 3, "order": 5},
                    ),
                    dbc.Col(
                        general_indicators.card_indicators,
                        width={"size": 3, "order": 5},
                    ),
                    dbc.Col(
                        general_indicators.card_indicators,
                        width={"size": 3, "order": 5},
                    ),
                ],
            ),
            dbc.Row(
                [
                    html.H2("TOURISM AND MIGRATION"),
                    html.Hr()
                ]),
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
                    dbc.Col(
                        general_info.card_statistics_line,
                        width={"size": 4, "order": 5},
                    ),
                    dbc.Col(
                        datatable_hosting_city.hosting_table,
                        width={"size": 4, "order": 5},
                    ),
                    dbc.Col(
                        general_info.card_statistics_violin,
                        width={"size": 4, "order": 5},
                    ),
                ]
            ),
        ]),
    ]),
],
    style={'backgroundColor': '#fafafa'}
)