import selenium
from selenium import webdriver
import time
import folium
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
    
    map_int4 = folium.Map(location = [44, 2.5], 
                         zoom_start = 8, 
                         tiles = 'Stamen Terrain')
 
    for i in range(0, len(occ_map)):
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
    
    return(map_int4)


def map_iteration(occ_df):

    driver = selenium.webdriver.Firefox()
    list_day = occ_df.day.unique()

    for image_nb in range(len(list_day)):
        map_day(occ_df, list_day[image_nb]).save('.//map_html/map_' + str(image_nb) + '.html') # save each map.html in the html folder
        driver.set_window_size(1000, 1000)  # choose a resolution
        driver.get('file:///C:/Users/megan/MIND/HMMA238/occpollution/map_html/map_' + str(image_nb)+ '.html')
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
    imageio.mimsave('animation.gif', images, fps=50)


