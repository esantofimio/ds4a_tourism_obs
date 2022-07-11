from dash import html, dcc
from dir import DirOpt
from components.airbnb.data_treatment import DataTreatment
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.special import boxcox, inv_boxcox
from dash import Dash, html, dcc, Input, Output, callback, State

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()
data_treatment = DataTreatment()
Airbnb_clean = data_treatment.airbnb_info()

ALLOWED_FIELDS = (
    'ADR_USD_trans', 'labels_1', 'labels_2', 'labels_3',
    'Listing_Type_norm_Hotel_room', 'Listing_Type_norm_Private_room',
    'Listing Type_norm_Shared_room', 'Latitude', 'Longitude', 'Bedrooms',
    'Bathrooms', 'Max_Guests', 'Overall_Rating', 'Avg_Dist_C_Comerciales',
    'Avg_Dist_Vida_Nocturna_Gastronomia',
     'Avg_Dist_Obras_urbanisticas_historicas', 'Avg_Dist_Fiestas_Ferias',
     'Avg_Dist_Otros', 'Avg_Dist_Atractivos_Religiosos',
     'Avg_Dist_Parques_Urbanos_Ecologicos_Diversiones',
     'Avg_Dist_Museos_Centros_Culturales', 'Avg_Dist_Estacion',
     'Avg_Dist_Wifi', 'Avg_Dist_Delitos', 'No_Delitos',
     'Actractivo_Religiosos', 'Centros_Comerciales', 'Fiestas_Ferias',
     'Museos_Centros_Culturales', 'Obras_Urbanisticas_Historicas',
     'Otros', 'Parques Urbanos, Ecologicos_Diversiones',
     'Vida Nocturna y Gastronomia', 'No_Estaciones_Transmilenio',
     'No_SITP_Transmilenio', 'No_Wifi_Gratis', 'Month_Esp'
)

