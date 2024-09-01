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

### Simple

Install Docker. In a command shell,
open the repository directory and run
(first build may take 5-10 minutes):
```
docker buildx bake
docker compose up
```
Connect to jupyterlab by opening `localhost:8888`
in a browser.
Open `notebooks/notebook.py` in jupyter then run all cells.

### Windows

Some experience/googling required.
Setup WSL, follow the instructions for linux.

### Linux

Install:
* pyenv
* python 3.12
* pipx (`pip install pipx`)
* poetry (`pipx install poetry`)
* invoke (`pipx install invoke`)
* docker

## Start/rebuild and restart jupyterlab

run jupyterlab in docker:
```
inv up
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

* fix autoreload?
* fix spectrogram
* [Sample audio](https://www2.cs.uic.edu/~i101/SoundFiles/)
* load audio
* analyze
