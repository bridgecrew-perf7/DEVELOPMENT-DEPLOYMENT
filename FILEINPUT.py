import sys
import fileinput
import csv
import re

in_filename = '/home/mac/Desktop/PD-LA/MM.csv'
out_filename = '/home/mac/Desktop/PD-LA/MMout.csv'

with open(in_filename) as infile, open(out_filename, "w") as outfile:
    for line in infile.readlines():
        line = re.sub(r"(\n)|(\s)|(W)", "", line)
        outfile.write(line)
