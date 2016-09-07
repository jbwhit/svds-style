# svds-style

This is a work in progress, if you feel that you have a better way of doing any of the below, please feel free to create a pull-request. 

## Setting up your laptop for Jupyter

Get miniconda.

```bash

cd ~/Downloads
wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh

# Lots of license agreements to read and agree to

#Update your .bashrc
source ~/.bashrc

conda update conda -y
```

Set up your environments (below are a reasonable list of packages to start with):

```bash

conda config --add channels conda-forge

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

conda create --name py2 python=2 $packages
conda create --name py3 python=3 $packages

# Install the matplotlib style library
pip install --upgrade mplsvds

```

## Setting up your laptop for SVDS style

```bash
# cd to wherever you put your github repos
git clone https://github.com/jbwhit/svds-style.git

# source activate whatever jupyter environment you use for svds

jupyter notebook --generate-config
mkdir -p ~/.jupyter/custom

if [ -e ~/.jupyter/custom/custom.css ]; then
    mv ~/.jupyter/custom/custom.css ~/.jupyter/custom/custom.css.`date +%Y-%m-%d`
else
    ln -s ${PWD}/css/jupyter/custom.css ~/.jupyter/custom/custom.css
fi
```

## What have you just done?

You just placed a `custom.css` file in your `~/.jupyter/custom` directory. This makes all of your notebooks follow the SVDS style -- but you aren't finished yet! 

Add the following snippet to your `.bashrc` file (making the initial change)

```bash
# Change this!
# Change this!
# Change this to be your initials!
export dsinitials='jbw'

# add to bashrc aliases
alias svds-activate-py2="source activate py2"
alias svds-activate-py3="source activate py3"
alias svds-deactivate="source deactivate"

svds-templatenb () {
    # Usage: svds-templatenb [exploratory_data_analysis]
    # Will download the most up-to-date Template notebook named with:
    # today's date, your initials, and [an optional phrase].
    # The example would yield a file named: 
    # 2016-08-17_jbw_exploratory_data_analysis.ipynb
    curl -H 'Accept: application/vnd.github.v3.raw' -L \
    https://api.github.com/repos/jbwhit/svds-style/contents/notebooks/Template-Python.ipynb \
    -o `date +%Y-%m-%d`_${dsinitials}_$1.ipynb
}

svds-minimalnb () {
    # Usage: svds-minimalnb [exploratory_data_analysis]
    # Will download the most up-to-date Template notebook named with:
    # today's date, your initials, and [an optional phrase].
    # The example would yield a file named: 
    # 2016-08-17_jbw_exploratory_data_analysis.ipynb
    curl -H 'Accept: application/vnd.github.v3.raw' -L \
    https://api.github.com/repos/jbwhit/svds-style/contents/notebooks/minimal-python.ipynb \
    -o `date +%Y-%m-%d`_${dsinitials}_$1.ipynb
} 

svds-create-project () {
    # Create directory structure in current working directory
    directories='docs
    report
    develop
    data
    source'

    for dir_name in ${directories}
    do
      mkdir $dir_name
      touch $dir_name/README.md
      if [ $dir_name = "source" ]; then
        mkdir -p $dir_name/sql
      fi
    done
}
```

## Why do we do dates this way?

![XKCD image](http://imgs.xkcd.com/comics/iso_8601.png)


