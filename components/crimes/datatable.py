from dash import Dash, html, dash_table
import dash_bootstrap_components as dbc
from dir import DirOpt
from components.crimes.data_treatment import DataTreatment
import pandas as pd
from collections import OrderedDict

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
Base_delitos = data_treatment.crimes_to_info()

df = Base_delitos["PAIS_PERSONA"].value_counts(normalize=True)\
    .reset_index().sort_values(by="PAIS_PERSONA", ascending=False).head(10)

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
                html.H4(children='Crimes per nationality ', style={"padding": "1rem"}),
                generate_table(df)
            ]
        )],
        style={"width": "100%",  "margin": 20, "height": "auto", "padding": "1rem"},
    )