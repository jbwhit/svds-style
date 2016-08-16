# svds-style

## Setting up your laptop for SVDS style

```bash
git clone git@github.com:jbwhit/svds-style.git
cd svds-style


# source activate whatever jupyter environment you use for svds
jupyter notebook --generate-config
mkdir -p ~/.jupyter/custom
ln -s ${PWD}/css/jupyter/custom.css ~/.jupyter/custom/custom.css
```

## What have you just done?

You just placed a `custom.css` file in your `~/.jupyter/custom` directory. This makes all of your notebooks follow the SVDS style -- but you haven't finished yet! 


