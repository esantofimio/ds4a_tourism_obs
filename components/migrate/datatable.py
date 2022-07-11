from dash import Dash, html, dash_table
import dash_bootstrap_components as dbc
from dir import DirOpt
from components.migrate.data_treatment import DataTreatment
import pandas as pd
from collections import OrderedDict

data_treatment = DataTreatment()
df = data_treatment.migration_to_info()

x = df.groupby('Motivo Viaje')['Fac Exp'].sum().to_frame().reset_index().sort_values(by=['Fac Exp'],
                                                                                     ascending=False)
y = df.groupby('Reason for trip')['Fac Exp'].sum().to_frame().reset_index().sort_values(by=['Fac Exp'],
                                                                                        ascending=False)
z = pd.merge(x, y, left_on='Motivo Viaje', right_on='Reason for trip', how='outer')
valida = (z.loc[z['Reason for trip'] != 'Otros', 'Fac Exp_x'] - z.loc[
    z['Reason for trip'] != 'Otros', 'Fac Exp_y']).sum()
valida1 = df['Reason for trip'].value_counts().to_frame().reset_index()['Reason for trip'].sum()
if (valida == 0) & (valida1 - df.shape[0] == 0):
    print("Ranking OK\n")
else:
    print("Ranking Wrong\n")

# Creamos el df para graficar
df_graph = df.groupby(['Año', 'Reason for trip'])['Fac Exp'].sum().to_frame() \
    .sort_values(by=['Fac Exp'], ascending=False).reset_index()
# ordenamos el df
df_graph = df_graph.sort_values(by=['Año', 'Reason for trip'], ascending=[True, True])
# renombramos columnas
df_graph = df_graph.rename(columns={'Fac Exp': 'Number of travelers', 'Año': 'Year'})



def generate_table(df_graph, max_rows=10):
    return dash_table.DataTable(
        data=df_graph.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_graph.columns],
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

migration_table = dbc.Card(
    children=[
        dbc.CardBody(
            [
                html.H4(children='2021 Travels Reasons ', style={"padding": "1rem"}),
                generate_table(df_graph)
            ]
        )],
        style={"width": "100%",  "margin": 20, "height": "auto", "padding": "1rem"},
    )