import selenium
from selenium import webdriver
import time
import folium
from folium.features import DivIcon
import branca.colormap as cm
import pandas as pd
import matplotlib.pyplot as plt
import imageio
import os

import occpollution
from occpollution.io import url_db, path_target
from occpollution.preprocess.get_pollution import get_ozone_day
from occpollution.preprocess.get_pollution import color_scale


def map_day(occ_df, jour):

    linear = color_scale(occ_df)
    occ_map = occ_df[occ_df['date'] == jour]
    
    map_int4 = folium.Map(location = [43.8, 2.5], 
                         zoom_start = 7.5, 
                         tiles = 'Stamen Terrain')
 
    for i in range(0, len(occ_map)):

        text = str(occ_map.date.iloc[1])

        folium.Circle(
            location = [occ_map.iloc[i]['Y'], occ_map.iloc[i]['X']],
            popup = occ_map.iloc[i]['nom_station'],
            radius = 300 * occ_map.iloc[i]['valeur'],
            color = 'black',
            fill = True,
            fill_color = linear(occ_map.iloc[i]['standard']),
            fill_opacity = 0.5,
            opacity = 0.4,
        ).add_to(map_int4)

        folium.map.Marker(
             [44.8, 3.8],
             icon=DivIcon(
                 icon_size=(200,100),
                 icon_anchor=(0,0),
                 html='<div style="font-size: 24pt">' + text + '</div>',
                 )
        ).add_to(map_int4)
    
    return(map_int4)


def map_iteration(occ_df):

    driver = selenium.webdriver.Chrome()
    list_day = occ_df.date.unique()

    path_html = os.getcwd() + '\\map_html'
    path_png = os.getcwd() + '\\map_png'

    if not os.path.exists(path_html):
        os.makedirs(path_html)
        
    if not os.path.exists(path_png):
        os.makedirs(path_png)

    for image_nb in range(len(list_day)):
        map_day(occ_df, list_day[image_nb]).save('.//map_html/map_' + str(image_nb) + '.html') # save each map.html in the html folder
        driver.set_window_size(1000, 1000)  # choose a resolution
        path_to_get = os.getcwd() + '\\map_html\\map_' + str(image_nb)+ '.html'
        driver.get(path_to_get)
        time.sleep(1)
        driver.save_screenshot("map_png/folium_%s.png" % str(image_nb).zfill(3))
        plt.close('all')     


def animation():
    png_dir = 'map_png'
    images = []
    for file_name in os.listdir(png_dir):
        if file_name.endswith('.png'):
            print(file_name)
            file_path = os.path.join(png_dir, file_name)
            images.append(imageio.imread(file_path))
    imageio.mimsave('animation.gif', images, fps=30)


