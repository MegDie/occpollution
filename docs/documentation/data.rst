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

Data from the Atmo-Occitanie measurement network are available at different time steps (Annual, Monthly, Daily, Hourly).

Update frequency:
- For hourly data: every hour (72h / 30d / 1 year rolling)
- For daily data: every day from 2 p.m. (1 year rolling)
- For monthly data: First Sunday of the month for month N-1 (1 year rolling)
- For annual data: First quarter for year N-1 after validation (Maximum 5 years)



