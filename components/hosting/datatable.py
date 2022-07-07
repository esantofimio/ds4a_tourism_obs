from dash import Dash, html, dash_table
from dir import DirOpt
import dash_bootstrap_components as dbc
import pandas as pd


dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
hosting_spots = pd.read_excel(f'{base_dir}/hosting.xlsx')

df = hosting_spots[['CATEGORIA', 'LOCALIDAD']]
df = df[:200]


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

        style_as_list_view=True,
        page_size=15
    )


app = Dash(__name__)

hosting_table = dbc.Card(
    children=[
        dbc.CardBody(
            [
                html.H4(children='Hosting places', style={"padding": "1rem"}),
                generate_table(df)
            ]
        )],
        style={"width": "100%",  "margin": 20, "height": "auto", "padding": "1rem"},
    )