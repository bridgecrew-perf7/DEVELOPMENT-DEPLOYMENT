import sys
import fileinput
import csv
import re

in_filename = '/home/mac/Desktop/PD-LA/WW.csv'
out_filename = '/home/mac/Desktop/PD-LA/WWout.csv'

with open(in_filename) as infile, open(out_filename, "w") as outfile:
    for line in infile.readlines():
        line = re.sub(r";;", ";", line)
        outfile.write(line)
