import selenium
from selenium import webdriver
import time
import folium
import branca.colormap as cm
import pandas as pd
import matplotlib.pyplot as plt

import occpollution
from occpollution.io import url_db, path_target
from occpollution.preprocess.get_pollution import get_ozone_day


def map_day(occ_df, jour):
    
    occ_map = occ_df[occ_df['date'] == jour]

    map_int4 = folium.Map(location = [43, 2.5], 
                         zoom_start = 9.5, 
                         tiles = 'Stamen Terrain')
 
    for i in range(0, len(occ_map)):
        folium.Circle(
            location = [occ_map.iloc[i]['Y'], occ_map.iloc[i]['X']],
            popup = occ_map.iloc[i]['nom_station'],
            radius = 10000,
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
        map_day(occ_df, list_day[image_nb]).save('.//html/map_' + str(image_nb) + '.html') # save each map.html in the html folder
        driver.set_window_size(4000, 3000)  # choose a resolution
        driver.get('file:///C:/Users/megan/MIND/HMMA238/occpollution/report/html/map_' + str(image_nb)+ '.html')
        time.sleep(1)
        driver.save_screenshot("gifs/folium_%s.png" % str(image_nb).zfill(3))
        plt.close('all')     







