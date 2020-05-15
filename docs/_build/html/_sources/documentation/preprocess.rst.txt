Preprocess
===========================

Treatment of data for Occutanie map in 2018
-----------------------------------------------

Once we have our datas stocked in a Pandas dataframe (see Input/Output section), we have to edit and transform some elements.

The first thing we need is a usable format of the date. 
The goal of our project is to follow the evolution of pollution over time so we must extract this element. 
We use the `to_datetime` method of `Pandas` Package to convert the date variables into a usable format.

In most case of our project, we have to focus our attention on one pollutant: the ozone.
So we have to select only this pollutant between all the others available (NO2, PM10, NO, etc.)

One last thing important is to standardize the value of the measurement. 
In fact, in our map (see map section), we have to have a great color scale to make a good difference between hight level and low level of pollution by color circles. 
To resolve this problem, we decide to standardize the value of pollution by centering and reducing the value.

The following function `get_ozone_an` do everything we said and is used for the treatment of datas in order to provide a map of the mean level of ozone in Occitanie in 2018. 
You could find this map in the little demonstration providing by executing the `script.py` file.

.. code-block:: python

   def get_ozone_an(occ_df):
    
    r"""
  Treatment of our data frame about annual data.
  """

    # usable format of the date (for the year here):
    occ_df['date'] = pd.to_datetime(occ_df['date_debut']).dt.to_period('Y')

    # selection of the pollutant:
    occ_df = occ_df[occ_df['nom_poll'] == 'O3']

    # standardization of the value:
    occ_df['standard'] = (occ_df[['valeur']] - np.mean(occ_df[['valeur']]))/ np.std(occ_df[['valeur']])

    return occ_df

Treatment of data for the animation
--------------------------------------

The following function is a bit more complete then the previous one but mostly do the same thing.

One of the additional things is the sorting of the date. 
In this project, the ultimate goal for this project was to make a video of the O3 (ozone) level across time for the cities available in the dataset.
So to have a good animation, we have to order the date to have a chronologic video. 
We use the method `sort_values` to sort our dates.

We also select the variables we care of to short the datas.

.. code-block:: python

    def get_ozone_day(occ_df):

    r"""
  The get_ozone_day function is a data treatment.
  """
    # usable format for the date
    occ_df['date'] = pd.to_datetime(occ_df['date_debut']).dt.to_period('D')

    # only pollutant we need
    occ_df = occ_df[occ_df['nom_poll'] == 'O3'] 

    # standardization of the value
    occ_df['standard'] = (occ_df[['valeur']] - np.mean(occ_df[['valeur']]))/ np.std(occ_df[['valeur']])

    # only variables we care about 
    variables = ['X', 'Y', 'nom_com', 'nom_station', 'valeur', 'date', 'standard']
    occ_df = occ_df[variables]

    # sort of dates
    occ_df = occ_df.sort_values(by = 'day', ascending = True)

    return occ_df

Function for the color scale of our map
--------------------------------------------

The last thing to approach in this section is the function `color scale`. We use it to have a good color scale of our circles. 
The green color correspond to a low level of pollutant concentration and the red color to a high level, as the logic wants.
The function identify what is the lowest and the highest value in a variable and then create a linear color scale using the method `LinearColormap` in the submodule `colormap` of the package `branca`, between this two values. 

.. code-block:: python

   def color_scale(occ_df):

    r"""
  The color_scale function determine a color scale for the circles indicating level of pollution.
  """
    
    linear = cm.LinearColormap(
    ['green', 'yellow', 'red'],
    vmin=min(occ_df['standard']), vmax=max(occ_df['standard'])
    )
    
    return(linear)

