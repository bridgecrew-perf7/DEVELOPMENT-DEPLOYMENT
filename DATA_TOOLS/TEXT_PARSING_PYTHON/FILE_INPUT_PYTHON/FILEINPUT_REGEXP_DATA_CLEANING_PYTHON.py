#manual_stop_words = ['the','and','to','of','was','with','on','in','for','no','name','is','he','or','at','as','one','she','am','you','his','your','were','by','pt','not','her','be','this','are','there','had','date','from','first','an','that','have','but','has','please','which','namepattern','seen','every','fax', 'home', 'telephone', 'given', 'after','also','will', 'un', 'up', 'well', 'time', 'any']
#line = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', "", line)
#line = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', "", line)
#line = re.sub("\d+", "", line)
#pip install nltk

### IMPORT LIBRARIES ###

import re

in_filename = './IN.csv'
out_filename = './OUT.csv'

with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:
    data = infile.readlines()
    for line in data:
        #        line = re.sub(r";", " ", line)
        line = re.sub(r"\W", " ", line)
        outfile.write(line)
