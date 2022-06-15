# Python 3
# Iterates over directories and changes folder names to lowercase and '-' and separator. root dir is where this script is placed
# dir: "Hello_WOrld" -> "hello-world"

import os
import re

path = os.getcwd()

def scan_dir(dir: str):
    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        
        if os.path.isdir(f):
            if(filename.startswith(".")):
                continue
            g = re.sub("[_]", "-", f.lower())
            try:
                os.rename(f, g)
                print(f"{filename} ----> {g}")
                scan_dir(g)

            # If source is a file
            # but destination is a file
            except IsADirectoryError:
                print("Source is a file but destination is a directory.")
            
            # If source is a directory
            # but destination is a file
            except NotADirectoryError:
                print("Source is a directory but destination is a file.")
            
            # For permission related errors
            except PermissionError:
                print("Operation not permitted.")
            
            # For other errors
            except OSError as error:
                print(error)

scan_dir(path)