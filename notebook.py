import importlib.metadata as met
met.distributions()
for pk in met.distributions():
    if pk.name.startswith("what"):
        print(pk)
        print(dir(pk))
        print(pk._path)
# %pip install -e /notebooks/


