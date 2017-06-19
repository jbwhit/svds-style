[![Build Status](https://travis-ci.org/jbwhit/svds-style.svg?branch=master)](https://travis-ci.org/jbwhit/svds-style)

# svds-style

This is a work in progress, if you feel that you have a better way of doing any of the below, please feel free to create a pull-request. 

This is meant to take a laptop from factory settings into something usable (or at least far along that path). 

For all setups, I recommend the following: 

```bash
git clone https://github.com/jbwhit/svds-style.git
cd svds-style/setup-minimal

# "install" when prompted
bash 01-initial-setup.bash

# This takes a while, unless it returns an error, wait.
bash 02-brew.bash

# This takes a while, unless it returns an error, wait.
bash 03-python-setup.bash
```

If your computer is an SVDS/non-client laptop, also run (this installs further applications like Slack): 

```bash

cd ../svds-setup
bash 02-brew.bash

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
     + SourceTree (a git client)

## Why use iTerm2?

First, follow the directions to [include shell integration](https://www.iterm2.com/documentation-shell-integration.html). 

Now you can do many cool things like: 

 - Drag-drop local files to a host
 - `scp` files from remote hosts with right click
 - Alert when long-running command returns
 - Undo window close if cmd+z within 5 seconds
 - Can turn on timestamps

Some recommended updates: 

 - turn off the helpful windows for pasting text

## Next SSH setup

This is a good start: http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/

Begin with:

```
mkdir -p $HOME/.ssh
chmod 0700 $HOME/.ssh
```

 - Create a new key-pair for each new client laptop (with passphrase).
 - [Update your github account](https://github.com/settings/keys) w/ the new public key.

Set up your `~/.ssh/config` file (create it if it doesn't exist).

And example config entry:

```bash
Host supercomputer
    HostName address.ip.numbers
    User username
    IdentityFile ~/.ssh/id_rsa
```

 - Send your public key to the computer you want access to with `ssh-copy-id`: like: `ssh-copy-id -i ~/.ssh/id_rsa.pub username@address.ip.numbers`


 - Learn tmux http://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/
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

```

## Incredibly useful additions to bashrc

Also, add the following to your `.bashrc` -- you have to run the commented commands first (but leave the comments in for future reference). These additions put the current git branch in your terminal, and allow for tab-completion of git commands. 

```bash

export PS1="\n# \w\n# \[${Green}\]\h \[${Color_Off}\]\[${Cyan}\]\${git_branch}\[${Red}\]\$git_dirty\[${Color_Off}\]$ "


# This can go in .inputrc (w/o the bind "")
bind "set completion-ignore-case on"
bind "set bell-style none"


#    eg. save mc
#    cd mc # no '$' is necessary
if [ ! -f ~/.dirs ]; then  # if doesn't exist, create it
    touch ~/.dirs
fi

alias show='cat ~/.dirs'
save (){
    command sed "/!$/d" ~/.dirs > ~/.dirs1; \mv ~/.dirs1 ~/.dirs; echo "$@"=\"`pwd`\" >> ~/.dirs; source ~/.dirs ;
    source ~/.dirs  # Initialization for the above 'save' facility: source the .sdirs file
}
source ~/.dirs  # Initialization for the above 'save' facility: source the .sdirs file
shopt -s cdable_vars # set the bash option so that no '$' is required when using the above facility

function path(){
    old=$IFS
    IFS=:
    printf "%s\n" $PATH
    IFS=$old
}

# git completion (if you installed via the setup instructions above)
if [ -f `brew --prefix`/etc/bash_completion.d/git-completion.bash ]; then
    . `brew --prefix`/etc/bash_completion.d/git-completion.bash
fi


if [ -f $(brew --prefix)/etc/bash_completion ]; then
. $(brew --prefix)/etc/bash_completion
fi

# git
if [ -f `brew --prefix`/etc/bash_completion.d/git-completion.bash ]; then
    . `brew --prefix`/etc/bash_completion.d/git-completion.bash
fi

# setup here: https://www.iterm2.com/documentation-shell-integration.html
source ~/.iterm2_shell_integration.`basename $SHELL`

# You have to run this commented code first before this will work
# mkdir ~/.bash
# cd ~/.bash
# git clone git://github.com/jimeh/git-aware-prompt.git
export GITAWAREPROMPT=~/.bash/git-aware-prompt
source $GITAWAREPROMPT/main.sh

```

Add the following so that an SSH agent runs and handles your key-passphrases.

```bash
    SSH_ENV="$HOME/.ssh/env"
    function start_agent {
        echo "Initialising new SSH agent..."
        /usr/bin/ssh-agent | sed 's/^echo/#echo/' > "${SSH_ENV}"
        echo succeeded
        chmod 600 "${SSH_ENV}"
        . "${SSH_ENV}" > /dev/null
        /usr/bin/ssh-add;
    }
    # Source SSH settings, if applicable
    if [ -f "${SSH_ENV}" ]; then
        . "${SSH_ENV}" > /dev/null
        #ps ${SSH_AGENT_PID} doesn't work under cywgin
        ps -ef | grep ${SSH_AGENT_PID} | grep ssh-agent$ > /dev/null || {
            start_agent;
        }
    else
        start_agent;
    fi
```


## Why do we write dates this way?

![XKCD image](http://imgs.xkcd.com/comics/iso_8601.png)

## Misc

### Git

 - add `.ipynb_checkpoints` to gitignore
 - http://nuclearsquid.com/writings/git-tricks-tips-workflows/


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
     + ~/miniconda*
 - Empty trash



