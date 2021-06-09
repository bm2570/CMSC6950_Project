# CMSC6950_Project

Project choice: PyAutoLens

Software Setup

#Create 
conda create -n PyAutoLens
conda activate PyAutoLens
#download packages needed
astropy numba numpy scikit-image scikit-learn scipy autoconf

conda activate PyAutoLens

git clone https://github.com/Jammy2211/PyAutoLens.git

conda install pip
#use conda to install PyAutoLens dependencies
pip install -r PyAutoLens/requirements.txt

conda install conda-build
conda-develop PyAutoLens

git clone https://github.com/rhayes777/PyAutoFit
git clone https://github.com/Jammy2211/PyAutoArray
git clone https://github.com/Jammy2211/PyAutoGalaxy
git clone https://github.com/Jammy2211/PyAutoLens

pip install -r PyAutoFit/requirements.txt
pip install -r PyAutoArray/requirements.txt
pip install -r PyAutoGalaxy/requirements.txt
pip install -r PyAutoLens/requirements.txt

conda-develop PyAutoFit
conda-develop PyAutoArray
conda-develop PyAutoGalaxy
conda-develop PyAutoLens

pip install pytest
pip install autoconf


test working:
cd /path/to/PyAutoFit
python3 -m pytest

