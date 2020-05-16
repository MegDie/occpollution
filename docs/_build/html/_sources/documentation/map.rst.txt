Occitanie Map
===========================

One of the goals of this project is to provide an interactive map showing the differences of pollution between cities of Occitanie.
If you can find a very full development of the map construction in the interactive part (see interactive_notebooks in the principal folder), you can have here an idea of the main code.
Our map are built under the `Folium` package. You can find more explanations about this package `here`_ .
`Folium` allows you to visualize data manipulated with Python.

.. _here: https://python-visualization.github.io/folium/


The following code is used to build a static map (counter to interactivity in the notebooks) of data in 2018. 
We focus on this year but it's only an exemple because data of 2019 are also available for Occitanie.
Therefore, the goal of this code is to plot a folium map with the annual dataset of Occitanie in 2018.
We use colored circles showing the severity of the pollution, based on the ozone level.

As explained in the code, we begin to select the year 2018 between all the available years and then we built the color scale for the circles with the `color_scale` function (see preprocess section for more details).
With a for loop, we plot the value of each city in the initialized map. `Folium` allows you to choose the zoom and location start.
Thanks to the geographic coordinates variable (the one that disapeared in the most recent data, see data section), we plot without problem each city at the right location.
The diameter of each circle (radius argument) depends on the value of ozone (with a multiplier). 
The color of each circle is choosen with the `color_scale` function that determine the lowest and highest value of the standardized value of ozone measurement.
The map obtained is saved under a html file.

.. code-block:: python

   def plot_interactive_map(occ_df):
    r"""
  The plot_interactive_map function plots the data.

  Input
  -----
    occ_df: Pandas data frame. 

  Output
  ------
    A folium map

  Example
  -------

  >> import occpollution
  >> occpollution.map.plot_interactive_map(df)

  """

    # selection of the year
    occ_2018 = occ_df[occ_df['date'] == '2018']
    
    # color scale
    linear = color_scale(occ_2018)

    # initialization if the map 
    map = folium.Map(location=[43.9333, 2.15], 
                 zoom_start=7.5, 
                 tiles='Stamen Terrain')
                 
    for i in range(0,len(occ_2018)):
        folium.Circle(
            # location of the city
            location=[occ_2018.iloc[i]['Y'], occ_2018.iloc[i]['X']],
            # we show the name of the station
            popup=occ_2018.iloc[i]['nom_station'],
            # radius of circle
            radius=occ_2018.iloc[i]['valeur']*100,
            # color of the circle
            color='black',
            # the color we fill circle with
            fill=True,
            fill_color=linear(occ_2018.iloc[i]['standard']),
            fill_opacity=0.5,
            opacity=0.4,
            ).add_to(map)
    
    map.save('map_occitanie2018.html') # we save the map into an html file

    return (map)