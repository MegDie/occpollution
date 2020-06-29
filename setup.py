from setuptools import setup
from occpollution import __version__ as current_version
setup(
  name='occpollution',
  version=current_version,
  description='Visualization of ozone pollution in Occitania',  
  url='https://github.com/MegDie/occpollution',
  author='MEGANE Diéval, GUELADIO Niasse, JEAN BAPTISTE Elucson',
  author_email='megane.dieval@etu.umontpellier.fr',
  autor_email='gueladio.niasse@etu.umontpellier.fr',
  author_email='jean-baptiste.elucson.etu.umontpellier.fr',
  license='MIT',
  packages=['occpollution', 'occpollution.map',
   'occpollution.ani', 'occpollution.preprocess', 'occpollution.io', 'occpollution.map'],
  zip_safe=False
)
