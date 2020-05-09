import occpollution

import webbrowser
import os, sys


occ_df = occpollution.Load_db().save_as_df()
occpollution.plot_interactive_map(occpollution.get_ozone_an(occ_df))

papath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"map_occitanie2018.html")
os.system("chrome "+papath)