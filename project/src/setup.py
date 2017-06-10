import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["requests", "queue", "bs4"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "cHelper",
        version = "0.0.1",
        description = "cHelper install test",
        options = {"build_exe": build_exe_options},
        executables = [Executable("__init__.py", base=base)])