# Basics Requirements
import pathlib
import os
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

# Data
import json
from datetime import datetime as dt

navbar = html.Div(
    [
        dbc.Navbar(
            dbc.Container([
                dbc.NavbarBrand("Team 186", href="#", style={'color': 'rgb(31, 120, 180)'}),

                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(dcc.Link('Migrate',
                                                 href='/migrate_page',
                                                 style={'color': 'rgb(31, 120, 180)',
                                                        'text-decoration': 'none',
                                                        'margin-left': '8px'}
                                                 )),
                            dbc.NavItem(dcc.Link('Crimes',
                                                 href='/crimes_page',
                                                 style={'color': 'rgb(31, 120, 180)',
                                                        'text-decoration': 'none',
                                                        'margin-left': '8px'}
                                                 )),
                            dbc.NavItem(dcc.Link('Hosting',
                                                 href='/hosting_page',
                                                 style={'color': 'rgb(31, 120, 180)',
                                                        'text-decoration': 'none',
                                                        'margin-left': '8px'}
                                                 )),
                            dbc.NavItem(dcc.Link('Price Airbnb',
                                                 href='/pricing_airbnb',
                                                 style={'color': 'rgb(31, 120, 180)',
                                                        'text-decoration': 'none',
                                                        'margin-left': '8px'}
                                                 )),
                        ], className="ml-auto", navbar=True
                    ),
                    id="navbar-collapse1",
                    navbar=True,
                ),
            ],
                style={'padding-bottom': '12px', 'padding-top': '12px'}
            ),
            color="#F9F9F9",
            dark=True,
            sticky="top",
            style={'box-shadow': "0px 1px 3px rgb(0 0 0 / 12%), 0px 1px 2px rgb(0 0 0 / 24%)"}
        )
    ]
)
