#!/usr/bin/env python3

from bs4 import BeautifulSoup

import csv
import io

in_filename = './infile.html'
out_filename = './list_of_links.csv'

content = None
with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:

    content = infile.read()
    soup = BeautifulSoup(content, "html.parser")

    find_table = soup.find_all(class_="siteSearchResults")

    linklist = []
    for table in find_table:
        links = table.find_all(href=True)

        for link in links:
            outfile.write(link.get('href') + "\n")
