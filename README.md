# CMSC6950 Project: Fruitbat

## Precursory Requirements

### We will be using the conda environment for the fruitbat code. We Assume you already have conda installed and have working knowledge on it. If not, you can view the documentation [here](https://docs.conda.io/en/latest/).

### First by creating and entering the conda environment called Fruitbat by:
        conda create -n Fruitbat
        conda activate Fruitbat

### To run the required Python codes, you will need to download several modules. We will be using pip to install these.
### First, you should make sure your setuptools are up to date:
        pip3 install --upgrade setuptools

### Next, the following modules will be needed
	1.) numpy
	2.) scipy
	3.) astropy
	4.) matplotlib
	5.) pandas
	6.) pyymw16
	7.) e13tools
### which can be downloaded simultaneously using pip:
	pip3 install numpy scipy astropy matplotlib pandas pyymw16 e13tools

## Software Setup and Installation

### In the created conda environment, fruitbat is installed by:
	pip3 install fruitbat
	git clone https://github.com/abatten/fruitbat
	cd fruitbat
	pip install .

### Once installed, run the following python code to test everything has installed correctly:

	python3 test.py

### you should obtain the output *26.05327033996582 pc / cm3*


## What is fruitbat used for?
 change ordering - fruitbat first then packages
## How to use fruitbat
