from dash import Dash, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from collections import OrderedDict

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

df = pd.DataFrame(data)

def generate_table(df, max_rows=10):
    return dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['Date', 'Region']
        ],

        style_as_list_view=True
    )


app = Dash(__name__)

crimes_table = dbc.Card(
    children=[
        dbc.CardBody(
            [
                html.H4(children='US Agriculture Exports (2011)', style={"padding": "1rem"}),
                generate_table(df)
            ]
        )],
        style={"width": "100%",  "margin": 20, "height": "auto", "padding": "1rem"},
    )