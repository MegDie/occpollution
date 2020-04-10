
# Overview

The motivation of this project is to perform some data visualization blending time and space representation of a dataset of Occitanie pollution.

The ultimate goal for this project is to make a video of the O3 (ozone) level across time for the cities available in the dataset.

**Widget :** 
A widget will compare, using boxplot/violins, the level of pollution across at least 3 cities from the dataset.

**Map rendering :**
A synthetic map display the degree of pollution in the cities provided. 

**Harmonization :**
Analysis jointly of the data from Montpellier and Paris (Paris 13ème)




# Structure

In the `\beamer` folder, you will find soon a presentation of this work

The `\doc` report will contain some documentation about this project

The `\report` folder contains some jupyter notebooks to display different elements like widgets, maps and soon data visualization by interactive histrograms and some analysis (using ANOVA)

The report `\occpolution` will contain a package python deploying widgets and interactive maps showing pollution data of Occitanie, it is made of the subfolders:
  + `.\ani` will display a video showing the evolution of ozone pollution per dey in Occitanie 
  + `.\map` will display an interactive map showing the level of ozone in Occitanie for a day/month we choose
  + `.\widget` will display widgets comparing the level of ozone of three cities

# (Co)worker(s)

    Mégane Diéval, `megane.dieval@etu.umontpellier.fr`

    Gueladio Niasse, `gueladio.niasse@etu.umontpellier.fr`

    Jean-Baptiste Elucson, `jean-baptise.elucson@etu.umontpellier.fr`