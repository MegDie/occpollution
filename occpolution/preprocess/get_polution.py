import  pandas as pd
import numpy as np

def get_polution(df_occ, log_scale=True):
  gd = df_occ.groupby(['nom_station']).size()
  if log_scale:
    gd = np.log(gd)
  return gd
