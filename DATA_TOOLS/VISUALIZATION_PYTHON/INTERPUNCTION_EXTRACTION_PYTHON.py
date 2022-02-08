#!/bin/usr/env python3

import fileinput
import re

in_filename = "./IN.txt"
out_filename = "./OUT.txt"

with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:
    for line in infile.readlines():
        line = re.sub(r"\w", " ", line)
        outfile.write(line)
