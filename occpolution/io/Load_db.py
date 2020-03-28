import pandas as pd
from download import download
from occpollution.io import url_db, path_target



class Load_db:
  def __init__(self, url=url_db, target_name=path_target):
    download(url, target_name, replace=True)
  
  @staticmethod
  def save_as_df():
    df_occ = pd.read_csv(path_target, na_values="", low_memory=False, converters={'nom_station': str, 'date': str})
    return df_occ
