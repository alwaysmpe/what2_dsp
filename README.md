# What2 DSP

## Overview

This is a setup based on my personal and
professional workflow. It has several quirks.
There are reasons for them.

This repository contains a package for generating,
analyzing and plotting signals as well
as a notebook to experiment with those
signals.

The main technology in use (don't worry if you don't know what these are but you'll probably hear some of these names a lot in the professional world):

* Some tasks are automated using [Invoke](https://www.pyinvoke.org/)
* The package is configured using [Poetry](https://python-poetry.org/).
* Notebooks are run in [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/).
* The notebook environment is managed using [Docker](https://www.docker.com/).

## Setup

Check out this repo and the associated submodules. With the git cli:
```
git clone --shallow-submodules --recursive https://github.com/alwaysmpe/what2_dsp.git
```
Or see the documentation for your git client of choice.

### Windows

#### Simple

Install Docker desktop. In a command shell,
open the repository directory and run
(first build may take 5-10 minutes):
<!-- docker desktop doesn't correctly resolve dependencies. -->
```
docker buildx bake foundation
docker buildx bake base-notebook
docker buildx bake minimal-notebook
docker buildx bake juwhat
docker compose up
```
Connect to jupyterlab by opening `localhost:8888`
in a browser.

All other instructions assume either linux or wsl.

#### Complex

Some experience/googling required.
Setup WSL, follow the instructions for linux.

### Linux

Install:
* pyenv
* python 3.12
* pipx (`pip install pipx`)
* poetry (`pipx install poetry`)
* invoke (`pipx install invoke`)
* docker (if wsl, install under linux not windows)

## Start/rebuild and restart jupyterlab

run jupyterlab in docker (see below if first build fails):
```
inv up
```

If your first build fails, you're likely not on the latest version of docker
(bake is experimental). Run each target in order:
```
docker buildx bake foundation
docker buildx bake base-notebook
docker buildx bake minimal-notebook
docker buildx bake juwhat
``` 

connect to jupyterlab by opening `localhost:8888`
in a browser.
Open `notebooks/notebook.py` in jupyter then run all cells.

To rebuild docker stack after changes to dockerfile,
run
```
inv up
```

## Run tests

run
```
inv pytest
```

## TODO

* fix spectrogram
* [Sample audio](https://www2.cs.uic.edu/~i101/SoundFiles/)
* load audio
* analyze