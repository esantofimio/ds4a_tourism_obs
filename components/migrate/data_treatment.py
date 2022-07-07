from dir import DirOpt
import pandas as pd
import numpy as np

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()

class DataTreatment:
    def migration_to_info(self):
        df = pd.read_csv(f"{base_dir}/colombia_migration_2021.csv", delimiter=';')
        motivos = df.groupby('Motivo Viaje')['Fac Exp'].sum().to_frame().sort_values(by=['Fac Exp'], ascending=False) \
            .reset_index().head(10)

        # 1. Ajustar Motivo Viaje, para agrupar los motivos que son menos recurrentes
        df['Reason for trip'] = np.select(condlist=[df['Motivo Viaje'] == motivos.iloc[0, 0],
                                                    df['Motivo Viaje'] == motivos.iloc[1, 0],
                                                    df['Motivo Viaje'] == motivos.iloc[2, 0],
                                                    df['Motivo Viaje'] == motivos.iloc[3, 0],
                                                    df['Motivo Viaje'] == motivos.iloc[4, 0],
                                                    df['Motivo Viaje'] == motivos.iloc[5, 0],
                                                    df['Motivo Viaje'] == motivos.iloc[6, 0],
                                                    df['Motivo Viaje'] == motivos.iloc[7, 0],
                                                    df['Motivo Viaje'] == motivos.iloc[8, 0],
                                                    df['Motivo Viaje'] == motivos.iloc[9, 0]
                                                    ]
                                          , choicelist=[motivos.iloc[0, 0],
                                                        motivos.iloc[1, 0],
                                                        motivos.iloc[2, 0],
                                                        motivos.iloc[3, 0],
                                                        motivos.iloc[4, 0],
                                                        motivos.iloc[5, 0],
                                                        motivos.iloc[6, 0],
                                                        motivos.iloc[7, 0],
                                                        motivos.iloc[8, 0],
                                                        motivos.iloc[9, 0]
                                                        ],
                                          default='Others')

        dictionary = {'Turismo': 'Tourism', 'Negocios': 'Business', 'Tránsito': 'Transit', 'Tripulación': 'Crew',
                      'Trabajo': 'Work', 'Eventos': 'Events', 'Residente': 'Resident', 'Estudios': 'Studies',
                      'Inadmisión': 'Inadmissibility', 'Tratamiento Médico': 'Medical treatment',
                      'Capacitación': 'Training', 'Cortesía': 'Courtesy'}

        df['Reason for trip'] = df['Reason for trip'].replace(dictionary)
        return df