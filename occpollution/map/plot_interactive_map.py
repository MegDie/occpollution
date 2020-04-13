import numpy as np
from numpy import array
import pandas as pd
import folium
import branca.colormap as cm
from download import download

import occpollution
from occpollution.io import url_db, path_target

def plot_interactive_map(occ_df):
    occ_df = occpollution.Load_db().save_as_df()
    occ_df = occ_df[occ_df['nom_poll'] == 'O3']
    occ_df['jour'] = pd.to_datetime(occ_df['date_debut']).dt.to_period('D')
    occ_df['centrer_reduire'] = (occ_df[['valeur']] - np.mean(occ_df[['valeur']]))/ np.std(occ_df[['valeur']])
    
    occ_day1 = occ_df[occ_df['jour'] == '2020-03-26']
    
    linear = cm.LinearColormap(
    ['green', 'yellow', 'red'],
    vmin=-3, vmax=1)
    
    map = folium.Map(location=[43.9333, 2.15], 
                 zoom_start=7.5, 
                 tiles='Stamen Terrain')
                 
    for i in range(0,len(occ_day1)):
        folium.Circle(
            location=[occ_day1.iloc[i]['Y'], occ_day1.iloc[i]['X']],
            popup=occ_day1.iloc[i]['nom_station'],
            radius=occ_day1.iloc[i]['valeur']*100,
            color='black',
            fill=True,
            fill_color=linear(occ_day1.iloc[i]['centrer_reduire']),
            fill_opacity=0.5,
            opacity=0.4,
            ).add_to(map)
    
    map.save('map_occitanie_day1.html')

    return (map)




