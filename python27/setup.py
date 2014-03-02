import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

setup(  name = "LOTF Text Adventure",
        version = "1.7.0",
        description = "Lord of the Flies Text Adventure",
        options = {'build_exe': {'icon':'icon.ico'}},
        executables = [Executable("Lord of the Flies.py", base=base)])