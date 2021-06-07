import itertools

import csv
import nltk
import sys
import fileinput

from nltk.corpus import stopwords
stop = stopwords.words('english')
csv.field_size_limit(sys.maxsize)


in_filename = '/home/mac/Desktop/PD-LA/SW.csv'
out_filename = '/home/mac/Desktop/PD-LA/SWout.csv'
