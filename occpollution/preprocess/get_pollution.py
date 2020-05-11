import pandas as pd
import numpy as np

def get_ozone_an(occ_df):
    occ_df['date'] = pd.to_datetime(occ_df['date_debut']).dt.to_period('Y')
    occ_df = occ_df[occ_df['nom_poll'] == 'O3'] 
    occ_df['standard'] = (occ_df[['valeur']] - np.mean(occ_df[['valeur']]))/ np.std(occ_df[['valeur']])
    return occ_df

def get_ozone_day(occ_df):
    occ_df['date'] = pd.to_datetime(occ_df['date_debut']).dt.to_period('D')
    occ_df = occ_df[occ_df['nom_poll'] == 'O3'] 
    occ_df['standard'] = (occ_df[['valeur']] - np.mean(occ_df[['valeur']]))/ np.std(occ_df[['valeur']])
    return occ_df


    



