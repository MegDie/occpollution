import numpy as np
from numpy import array
import pandas as pd
import folium
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import branca.colormap as cm

from occpollution.preprocess.get_pollution import color_scale

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
    occ_2018 = occ_df[occ_df['date'] == '2018']
    
    linear = color_scale(occ_2018)
    
    map = folium.Map(location=[43.9333, 2.15], 
                 zoom_start=7.5, 
                 tiles='Stamen Terrain')
                 
    for i in range(0,len(occ_2018)):
        folium.Circle(
            location=[occ_2018.iloc[i]['Y'], occ_2018.iloc[i]['X']],
            popup=occ_2018.iloc[i]['nom_station'],
            radius=occ_2018.iloc[i]['valeur']*100,
            color='black',
            fill=True,
            fill_color=linear(occ_2018.iloc[i]['standard']),
            fill_opacity=0.5,
            opacity=0.4,
            ).add_to(map)
    
    map.save('map_occitanie2018.html')

    return (map)