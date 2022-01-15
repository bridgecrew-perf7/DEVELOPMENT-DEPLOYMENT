

import csv
from bs4 import BeautifulSoup


with open('./example.html', 'r') as toparse:
	htmlcontent = toparse.read()
	soup = BeautifulSoup(htmlcontent, 'html.parser')

with open('extracted.csv', 'w', encoding='utf-8', newline='') as csvfile:
	contentwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	contentwriter.writerow(['NAME','ADDRESS','PHONE','WORKPLACE','POSITION'])

	for row in soup.select("tbody tr"):
		name = row.select("td")[0].getText()
		address = row.select("td")[1].getText()
		phone = row.select("td")[2].getText()
		workplace = row.select("td")[3].getText()
		position = row.select("td")[4].getText()
		additional = row.select("td")[5].getText()

		contentwriter.writerow([name, address, phone, workplace, position])
