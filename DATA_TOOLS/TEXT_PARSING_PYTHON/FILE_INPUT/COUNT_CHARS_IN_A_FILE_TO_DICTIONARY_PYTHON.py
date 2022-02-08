#!/usr/bin/env python3

#
# <search char> <filename>
#

import sys

filename = str(sys.argv[1])

worddict = {}

f = open(filename)

for line in f:
    for word in line.lower().split():
        if word not in worddict:
            worddict[word] = 0
        worddict[word] += 1

print(word, worddict[word])
