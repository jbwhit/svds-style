[![Build Status](https://travis-ci.org/jbwhit/svds-style.svg?branch=master)](https://travis-ci.org/jbwhit/svds-style)

# svds-style

This is a work in progress, if you feel that you have a better way of doing any of the below, please feel free to create a pull-request. 

This is meant to take a laptop from factory settings into something usable (or at least far along that path). 

```bash
git clone https://github.com/jbwhit/svds-style.git
```

```bash

cd setup
bash 01-initial-setup.bash
bash 02-brew.bash
bash 03-python-setup.bash
```


## Your laptop will now have

 - brew installed
 - conda installed w/ reasonable starting packages
 - svds-style installed (automatically make Jupyter Notebooks have SVDS templating)
 - mplsvds installed (plots will use SVDS colors)
 - one-command functions to create minimal or template notebooks that query most up-to-date versions automatically
 - Extra command line tools 
     + pandoc
     + tmux
     + wget
     + grep
 - Applications (that you don't have to install separately from internet)
     + iTerm2
     + Sublime Text
     + Google Chrome
     + caffeine
     + flux
     + SourceTree
     + VLC

## Next 

Set up your `~/.ssh/config` file. This is a good start: http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/

```
mkdir -p $HOME/.ssh
chmod 0700 $HOME/.ssh
```

Have a new key-pair for each new client laptop.

Learn tmux http://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/
http://www.starkandwayne.com/blog/iterm-and-tmux-sitting-in-a-tree/

## Setting up your laptop for SVDS style

```bash
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

alias svds-activate-py2="source activate py2"
alias svds-activate-py3="source activate py3"
alias svds-deactivate="source deactivate"




```

## Why do we write dates this way?

![XKCD image](http://imgs.xkcd.com/comics/iso_8601.png)


## Incredibly useful additions to bashrc

Add the following to your `.bashrc` -- you have to run the commented commands first (but leave the comments in for future reference). These additions put the current git branch in your terminal, and allow for tab-completion of git commands. 

```bash
# curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash

if [ -f ~/.git-completion.bash ]; then
  . ~/.git-completion.bash
fi

# mkdir ~/.bash
# cd ~/.bash
# git clone git://github.com/jimeh/git-aware-prompt.git
export GITAWAREPROMPT=~/.bash/git-aware-prompt
source $GITAWAREPROMPT/main.sh

```

## Decommissioning 

First make sure that everything that needs to be backed up at the client is backed up and delivered. Get an OK from your SA that you are going to wipe your laptop. 

 - Delete .ssh/
 - Remove installed applications
     + Slack (shouldn't be there anyway)
     + Evernote (shouldn't be there anyway)
     + Dropbox
     + Chrome
         * de-link account
         * clear browsing data from the beginning of time
     + Documents
     + Downloads
     + project folder
     + miniconda
 - Empty trash



