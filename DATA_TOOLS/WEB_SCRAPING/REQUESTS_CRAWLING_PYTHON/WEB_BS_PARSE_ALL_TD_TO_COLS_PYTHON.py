#pip install bs4

### IMPORT LIBRARIES ###

from bs4 import BeautifulSoup
import csv

with open('./INPUT.html') as f:
    n = 0
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    tds = soup.find_all("td")

with open('ALL_TDS.csv', 'a', encoding='utf-8', errors='replace') as f:
    f.write('NAME;ADDRESS;PHONE;WORKPLACE;POSITION;ADDITIONAL\n')

    for td in tds:
        f.write(td.text)
        f.write(";")
        n = n + 1
        if n % 6 == 0:
              f.write("\n")
