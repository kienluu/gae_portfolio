#!/usr/bin/env python
import optparse
import os
import re

def main():
    p = optparse.OptionParser()
    options, arguments = p.parse_args()
    package_root = arguments[0]
    mod = __import__(package_root)
    mod_path = mod.__file__
    package_folder_re = re.compile(
        r'[/\\]__init__\.py[co]?$', flags=re.IGNORECASE)
    if package_folder_re.search(mod_path):
        print os.path.dirname(mod_path)
        exit(0)
    exit(1)

if __name__ == '__main__':
    main()
