import occpollution
from occpollution.io import path_target
from occpollution.ani.animation import map_iteration
from occpollution.ani.animation import animation

import pandas as pd

import webbrowser
import os, sys

# The following lines create a video of the ozone evolution in Occitanie during the last year

occ_j = pd.read_csv(path_target) # import data
occ_j = occpollution.get_ozone_day(occ_j) # treatment of data
map_iteration(occ_j)
animation()

papapath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"animation.gif")
os.system("chrome "+papapath)

