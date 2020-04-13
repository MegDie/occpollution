import pandas as pd
import numpy as numpy

def get_ozone(occ_df):
    occ_df['date'] = pd.to_datetime(occ_df['date_debut']).dt.to_period('M')
    occ_df = occ_df[occ_df['nom_poll'] == 'O3'] 
    return occ_df
    



