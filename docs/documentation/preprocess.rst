Preprocess
===========================

.. code-block:: python

   def get_ozone_an(occ_df):
    
    r"""
  Treatment of our data frame about annual data.
  """

    occ_df['date'] = pd.to_datetime(occ_df['date_debut']).dt.to_period('Y')
    occ_df = occ_df[occ_df['nom_poll'] == 'O3'] 
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

