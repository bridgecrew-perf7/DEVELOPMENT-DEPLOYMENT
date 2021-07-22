#optional manual_stop_words = ['the','and','to','of','was','with','on','in','for','no','name','is','he','or','at','as','one','she','am','you','his','your','were','by','pt','not','her','be','this','are','there','had','date','from','first','an','that','have','but','has','please','which','namepattern','seen','every','fax', 'home', 'telephone', 'given', 'after','also','will', 'un', 'up', 'well', 'time', 'any']

import fileinput
import re
import io
import nltk

#nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

in_filename = '/home/mac/Desktop/PANDAS-ML/IN.csv'
out_filename = '/home/mac/Desktop/PANDAS-ML/OUT.csv'

stop_words = set(stopwords.words('english'))

infile = open(in_filename, "r")

line = infile.read()
words = line.split(";")
for r in words:
    if not r in stop_words:
        outfile = open(out_filename,"a")
        outfile.write(";"+r)
