Data
====================

We exploit data from `the following website`_ . 
Atmo-Occitanie has an open data portal providing data about air quality in Occitanie, with dayly, monthly or annual measures.

.. _the following website: http://data-atmo-occitanie.opendata.arcgis.com/search?tags=Mesures


The variables we focus on are:

- "nom_com" : the name of the city
- "nom_station", "code_station" : the name of the station, there could be more than one station for each city
- "X", "Y" : formerly the geographic coordinates (no longer available)
- "nom_poll" : name of the pollutant
- "valeur" : measured value of the pollutant
- "date_debut", "date_fin" : the date of the beginning and the end of measurement


Only one year of data is available for daily data, the ones we use to code our widgets.

