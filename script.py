import occpollution
import occpollution.map

import webbrowser
import os, sys


occ_df = occpollution.Load_db().save_as_df()
occpollution.map.plot_interactive_map(occ_df)


webbrowser.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "occpollution", "map", "map_occitanie.html"))
webbrowser.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "occpollution", "map", "map_occitanie_day1.html"))
