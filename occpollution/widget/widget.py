import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact 

def plot_widget(occ, month, station_1='Montpellier Nord - Périurbain', 
station_2='Lourdes-Lapaca Urbain', station_3='Toulouse-Berthelot Urbain'):

    stations = station_1, station_2, station_3
    df_station = occ[occ['nom_station'].isin(stations)]
    df_station = df_station[df_station['nom_poll'] == 'O3']
    df_station = df_station[df_station.date == month]
    df_station = df_station[['nom_com', 'nom_station', 'valeur', 'date']]

    plt.style.use('Solarize_Light2')
    sns.catplot(x = 'nom_com', y = 'valeur', 
            data = df_station,
            height = 3, aspect = 2,
            kind = 'violin')
    plt.tight_layout()
    plt.xlabel('Cities')
    plt.ylabel('O3')
    plt.title("Comparison of ozone measurements over a month from 3 cities")
    plt.show()

    interact(plot_widget, station_1=occ.nom_station.unique(), 
         station_2=occ.nom_station.unique(), 
         station_3=occ.nom_station.unique(), 
         month=occ.date.unique())    

