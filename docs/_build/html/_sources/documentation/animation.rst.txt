Animation
===========================

The ultimate goal for this project is to make a video of the O3 (ozone) level across time for the cities available in the dataset.
Still using the `folium` package, we plot all the required map to build our animation (a gif file).

Step 1: Plot all the required maps
------------------------------------

In order to edit our video, we first need to get all maps of the period we study: 2019, 29 April to 2020, 24 April (refer to Input/Output section to know why).
The following function do mostly the same as the `plot_interactive_map` function (refer to Occitanie map section).
It's import to specify that we use the `color_scale` function (refer to preprocess section) before choosing the day to have a global scale depending on the degree of ozone pollution.  
The difference is that we print the date on each map to locate in time during the video.

.. code-block:: python
   
   def map_day(occ_df, jour):
    
    # color scale
    linear = color_scale(occ_df)

    # choice of the day
    occ_map = occ_df[occ_df['date'] == jour]
    
    # initialization of the map
    map_int4 = folium.Map(location = [43.8, 2.5], 
                         zoom_start = 7.5, 
                         tiles = 'Stamen Terrain')
 
    for i in range(0, len(occ_map)):

        # storage of the date to print it on the map
        date = str(occ_map.day.iloc[1])

        # same as the plot_interactive_map function
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

        # date specified on the map
        folium.map.Marker(
             [44.8, 3.8],
             icon=DivIcon(
                 icon_size=(200,100),
                 icon_anchor=(0,0),
                 html='<div style="font-size: 24pt">' + date + '</div>',
                 )
        ).add_to(map_int4)
    
    return(map_int4)

Step 2: Convert each html map into a png file
------------------------------------------------

.. code-block:: python

   def map_iteration(occ_df):

    driver = selenium.webdriver.Chrome()
    list_day = occ_df.day.unique()

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

Step 3: Editing of the video 
----------------------------

.. code-block:: python

   def animation():
    png_dir = 'map_png'
    images = []
    for file_name in os.listdir(png_dir):
        if file_name.endswith('.png'):
            print(file_name)
            file_path = os.path.join(png_dir, file_name)
            images.append(imageio.imread(file_path))
    imageio.mimsave('animation.gif', images, fps=30)
