from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from pages.home import home
from pages.migrate import migrate
from pages.crimes import crimes
from pages.hosting import hosting
from pages.pricing_airbnb import pricing_airbnb
from pages.bases import bases
from flask import Flask


###########################################################
#
#           APP LAYOUT:
#
###########################################################
server = Flask(__name__)
app = Dash(__name__, external_stylesheets=[dbc.themes.YETI], server=server, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
    ],
)

index_page = html.Div([
    home
],
    style={'backgroundColor': '#F9F9F9'}
)

migrate_page = html.Div([
    migrate
],
    style={'backgroundColor': '#e2e2e2'}
)

hosting_page = html.Div([
    hosting
],
    style={'backgroundColor': '#F9F9F9'}
)

pricing_airbnb = html.Div([
    pricing_airbnb
],
    style={'backgroundColor': '#F9F9F9'}
)


crimes_page = html.Div([
    crimes
],
    style={'backgroundColor': '#F9F9F9'}
)

bases_page = html.Div([
    bases
],
    style={'backgroundColor': '#F9F9F9'}
)


@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/index_page':
        return index_page
    elif pathname == '/crimes_page':
        return crimes_page
    elif pathname == '/migrate_page':
        return migrate_page
    elif pathname == '/hosting_page':
        return hosting_page
    elif pathname == '/pricing_airbnb':
        return pricing_airbnb
    elif pathname == '/bases_page':
        return bases_page
    else:
        return crimes_page
    # You could also return a 404 "URL not found" page here

if __name__ == '__main__':
    app.run_server()

