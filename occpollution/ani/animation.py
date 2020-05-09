import imgkit
import branca.colormap as cm

from occpollution.io import url_db, path_target
from occpollution.preprocess.get_pollution import get_ozone_day


occ_j =   

linear4 = cm.LinearColormap(
    ['green', 'yellow', 'red'],
    vmin=min(occ_j['standard']), vmax=max(occ_j['standard'])
)

def map_video(jour):
    
    occ_map = occ_j[occ_j['day'] == jour]
    

    map_int4 = folium.Map(location = [43, 2.5], 
                         zoom_start = 7.5, 
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








