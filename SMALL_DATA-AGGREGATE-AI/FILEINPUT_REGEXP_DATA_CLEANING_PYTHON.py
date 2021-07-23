#adjust regexps to input data

import fileinput
import re

in_filename = '/home/mac/Desktop/DATA-AGGREGATE-AI/IN.csv'
out_filename = '/home/mac/Desktop/DATA-AGGREGATE-AI/OUT.csv'

with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:
    for line in infile.readlines():
#        line = re.sub(r";", " ", line)
        line = re.sub(r"\W", " ", line)
        outfile.write(line)
