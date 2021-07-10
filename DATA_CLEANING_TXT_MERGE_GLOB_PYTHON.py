#merge(convert(files))

import fileinput
import glob

out_filename = '/home/mac/Desktop/RESULT.txt'

with open(out_filename, "w") as outfile:
    for filename in glob.glob('/home/mac/Desktop/TOMERGE/*.rtf'):
        with open(filename) as infile:
            for line in infile:
                outfile.write(line)
        outfile.write("\n\n")
