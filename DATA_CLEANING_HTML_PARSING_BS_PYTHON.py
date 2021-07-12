# wget -m -k -K -e robots=off -E -l 7 -t 6 -w 1 --max-redirect 0 http://www.example-site.com/
# --accept-regex urlregex
# wget -m -k -K -l 10 -w 1 -A .jpg,png,gif,mp3,pfd,docx,doc,csv http://www.example-site.com/

import fileinput
import re
import glob
from bs4 import BeautifulSoup

in_filename = glob.glob('/home/mac/Desktop/TOPARSE/*.html'
out_filename = '/home/mac/Desktop/PANDAS-ML/OUT.csv'

with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:
    for fi in infile:
        with open(fi) as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            print(soup.title)
            outfile.write(line)

parsed_html = BeautifulSoup(html)
print(parsed_html.body.find('div', attrs={'class':'container'}).text)
