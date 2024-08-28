import subprocess

installed = subprocess.run(
    "pip list | grep /notebook"
    shell=True,
)

if len(installed.stdout) == 0:
    %pip install -e /notebooks
