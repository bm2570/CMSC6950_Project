# CMSC6950 Project: Fruitbat

## What is Fruitbat and What is it Used For?

*fruitbat* is an open source third party Python package used to calculate fast radio bursts (FRBs) from sources residing outside of the Milky Way galaxy. For more info, see the paper [here](https://arxiv.org/pdf/1905.04294.pdf).

## Precursory Requirements

### We will be using the conda environment for the fruitbat code. We Assume you already have conda installed and have working knowledge on it. If not, you can view the documentation [here](https://docs.conda.io/en/latest/).

### First create and enter the conda environment called Fruitbat by:
        conda create -n Fruitbat
        conda activate Fruitbat

### To run the required Python codes, you will need to download several modules. We will be using pip to install these.We will need the following modules:
	1.) numpy
	2.) scipy
	3.) astropy
	4.) matplotlib
	5.) pandas
	6.) pyymw16
	7.) e13tools
### These can be downloaded simultaneously using pip:
	pip3 install numpy scipy astropy matplotlib pandas pyymw16 e13tools
### Note: if any issues arise when downloading these packages, make sure your setuptools are up to date:
        pip3 install --upgrade setuptools

## Software Setup and Installation

### In the created conda environment, install fruitbat by:
	pip3 install fruitbat
	git clone https://github.com/abatten/fruitbat
	cd fruitbat
	pip install .

### Once installed, run the following python code to test everything has installed correctly:
	python3 test.py
### If you obtain the output *26.05327033996582 pc / cm3*, the package is ready to use.

