FROM quay.io/jupyter/minimal-notebook

USER root

RUN apt-get update --yes && \
    apt-get upgrade --yes && \
    apt-get install --yes --no-install-recommends \
    'p7zip-full' \
    'libzmq3-dev' \
    'build-essential' \
    'file'

USER ${NB_UID}

RUN mamba update --all -y

RUN mamba install --quiet --yes \
    'sympy' \
    'matplotlib' \
    'plotly' \
    'altair' \
    'jupytext' \
    'python-graphviz' \
    'pyzmq' \
    'scikit-learn' \
    'pydeck' \
    'pytest' \
    'pytest-order' \
    'pandas' \
    'numpy' \
    'altair' \
    'pyright' \
    'pydocstyle' \
    'pylama[toml]' \
    'pytest-lazy-fixture' \
    'mypy' \
    'pandas-stubs' \
    'pandera' \
    'flake8' \
    'pyright'

RUN mamba update --all -y

USER root

# Dev only
RUN echo "jovyan ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/jovyan

USER ${NB_UID}

COPY ./jupyter_docmanager_settings.json .jupyter/lab/user-settings/@jupyterlab/docmanager-extension/plugin.jupyterlab-settings 
COPY ./jupyter_notebook_config.json .jupyter/jupyter_notebook_config.json
COPY ./20install-notebook-pkg.sh /usr/local/bin/before-notebook.d/

USER root
RUN fix-permissions "${HOME}"
USER ${NB_UID}

WORKDIR /notebooks/
