Input/Output
===========================

The first step of each element of our projet is to reach the data we exploit. 
The following class download the data and then permit to python to read the csv file obtained to get a Pandas dataframe.
It uses the `read_csv` method from `Pandas` package and the `download` method from the `Download` package. 

.. code-block:: python

   class Load_db:
  r"""
  The Load_db class read a csv file downloaded on OpenData server. It contains only one method.
  """

  def __init__(self, url=url_db_an, target_name=path_target_an):
    download(url, target_name, replace=False)
  
  @staticmethod
  def save_as_df():
    r"""
    The save_as_df function return a Pandas Dataframe with the data.
    """
    df_occ = pd.read_csv(path_target_an)
    return df_occ


An important thing is that during the development of our project, the website where we got our Occitanie data changed some of his variables.
Geographic coordinates disappeared and it was very bothering for the construction of our map (see the map section), and the dates got an unreadable format.
That's why we had to use the most recent version of datas we had and stop the downloading of datas. 
So please, be carefull to don't change the argument "replace=False" in the  download method, in any function of the project, at the risk to swich good datad against corrupted ones. 
In fact, the path (path_target_an, path_target, etc.) is still connected to the url of updated data in all our functions.
We stopped collecting the data the 2020 April 24. 

