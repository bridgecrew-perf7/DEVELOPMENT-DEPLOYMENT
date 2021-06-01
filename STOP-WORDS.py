import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import itertools
import umap
import sklearn

import csv
import nltk
import sys
import fileinput
import re

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

in_filename = '/home/mac/Desktop/PD-LA/SW.csv'
out_filename = '/home/mac/Desktop/PD-LA/SWout.csv'

with open(in_filename, newline=';') as infile, open(out_filename, "w") as outfile:
    for line in infile.readlines():
        if not line in stop_words:
            outfile.write(line)
