from dir import DirOpt
import pandas as pd
import numpy as np

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()

class DataTreatment:
    def crimes_to_info(self):
        Base_delitos = pd.read_excel(f"{base_dir}/delitos.xlsx", sheet_name="Consolidadas", na_values=["N/A", "", 0])
        return Base_delitos