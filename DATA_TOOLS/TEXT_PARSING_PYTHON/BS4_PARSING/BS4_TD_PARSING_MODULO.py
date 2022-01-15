from bs4 import BeautifulSoup
import csv

with open('./example.html') as f:
    n = 0
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    tds = soup.find_all("td")

with open('example_out.csv', 'a', encoding='utf-8', errors='replace') as f:
    f.write('NAME;ADDRESS;PHONE;WORKPLACE;POSITION\n')

    for td in tds:
        f.write(td.text)
        f.write(";")
        n = n + 1
        if n % 6 == 0:
              f.write("\n")
