from bs4 import BeautifulSoup as bs
from csv import reader
import pandas as pd

f = open("./INPUT.html", "r")
html = f.read()

s = bs(html, "html.parser")
tds = s.find_all("td")

data = ""
n = 0

for td in tds:
    f.write(td.text)
    f.write(";")
    n = n + 1
    if n % 6 == 0:
        f.write("\n")
