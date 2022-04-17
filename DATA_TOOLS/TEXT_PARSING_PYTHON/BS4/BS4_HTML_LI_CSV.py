from bs4 import BeautifulSoup

from itertools import zip_longest

import csv
import re
import io

in_filename = './input.html'
out_filename = './output.csv'


content = None
with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:

    content = infile.read()
    soup = BeautifulSoup(content, "html.parser")

    name = []
    address = []
    out = []
    url = []

    # 1. find all, 2. find all, 3. if in str: 4. find, 5. .text / .get(''), 6. append 7. zip_longest itertools
    class_soup = soup.find_all(class_="details details_two_columns")

    for each_class_element in class_soup:
        li_element_soup = BeautifulSoup(str(each_class_element), "html.parser")
        li_element_soup = li_element_soup.find_all('li')

        # name
        for li_element in li_element_soup:

            if "Name:" in str(li_element):

                span = li_element.find("span")

                if span is not None:
                    name.append(span.text.strip())
                else:
                    name.append("")
                print(name)

        # address
        for li_element in li_element_soup:

            if "Address:" in str(li_element):

                span = li_element.find("span")

                if span is not None:
                    address.append(span.text.strip())
                else:
                    address.append("")
                print(age)


        # url
        for li_element in li_element_soup:

            if "Homepage:" in str(li_element):

                hrefs = li_element.find_all('a')
                for href in hrefs:
                    domain = href.get('href')

                    if domain is not None:
                        url.append(domain)
                    else:
                        url.append("")


    data = [name, age, url]
    export_data = zip_longest(*data, fillvalue = '')

    write = csv.writer(outfile, delimiter=';')
    write.writerow(("Name", "Address", "Url"))
    write.writerows(export_data)
