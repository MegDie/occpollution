Preprocess
===========================

Once we have our datas stocked in a Pandas dataframe (see Input/Output section), we have to edit and transform some elements.

The first thing we need is a usable format of the date. 
The goal of our project is to follow the evolution of pollution over time so we must extract this element. 
We use the `to_datetime` method of `Pandas` Package to convert the date variables into a usable format.

In most case of our project, we have to focus our attention on one pollutant: the ozone.
So we have to select only this pollutant between all the others available (NO2, PM10, NO, etc.)

One last thing important is to standardize the value of the measurement. 
In fact, in our map (see map section), we have to have a great color scale to make a good difference between hight level and low level of pollution by color circles. 
To resolve this problem, we decide to standardize the value of pollution by centering and reducing the value.

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

    def get_ozone_day(occ_df):

    r"""
  The get_ozone_day function is a data treatment.
  """

    occ_df['date'] = pd.to_datetime(occ_df['date_debut']).dt.to_period('D')
    occ_df = occ_df[occ_df['nom_poll'] == 'O3'] 
    occ_df['standard'] = (occ_df[['valeur']] - np.mean(occ_df[['valeur']]))/ np.std(occ_df[['valeur']])
    variables = ['X', 'Y', 'nom_com', 'nom_station', 'valeur', 'date', 'standard']
    occ_df = occ_df[variables]
    occ_df = occ_df.sort_values(by = 'day', ascending = True)
    return occ_df

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

