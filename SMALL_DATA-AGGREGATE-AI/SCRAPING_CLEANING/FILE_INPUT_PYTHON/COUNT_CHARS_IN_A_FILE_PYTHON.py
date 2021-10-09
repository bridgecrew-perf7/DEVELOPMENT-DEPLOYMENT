#!/usr/bin/env python3

#
# <search char> <filename>
#

import sys

sChar = sys.argv[1]
filename = sys.argv[2]

fh = open(filename)

counter = 0
for line in fh:
    for ch in line:
        if ch == sChar:
            counter += 1

print(counter)
