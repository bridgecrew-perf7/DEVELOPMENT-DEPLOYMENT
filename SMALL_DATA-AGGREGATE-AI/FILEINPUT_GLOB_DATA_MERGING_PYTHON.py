#manual_stop_words = ['the','and','to','of','was','with','on','in','for','no','name','is','he','or','at','as','one','she','am','you','his','your','were','by','pt','not','her','be','this','are','there','had','date','from','first','an','that','have','but','has','please','which','namepattern','seen','every','fax', 'home', 'telephone', 'given', 'after','also','will', 'un', 'up', 'well', 'time', 'any']
#line = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', "", line)
#line = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', "", line)
#line = re.sub("\d+", "", line)

### IMPORT LIBRARIES ###

import fileinput
import glob

in_filename = glob.glob('/home/mac/Desktop/TOMERGE/*.rtf'
out_filename = '/home/mc/Desktop/RESULT.txt'

with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:
        with open(in_filename) as infile:
            for line in infile:
                outfile.write(line)
