#!/usr/bin/env python3

string_linecount = 0
full_linecount = 0

in_filename = 'demo.log'
out_filename = 'outlines.txt'

with open(in_filename, "r", encoding="cp1252") as infile, open(out_filename, "w") as outfile:
    data = infile.readlines()
    for line in data:
        full_linecount += 1

        if "(TBCB)" in line:
            outfile.write(line)
            string_linecount += 1
    print(full_linecount)
    print(string_linecount)
