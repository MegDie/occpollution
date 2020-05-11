import occpollution
from occpollution.io import path_target
from occpollution.preprocess.get_pollution import color_scale
from occpollution.ani.animation import map_iteration 

import pandas as pd

import webbrowser
import os, sys


# The following lines open an interactive map of 2018 ozone's data in Occitanie

occ_df = occpollution.Load_db().save_as_df()
occpollution.plot_interactive_map(occpollution.get_ozone_an(occ_df))

papath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"map_occitanie2018.html")
os.system("chrome "+papath)

# The following lines create a video of the ozone evolution in Occitanie during the last year

occ_j = pd.read_csv(path_target) # import data
occ_j = occpollution.get_ozone_day(occ_j) # treatment of data
linear = color_scale(occ_j) # color scale for the circles

map_iteration(occ_j)
