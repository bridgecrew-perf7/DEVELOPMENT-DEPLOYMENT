### IMPORT LIBRARIES ###

from bs4 import BeautifulSoup
import csv

with open('ALL_TDS.csv', 'w') as f:
    f.write('NAME;ADDRESS;PHONE;WORKPLACE;POSITION;\n')

with open('/home/mac/Desktop/INPUT.html') as f:
    n = 1
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    tds = soup.find_all("td")
    for td in tds:
        with open('ALL_TDS.csv', 'a', encoding='utf-8', errors='replace') as f:
            f.write(td.text)
            f.write(";")
            n = n + 1
            if n % 5 == 0:
               f.write("\n")
