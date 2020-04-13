import numpy as np
from numpy import array
import pandas as pd
import folium
import branca.colormap as cm
from download import download

def plot_interactive_map(occ_df):
    r"""
  The plot_interactive_map function plots the data.

  Input
  -----
    occ_df: Pandas data frame. 

  Output
  ------
    A folium map

  Example
  -------

  >> import occpollution
  >> occpollution.map.plot_interactive_map(df)

  """
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




