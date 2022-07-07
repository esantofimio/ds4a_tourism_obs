from dir import DirOpt
import pandas as pd
import numpy as np

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()

class DataTreatment:
    def airbnb_info(self):
        Airbnb = pd.read_csv(f"{base_dir}/airbnb.csv", encoding = 'utf-8')
        Airbnb_clean = Airbnb[['Last Scraped Date', 'Average Daily Rate (USD) Def', 'Latitude', 'Longitude', 'Bedrooms',
                               'Bathrooms', 'Max Guests', 'Overall Rating', 'Avg_Dist_C_Comerciales',
                               'Avg_Dist_Vida_Nocturna_Gastronomia',
                               'Avg_Dist_Obras_urbanisticas_historicas', 'Avg_Dist_Fiestas_Ferias', 'Avg_Dist_Otros',
                               'Avg_Dist_Atractivos_Religiosos',
                               'Avg_Dist_Parques_Urbanos_Ecologicos_Diversiones', 'Avg_Dist_Museos_Centros_Culturales',
                               'Avg_Dist_Estacion',
                               'Avg_Dist_Wifi', 'Avg_Dist_Delitos', 'No.Delitos', 'Actractivo Religiosos',
                               'Centros Comerciales',
                               'Fiestas y Ferias', 'Museos y Centros Culturales', 'Obras Urbanisticas e Historicas',
                               'Otros',
                               'Parques Urbanos, Ecologicos y Diversiones', 'Vida Nocturna y Gastronomia',
                               'No.Estaciones Transmilenio',
                               'No.SITP Transmilenio', 'No.Wifi Gratis', 'Localidad', 'Listing Type_norm']]
        Airbnb_clean['Last Scraped Date'] = pd.to_datetime(Airbnb_clean['Last Scraped Date'], format="%Y-%m-%d")
        Airbnb_clean['Year-Month'] = Airbnb_clean['Last Scraped Date'].dt.year.astype(str) + '-' + Airbnb_clean[
            'Last Scraped Date'].dt.month.astype(str)
        Airbnb_clean['Month'] = Airbnb_clean['Last Scraped Date'].dt.month
        return Airbnb_clean