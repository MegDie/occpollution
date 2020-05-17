
![Python package](https://github.com/MegDie/occpollution/workflows/Python%20package/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/occpollution/badge/?version=latest)](https://occpollution.readthedocs.io/en/latest/?badge=latest)

# Overview

The motivation of this project is to perform some data visualization blending time and space representation of a dataset of Occitanie pollution and some analysis.


# Setup

Please check that all python packages in the `requirements.txt` file are installed on your computer in the correct version. To be sure every dependencies are installed in the right version you can simply run in a prompt:

    $ pip install -r requirements.txt


Read carefully the installation section in the doc to make sure everything is okay for the running of the package.

To install this package, you can simply run the following command in a prompt:

    $ pip install git+https://github.com/MegDie/occpollution

I recommand to clone the entire folder, and then install it (git must be functionnal on your computer): 

    $ git clone https://github.com/Megdie/occpollution
    $ pip install /path/to/occpollution
    

# Documentation

You could find the documentation of this package [here](https://occpollution.readthedocs.io/en/latest/). Please read carefully each part you want to exploit in the package.

# Demonstration

The execution of the `animation.py` file permit to create a gif of the evolution of ozone in Occitanie (more explanations in the doc). Please, read and follow the entire [installation section](https://occpollution.readthedocs.io/en/latest/installation/installation.html) in the doc before executing this script. 

In a prompt, you can simply run the following command:
    
    $ python /path/to/animation.py


The GIF is a bit long to edit, please wait about 20 minutes. Don't worry, Chrome will load some maps (362) and be very active, everything is normal. You can meanwhile read the documentation or have a drink ;)

# Structure

In the `\beamer` folder, you can find a presentation of this work.

The `\doc` folder contains some documentation about this project.

The `\interactive_notebooks` contains part of the projet necessiting interactivity, espacially boxplot widgets and interactive maps. The interactivity allows you to choose element as pollutant, date or city to visualize the data.

The folder `\occpollution` contains all the main code.

The `\report` folder contains a jupyter nootebook displaying different elements like widgets, maps, data visualization and some analysis (using ANOVA) to resume the entire project.