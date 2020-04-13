import pandas as pd
from download import download
from occpollution.io import url_db, path_target

class Load_db:
  r"""
  The Load_db class read a csv file downloaded on OpenData server. It contains only one method.
  """

  def __init__(self, url=url_db, target_name=path_target):
    download(url, target_name, replace=False)
  
  @staticmethod
  def save_as_df():
    r"""
    The save_as_df function return a Pandas Dataframe with the data.
    """
    df_occ = pd.read_csv(path_target)
    return df_occ
