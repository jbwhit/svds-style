#!/bin/bash

cd ~/Downloads
wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh -b

# Add to and source .bashrc
export PATH="$HOME/miniconda3/bin:$PATH"
# Clears history
hash -r

# Don't ask if you want to update
conda config --set always_yes yes

# -q for quiet
conda update -q conda

# List info in case things don't work
conda info -a

# This adds the conda-forge channel below the defaults library
conda config --append channels conda-forge

packages='jupyter
notebook
ipywidgets
jupyter_contrib_nbextensions
jupyter_nbextensions_configurator
pyparsing
matplotlib
mkl
mpld3
seaborn
pip
pandas
scikit-learn
scipy
numpy
statsmodels
tqdm'

conda create -q --name py2 python=2 $packages
# Including r
conda create -q --name py3 --channel r r r-irkernel r-recommended r-essentials rpy2 python=3 $packages -y

source activate py3
# Install the matplotlib style library
pip install --upgrade mplsvds
source deactivate

source activate py2
# Install the matplotlib style library
pip install --upgrade mplsvds
source deactivate
