import fileinput
import glob

in_filename = glob.glob('/home/mac/Desktop/TOMERGE/*.rtf'
out_filename = '/home/mc/Desktop/RESULT.txt'

with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:
        with open(in_filename) as infile:
            for line in infile:
                outfile.write(line)
