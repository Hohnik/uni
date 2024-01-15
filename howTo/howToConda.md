# How to Conda

## Create environment

```bash
conda create --name <envName> python=<version>;
conda create --name myEnv python=3.9;
```

## Everyday commands

```bash
conda update conda; # Update conda
conda env list;  # List all environments

conda search <packagename>;
conda install <packagename>; # https://docs.anaconda.com/free/anaconda/reference/packages/pkg-docs/

conda activate <env>;
conda deactivate;

```

## Delete environment

```bash
conda env remove --name <envName>;
conda env remove --name myEnv
```
