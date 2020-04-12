from setuptools import setup
from occpollution import __version__ as current_version

setup(
  name='occpollution',
  version=current_version,
  description='Visualization of Ozone pollution in Occitanie',
  url='https://github.com/MegDie/Project_Occitanie_Polution',
  author='Mégane Diéval',
  author_email='megane.dieval@etu.umontpellier.fr',
  license='MIT',
  packages=['occpollution', 'occpollution.map',
   'occpollution.ani', 'occpollution.widget', 'occpollution.preprocess', 'occpollution.io'],
  zip_safe=False
)