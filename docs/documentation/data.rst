Data
====================

Where Occitanie data come from ? 
-----------------------------------

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

We also include (sometimes) Paris data, see sources section for more informations.


Why Ozone as a pollution indicator?
----------------------------------------- 

In most of our research, we chose the ozone (O3) as an indacator of pollution. If ozone is one of the common pollutant between Occitanie and Paris, 
there are also other good reasons to choose it.

Ozone is a highly reactive, unstable chemical compound made up of three oxygen atoms. 
The chemical formula for ozone is O3. It plays a very important role in earthly life. 
Naturally present in the atmosphere, it forms a layer in the stratosphere (12 to 50 km above the ground), which protects from ultraviolet rays (more than 97% of ultraviolet rays are intercepted by this layer). 
On the other hand, in the lower layers of the atmosphere (troposphere, from 0 to 12 km above the ground), ozone is an atmospheric pollutant harmful to human health, animals and plants, because of its oxidizing nature.

For the general public, the term pollution often evokes a toxic chemical released into the environment. And in this case, we immediately perceive the potential danger and risks for the health of our children and for ourselves. 
However, the nature of pollution is very varied. Pollutants can be natural or artificial, chemical or biological, toxic or not. 
Sometimes their pollutant status simply depends on increasing their concentration or interacting with another factor. 
Furthermore, the concerns are not the same if one is interested in the health of an individual, or of a population, that of the planet or the biological diversity of an environment.

Ozone is a secondary pollutant, which means that it is not emitted directly by human activities. The latter results, in fact, from chemical transformations, under the effect of solar radiation, of primary pollutants such as nitrogen oxides and volatile organic compounds. 
Weak wind, strong heat are the ingredients that, in general, most immediately explain its appearance. 
It affects plants and reduces crop yields by disturbing photosynthesis. 
It contributes to the greenhouse effect and to the oxidation of certain materials such as textiles or rubber.
It is a very irritating gas which easily penetrates to the thinnest respiratory tract. 
It can cause irritation of the eyes, nose and throat, cough, shortness of breath, especially in the most sensitive people (the elderly, asthmatics, young children). 
Thus, high daily concentrations of ozone are associated with an increase in asthma attacks and hospital admissions for respiratory and cardiovascular causes, according to Santé Publique France.
According to a study published in 2016 by the European Environment Agency, "chronic exposure to ozone is responsible for nearly 500 deaths from respiratory causes each year" in France. 
Less than the 48,000 annual deaths attributed to fine particles, another air pollutant. 
Concerning this time the pollution peaks, another study by the same agency relating to nine large cities concluded that during the heat wave of 2003, ozone would have been responsible for 380 premature deaths (including 228 in Paris) between 3 and August 17.
So, at very high rates, this gas reduces the ability of plants to provide photosynthesis. 
"Very high levels of O3 cause damage to plant cells, altering their reproduction and growth, thus reducing the production of agricultural crops, forest growth and biodiversity", underlines the European Environment Agency (EEA).




