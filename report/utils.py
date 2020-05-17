# This code is usefull so as not to weigh down the report

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Montpellier data
occitanie = pd.read_csv("datasets/Mesure_journaliere_Region_Occitanie_Polluants_Principaux.csv", sep="," , header=0)
occitanie = occitanie[occitanie['nom_com'] == 'MONTPELLIER'] # selection of Montpellier
occitanie = occitanie[occitanie['nom_poll'] == 'O3'] # Only Prés d' Arènes urbain available for O3 
occitanie['date'] = pd.to_datetime(occitanie['date_debut']).dt.to_period('M') # good format for the date
occitanie = occitanie.sort_values(by = 'date', ascending = True) # date sorting
mtp = occitanie.groupby('date').agg({'valeur':'mean'}) # mean to have value for months
mtp['date'] = occitanie.date.unique()
mtp['nom_com'] = ['MONTPELLIER']*13
mtp['X'] = ['3.88689']*13
mtp['Y'] = ['43.5915']*13
mtp['O3'] = mtp['valeur']

occitanie = pd.read_csv("datasets/Mesure_journaliere_Region_Occitanie_Polluants_Principaux.csv", sep="," , header=0)
occitanie = occitanie[occitanie['nom_com'] == 'MONTPELLIER']
occitanie = occitanie[occitanie['nom_poll'] == 'NO2'] 
occitanie['date'] = pd.to_datetime(occitanie['date_debut']).dt.to_period('M')
occitanie = occitanie.sort_values(by = 'date', ascending = True)
NO2_df = occitanie.groupby('date').agg({'valeur':'mean'})
NO2_df['date'] = occitanie.date.unique()
mtp['NO2'] = NO2_df['valeur']
variables = ['nom_com', 'O3', 'NO2', 'date', 'X', 'Y' ]
mtp = mtp[variables]


# Paris data
paris = pd.read_csv("datasets/PA13_ANOVA.csv", sep=";" , header=0)
paris = paris[paris.date.isna()==False] # delete Nan row
paris = paris[paris['O3']!='n/d'] # no line without O3 data
paris['O3'] = paris['O3'].astype('float') # convert measurement as float
paris['date'] = pd.to_datetime(paris['date'], dayfirst = True).dt.to_period('M') # good format for the date
paris = paris.sort_values(by = 'date', ascending = True)
jour_paris = paris.date.unique()
par = paris.groupby('date').agg({'O3':'mean'}) # mean by day because we have hours
par['date'] = jour_paris
par['valeur'] = par['O3']
par['nom_com'] = ['PARIS']*13
par['X'] = [2.3488]*13
par['Y'] = [48.8534]*13

paris = pd.read_csv("datasets/PA13_ANOVA.csv", sep=";" , header=0)
paris = paris[paris.date.isna()==False]
paris = paris[paris['NO2']!='n/d']
paris['NO2'] = paris['NO2'].astype('float')
paris['date'] = pd.to_datetime(paris['date'], dayfirst = True).dt.to_period('M')
paris = paris.sort_values(by = 'date', ascending = True)
jour_paris = paris.date.unique()
paris_NO2_df = paris.groupby('date').agg({'NO2':'mean'})
par['NO2'] = paris_NO2_df['NO2']
par = par [variables]

# plot the data 
def plot_lines():
    plt.figure(figsize=(15,5))
    plt.subplot(1, 2, 1)
    ax = plt.gca()
    par.plot(kind='line',x='date',y='O3',ax=ax, color = 'pink', label = 'Paris 13')
    mtp.plot(kind='line',x='date',y='O3', color='orange', ax=ax, label = "Montpellier prés d'Arènes")
    plt.title("O3 evolution over months between April 2019 and April 2020")
    plt.subplot(1, 2, 2)
    ax = plt.gca()
    par.plot(kind='line',x='date',y='NO2',ax=ax, color = 'pink', label = 'Paris 13')
    mtp.plot(kind='line',x='date',y='NO2', color='orange', ax=ax, label = 'Montpellier Chaptal')
    plt.title("NO2 evolution over months between April 2019 and April 2020")
    #plt.show()
    plt.tight_layout()

# boxplot with interactivity
def boxplot_widget(pollutant):

    df_villes = pd.concat([mtp, par])
    
    plt.style.use('dark_background')
    sns.catplot(x = 'nom_com', y = pollutant, 
            data = df_villes,
            height = 3, aspect = 2,
            kind = 'boxen')
    plt.tight_layout()
    plt.xlabel('Cities')
    plt.ylabel(pollutant)
    plt.title(pollutant + " measurement between 04/2019 and 04/2020")
    plt.show()

# data for anova
df_villes = pd.concat([mtp, par])
df_ANOVA = df_villes[['nom_com', 'O3', 'NO2']]

# containment data
occitanie = pd.read_csv("datasets/Mesure_journaliere_Region_Occitanie_Polluants_Principaux.csv", sep="," , header=0)
mtp_df = occitanie[occitanie['nom_com'] == 'MONTPELLIER']
mtp_df['date'] = pd.to_datetime(mtp_df['date_debut']).dt.to_period('D')
mtp_df = mtp_df.sort_values(by = 'date', ascending = True)
variables = ['nom_com', 'nom_station', 'nom_poll', 'valeur', 'date' ]
mtp_df = mtp_df[variables]
mtp_df = mtp_df.iloc[3649:5388,]
mtp_df







