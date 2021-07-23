#optional: manual_stop_words = ['the','and','to','of','was','with','on','in','for','no','name','is','he','or','at','as','one','she','am','you','his','your','were','by','pt','not','her','be','this','are','there','had','date','from','first','an','that','have','but','has','please','which','namepattern','seen','every','fax', 'home', 'telephone', 'given', 'after','also','will', 'un', 'up', 'well', 'time', 'any']

#### IMPORT LIBRARIES ####

import fileinput
import re


in_filename = '/home/mac/Desktop/PANDAS-ML/IN.csv'
out_filename = '/home/mac/Desktop/PANDAS-ML/OUT.csv'

with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:
    for line in infile.readlines():
        line = re.sub(r";", " ", line)
        outfile.write(line)
