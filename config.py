import os
from pathlib import Path

_base_dir = os.path.abspath(os.path.dirname(__file__))
_base_dir_pathlib = Path(_base_dir)

def prRed(skk):
    print("\033[91m{}\033[00m".format(skk))


def prGreen(skk):
    print("\033[92m{}\033[00m".format(skk))
