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
### These will be downloaded with the *fruitbat* package if they are already not installed to your computer. *fruitbat* download commands are shown in the following section.

## Software Setup and Installation

### *fruitbat* is install by using either using pip:
	pip3 install fruitbat
	
### *OR* by cloning the repository:
	git clone https://github.com/abatten/fruitbat
	cd fruitbat
	pip install .

### For the purposes of this project however, using pip is sufficient.
 
### **Note:** if this project is being downloaded on a linux machine, an error may be displayed to the screen due to the *pyymw16* package. If this occurs, the *fruitbat* should be fine, however you should refer to the documentation [here](https://pypi.org/project/fruitbat/) if any issues arise.

### If not done so already, clone this repository using
        git clone https://github.com/bm2570/CMSC6950_Project.git
        cd CMSC6950_Project

### From here, run the following python code to test everything has installed correctly:
	python3 test.py
### If you obtain the output *26.05327033996582 pc / cm3*, the package has installed correctly and is ready to use.

## Usage of *fruitbat*
*fruitbat* is used in this project in a series of scripts to calculate cosmological properties using three separate methods referred to as **[Zhang2018](https://arxiv.org/pdf/1808.05277.pdf)**, **[Ioka2003](https://arxiv.org/pdf/astro-ph/0309200.pdf)**, and **[Inoue2004](https://academic.oup.com/mnras/article/348/3/999/1279487)** (refer to papers for precise details).

`distance_calculations.py` uses the *calc_redshift()*, *calc_comoving_distance()*, and *calc_luminosity_distance()* functions to calculate the redshift, comoving distance and luminosity distances for these methods.

`latlong.py` uses the *calc_dm_galaxy()* and *calc_redshift()* functions to determine the dispersion measure contribution from the Milky Way and its associated redshift over a defined grid of latitude and longitude coordinates.

## Running the Project 

Running the make file for this project will produce the pdf file and the finalized figures. To do so just simply type `make`. 
Note that this will take approximately 10 minutes to run. Any flags outputted to the screen from the *fruitbat* package or *latex* are just warnings and do not affect any of the results.
