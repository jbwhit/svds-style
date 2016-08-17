# svds-style

## Setting up your laptop for Jupyter


```bash

cd ~/Downloads
wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh

# Lots of license agreements to read and agree to

#Update your .bashrc
source ~/.bashrc

conda update conda -y
```

```bash

conda config --add channels conda-forge

packages='jupyter
notebook
ipywidgets
jupyter_nbextensions_configurator
pyparsing
matplotlib
seaborn
mpld3
pandas
scikit-learn
scipy
numpy
statsmodels'

conda create --name py3 python=3 $packages
conda create --name py2 python=2 $packages

pip install mplsvds

# add to bashrc aliases
alias envpy2="source activate py2"
alias envpy3="source activate py3"
alias sd="source deactivate"
alias nb="jupyter notebook"

```

## Setting up your laptop for SVDS style

```bash
git clone git@github.com:jbwhit/svds-style.git
cd svds-style

# source activate whatever jupyter environment you use for svds

jupyter notebook --generate-config
mkdir -p ~/.jupyter/custom

if [ -f ~/.jupyter/custom/custom.css ]; then
    mv ~/.jupyter/custom/custom.css ~/.jupyter/custom/custom.css.`date +%Y-%m-%d`
else
    ln -s ${PWD}/css/jupyter/custom.css ~/.jupyter/custom/custom.css
fi
```

## What have you just done?

You just placed a `custom.css` file in your `~/.jupyter/custom` directory. This makes all of your notebooks follow the SVDS style -- but you haven't finished yet! 


svdsnb () {
    # Usage: svdsnb [exploratory_data_analysis]
    # Will download the most up-to-date Template notebook named with:
    # today's date, your initials, and [an optional phrase].
    # The example would yield a file named: 
    # 2016-08-17_jbw_exploratory_data_analysis.ipynb
    curl -H 'Authorization: token e619d2e19d93aaa8f6f30b7b6e2b4581fa6a0ed0' -H 'Accept: application/vnd.github.v3.raw' -L https://api.github.com/repos/jbwhit/svds-style/contents/notebooks/Template-Python.ipynb -o `date +%Y-%m-%d`_jbw_$1.ipynb
} 
