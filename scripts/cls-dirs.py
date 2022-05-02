# Python 3
# Iterates over directories and changes folder names to lowercase and '-' and separator. root dir is where this script is placed

import os

path = os.getcwd()


def scan_dir(dir: str):
    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        if os.path.isdir(f):
            g = os.path.join(dir, filename.lower()).replace(
                '_', '-').replace(' ', '_')
            os.rename(f, g)
            print(g)
            scan_dir(g)


scan_dir(path)
