Animation
===========================

The ultimate goal for this project is to make a video of the O3 (ozone) level across time for the cities available in the dataset.
Still using the `folium` package, we plot all the required map to build our animation (a gif file).

Step 1: Plot all the required maps
------------------------------------

In order to edit our video, we first need to get all maps of the period we study: 2019, 29 April to 2020, 24 April (refer to Input/Output section to know why).
The following function do mostly the same as the `plot_interactive_map` function (refer to Occitanie map section).
It's import to specify that we use the `color_scale` function (refer to preprocess section) before choosing the day to have a global scale: the highest and lowest measurement are calculated on the entire dataset and not only on one day, so we can properly see the difference of pollution between days and cities, and not only between cities.  
The difference between `map_day` function and `plot_interactive_map` function is that we print the date on each map to locate in time during the video.

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

We use the previous function in the following one: the goal here is to transform all the html map we get into png files so we can edit an animation.

`Selenium` (refer to installation section) allows us to interact with the web using chromedriver. 
Chrome and chromedriver should be properly installed and located on your computer.

First, the function test the existence of two folders: the first one stores the html map, the second one the png map. 
The two folders are created (normaly they can't exist on your computer), so we can begin thanks to the previous function to download the map of each day.
In the same for loop, `selenium` takes care of converting each html map into a png map and stores these file in the map_png folder created before.

.. code-block:: python

   def map_iteration(occ_df):

    # Definition of the navigator 
    driver = selenium.webdriver.Chrome()

    # Identification of the available days
    list_day = occ_df.day.unique()

    # path to folders we want to store our files into
    path_html = os.getcwd() + '\\map_html'
    path_png = os.getcwd() + '\\map_png'

    # test the non presence of the previous folders and then create them 
    if not os.path.exists(path_html):
        os.makedirs(path_html)
        
    if not os.path.exists(path_png):
        os.makedirs(path_png)

    for image_nb in range(len(list_day)):
        # save each map.html in the html folder
        map_day(occ_df, list_day[image_nb]).save('.//map_html/map_' + str(image_nb) + '.html')
        # choose a resolution
        driver.set_window_size(1000, 1000)
        # locate the path of the html file we want to convert
        path_to_get = os.getcwd() + '\\map_html\\map_' + str(image_nb)+ '.html'
        # the html map is opened on the navigator
        driver.get(path_to_get)
        # break to let time at the map to load
        time.sleep(1)
        # screenshot of the html map
        driver.save_screenshot("map_png/folium_%s.png" % str(image_nb).zfill(3))
        # close the windows
        plt.close('all')   

Step 3: Editing of the video 
----------------------------

This last step consists to edit the video with the png files. We use the package `imageio` to achieve what we want. 
Thanks to the sorting part in `get_ozone_day` function (refer to preprocess section), the png file are in the right order if you upstream process data with this function.

See the code below for more details: 

.. code-block:: python

   def animation():

    # indicate the folder where the function can find the png files
    png_dir = 'map_png'

    # empty variables where png files are concatenated
    images = []

    # loops through each png file
    for file_name in os.listdir(png_dir):
        # test if the file is a png file
        if file_name.endswith('.png'):
            # construct the path to the png file
            print(file_name)
            file_path = os.path.join(png_dir, file_name)
            # concatenate the png file with the previous one on image variable
            images.append(imageio.imread(file_path))
            
    # edit of the video        
    imageio.mimsave('animation.gif', images, fps=30)
