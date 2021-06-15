# CMSC6950 Project: Fruitbat

## What is Fruitbat and What is it Used For?

*fruitbat* is an open source third party Python package used to calculate fast radio bursts (FRBs) from sources residing outside of the Milky Way galaxy. For more info, see the paper [here](https://arxiv.org/pdf/1905.04294.pdf).

## Precursory Requirements

### To run the required Python codes, you will need to download several modules. The following are needed:
	1.) numpy
	2.) scipy
	3.) astropy
	4.) matplotlib
	5.) pandas
	6.) pyymw16
	7.) e13tools
### These will be downloaded when the *fruitbat* package is downloaded. *fruitbat* is downloaded by the commands in the following section.

## Software Setup and Installation

### *fruitbat* is installed by:
	pip install fruitbat
	pip install fruitbat
	git clone https://github.com/abatten/fruitbat
	cd fruitbat
	pip install .

### Once installed, run the following python code to test everything has installed correctly:
	python3 ../test.py
### If you obtain the output *26.05327033996582 pc / cm3*, the package has installed correctly and is ready to use.

## Usage of *fruitbat*
*fruitbat* is used in this project in a series of scripts to calculate cosmological properties using three methods referred to as **[Zhang2018](https://arxiv.org/pdf/1808.05277.pdf)**, **[Ioka2003](https://arxiv.org/pdf/astro-ph/0309200.pdf)**, and **[Inoue2004](https://academic.oup.com/mnras/article/348/3/999/1279487)**.

`distance_calculations.py` uses the *calc_redshift()*, *calc_comoving_distance()*, and *calc_luminosity_distance()* functions to calculate the redshift, comoving distance and luminosity distances for these methods.

`latlong.py` uses the *calc_dm_galaxy()* and *calc_redshift()* functions to determine the dispersion measure contribution from the Milky Way and its associated redshift over a defined grid of latitude and longitude coordinates.

## Running the Project 

Running the make file provided will produce the pdf file and the finalized figures. 
Note that this will take approximately 10 minutes to run. Any flags outputted to the screen are just warnings from the *fruitlab* package that not affect any of the results.
