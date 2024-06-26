# shepard
a collection of tools for NWN EE development designed for the Echoes of War persistent world

# requirements

Python 3

# installation

``` pip install . ```

# usage

``` shepard --help ```

# dev testing
windows
```
python -m venv .venv
.\.venv\Scripts\activate
pip install --editable .
```

linux or mac
```
python -m venv .venv
.venv/bin/activate
pip install --editable .
```

# baked in dependencies

The lib/data/ folder is from the nwserver 8193.36-12

The lib/ tools are from 
* https://github.com/nwneetools/nwnsc
* https://github.com/niv/neverwinter.nim