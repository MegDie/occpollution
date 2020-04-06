import pandas as pd
import numpy as numpy

def get_ozone(df_occ):
    occ = df_occ
    occ['date'] = pd.to_datetime(occ['date_debut']).dt.to_period('M')
    occ = occ[occ['nom_poll'] == 'O3'] 
    return occ
    



