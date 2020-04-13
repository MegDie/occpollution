import occpollution

import webbrowser
import os, sys


occ_df = occpollution.Load_db().save_as_df()
occpollution.plot_interactive_map(occpollution.get_ozone(occ_df))

webbrowser.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "occpollution", "map_occitanie_day1.html"))
