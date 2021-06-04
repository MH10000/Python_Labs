# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

path = pathlib.Path('c:/Users/Martin pc/Documents/CodingNomads/Labs/python_fundamentals-master')
path_str = str(path)

for filepath in path.iterdir():
    if filepath.suffix == '.py':
        print(filepath.name)
    else:
        print(f"none found, it's {filepath.name}")