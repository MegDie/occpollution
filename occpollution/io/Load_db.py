import pandas as pd
from download import download
from occpollution.io import url_db_an, path_target_an

class Load_db:
  r"""
  The Load_db class read a csv file downloaded on OpenData server. It contains only one method.
  """

  def __init__(self, url=url_db_an, target_name=path_target_an):
    download(url, target_name, replace=True)
  
  @staticmethod
  def save_as_df():
    r"""
    The save_as_df function return a Pandas Dataframe with the data.
    """
    df_occ = pd.read_csv(path_target_an)
    return df_occ