class PredictionModel:
    def __init__(self, title: str, ID: str):
        self.title = title
        self.id = ID

    def training(self):
        ADR_USD_trans, lambdat = stats.boxcox(Airbnb_clean['Average Daily Rate (USD) Def'])
        Airbnb_clean['ADR_USD_trans'] = ADR_USD_trans
        Airbnb_clean['Month_Esp'] = 0
        for i in range(len(Airbnb_clean)):
            if Airbnb_clean['Month'][i] in (1, 2, 3, 5, 8, 9, 10, 11):
                Airbnb_clean['Month_Esp'][i] = 0
            else:
                Airbnb_clean['Month_Esp'][i] = 1
        X = Airbnb_clean[['Latitude', 'Longitude']]
        kmeans = KMeans(n_clusters=4).fit(X)
        labels = kmeans.predict(X)
        Airbnb_clean['labels'] = labels
        Airbnb_clean['labels'] = Airbnb_clean['labels'].astype("category")
        Cat = pd.get_dummies(Airbnb_clean[['labels', 'Listing Type_norm']], columns=['labels', 'Listing Type_norm'],
                             drop_first=True)
        Airbnb_modelo = pd.concat([Airbnb_clean.iloc[:, 35], Cat, Airbnb_clean.iloc[:, 2:31], Airbnb_clean.iloc[:, 36]],
                                  axis=1)
        np.random.seed(100)
        ndata = len(Airbnb_modelo)
        idx_train = np.random.choice(range(ndata), int(0.8 * ndata), replace=False)
        idx_test = np.asarray(list(set(range(ndata)) - set(idx_train)))
        train = Airbnb_modelo.iloc[idx_train]  # the training data set
        test = Airbnb_modelo.iloc[idx_test]  # the test data set
        formula1 = '''ADR_USD_trans ~ labels_1+ labels_2+ labels_3+
                   Q('Listing Type_norm_Hotel room')+ Q('Listing Type_norm_Private room')+
                   Q('Listing Type_norm_Shared room')+ Latitude+ Longitude+
                   Bathrooms+ Q('Max Guests')+ Q('Overall Rating')+ Avg_Dist_C_Comerciales+
                   Avg_Dist_Vida_Nocturna_Gastronomia+
                   Avg_Dist_Obras_urbanisticas_historicas+
                   Avg_Dist_Otros+
                   Avg_Dist_Parques_Urbanos_Ecologicos_Diversiones+
                   Avg_Dist_Museos_Centros_Culturales+ Avg_Dist_Delitos+ Q('No.Delitos')+
                   Q('Actractivo Religiosos')+ Q('Centros Comerciales')+
                   Q('Museos y Centros Culturales')+ Q('Obras Urbanisticas e Historicas')+
                   Otros+ Q('Parques Urbanos, Ecologicos y Diversiones')+
                   Q('Vida Nocturna y Gastronomia')+
                   Q('No.SITP Transmilenio')+Month_Esp
            '''
        model1 = smf.ols(formula=formula1, data=train).fit()
        model1.save(f'{base_dir}/model')

    @staticmethod
    def get_prediction(vals):
        print(vals)
        ADR_USD_trans, lambdat = stats.boxcox(Airbnb_clean['Average Daily Rate (USD) Def'])
        Airbnb_clean['ADR_USD_trans'] = ADR_USD_trans
        Airbnb_clean['Month_Esp'] = 0
        for i in range(len(Airbnb_clean)):
            if Airbnb_clean['Month'][i] in (1, 2, 3, 5, 8, 9, 10, 11):
                Airbnb_clean['Month_Esp'][i] = 0
            else:
                Airbnb_clean['Month_Esp'][i] = 1
        X = Airbnb_clean[['Latitude', 'Longitude']]
        kmeans = KMeans(n_clusters=4).fit(X)
        labels = kmeans.predict(X)
        Airbnb_clean['labels'] = labels
        Airbnb_clean['labels'] = Airbnb_clean['labels'].astype("category")
        Cat = pd.get_dummies(Airbnb_clean[['labels', 'Listing Type_norm']], columns=['labels', 'Listing Type_norm'],
                             drop_first=True)
        Airbnb_modelo = pd.concat([Airbnb_clean.iloc[:, 35], Cat, Airbnb_clean.iloc[:, 2:31], Airbnb_clean.iloc[:, 36]],
                                  axis=1)
        np.random.seed(100)
        ndata = len(Airbnb_modelo)
        idx_train = np.random.choice(range(ndata), int(0.8 * ndata), replace=False)
        train = Airbnb_modelo.iloc[idx_train]
        ADR_USD_trans, lambdat = stats.boxcox(Airbnb_clean['Average Daily Rate (USD) Def'])
        model1 = sm.load(f'{base_dir}/model')


        if None not in vals and len(vals) > 1:
            train.loc[0] = vals
        print(f'example {train.loc[0]}')
        Y_orig_pred_train = inv_boxcox(model1.predict(train.loc[0]), lambdat)
        print(f'result {Y_orig_pred_train}')
        return Y_orig_pred_train

    def display(self):

        layout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        html.H6("Predict airbnb price"),
                        html.Div([
                            dcc.Input(
                                id="input_{}".format(_), type='text',
                                placeholder="{}".format(_),
                                style={"width": "80%",
                                       "margin": "5px"}
                            )
                            for _ in ALLOWED_FIELDS
                        ]),
                        html.Br(),
                        html.Div(id='my-output'),
                        dbc.Button([
                            'Submit',
                        ],
                        id='id_submit')
                    ]
                ),
            ],
            style={"width": "100%",  "margin": 20, "height": "auto", },
        )

        @callback(
            Output(component_id='my-output', component_property='children'),
            [State("input_{}".format(_), "value") for _ in ALLOWED_FIELDS],
            Input(component_id='id_submit', component_property='n_clicks')
        )
        def update_output_div(*vals):
            vals = vals[:-1]
            features = []
            if None not in vals:
                for i in vals:
                    features.append(float(i))
                print(f'example {features}')
            try:
                return f'This airbnb would cost: {self.get_prediction(features)[0]:.3g} dollars'
            except Exception as e:
                print(e)
                return ''
            #
        return layout

    # ADR_USD_trans
    # 2.236500
    # labels_1
    # 1.000000
    # labels_2
    # 0.000000
    # labels_3
    # 0.000000
    # Listing
    # Type_norm_Hotel
    # room
    # 0.000000
    # Listing
    # Type_norm_Private
    # room
    # 0.000000
    # Listing
    # Type_norm_Shared
    # room
    # 0.000000
    # Latitude
    # 4.663090
    # Longitude - 74.054590
    # Bedrooms
    # 4.000000
    # Bathrooms
    # 3.000000
    # Max
    # Guests
    # 5.000000
    # Overall
    # Rating
    # 0.000000
    # Avg_Dist_C_Comerciales
    # 0.051228
    # Avg_Dist_Vida_Nocturna_Gastronomia
    # 0.058387
    # Avg_Dist_Obras_urbanisticas_historicas
    # 0.058777
    # Avg_Dist_Fiestas_Ferias
    # 0.042693
    # Avg_Dist_Otros
    # 0.070924
    # Avg_Dist_Atractivos_Religiosos
    # 0.060088
    # Avg_Dist_Parques_Urbanos_Ecologicos_Diversiones
    # 0.081904
    # Avg_Dist_Museos_Centros_Culturales
    # 0.060758
    # Avg_Dist_Estacion
    # 0.068557
    # Avg_Dist_Wifi
    # 0.072733
    # Avg_Dist_Delitos
    # 0.057526
    # No.Delitos
    # 193.000000
    # Actractivo
    # Religiosos
    # 8.000000
    # Centros
    # Comerciales
    # 7.000000
    # Fiestas
    # y
    # Ferias
    # 3.000000
    # Museos
    # y
    # Centros
    # Culturales
    # 7.000000
    # Obras
    # Urbanisticas
    # e
    # Historicas
    # 8.000000
    # Otros
    # 6.000000
    # Parques
    # Urbanos, Ecologicos
    # y
    # Diversiones
    # 13.000000
    # Vida
    # Nocturna
    # y
    # Gastronomia
    # 4.000000
    # No.Estaciones
    # Transmilenio
    # 13.000000
    # No.SITP
    # Transmilenio
    # 509.000000
    # No.Wifi
    # Gratis
    # 20.000000
    # Month_Esp
    # 0.000000

