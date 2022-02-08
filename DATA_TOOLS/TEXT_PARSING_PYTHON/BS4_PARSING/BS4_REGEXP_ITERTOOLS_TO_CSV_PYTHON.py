#!/usr/bin/env python3

from bs4 import BeautifulSoup

from itertools import zip_longest
import csv
import io
from urllib.parse import urlparse

import re


# infile outfile
in_filename = './Example.csv'
out_filename = './Example_Out_Parsed.csv'

content = None

names = ()
budgets = ()
hourlyrates = ()
employeecounts = ()
ratings = ()
taglines = ()
locations = ()
domains = ()



with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:

    content = infile.read()
    soup = BeautifulSoup(content, "html.parser")


    # names
    for name in soup.find_all(class_=""):
        name = re.sub(r"\s", "", str(name))

        name_soup = BeautifulSoup(name, "html.parser")
        name = name_soup.text


        names = names + (name, )


    # budgets
    for budget in soup.find_all(class_=""):
        budget = re.sub(r"\s", "", str(budget))

        budget_soup = BeautifulSoup(budget, "html.parser")
        budget = budget_soup.text

        budgets = budgets + (budget, )



    # hourlyrates
    for hourlyrate in soup.find_all(class_=""):
        hourlyrate = re.sub(r"\s", "", str(hourlyrate))
        hourlyrate = re.sub(r",", ".", str(hourlyrate))

        hourlyrate_soup = BeautifulSoup(hourlyrate, "html.parser")
        hourlyrate = hourlyrate_soup.text

        hourlyrates = hourlyrates + (hourlyrate, )


    # employeecounts
    for employeecount in soup.find_all(class_=""):
        employeecount = re.sub(r"\s", "", str(employeecount))

        employeecount_soup = BeautifulSoup(employeecount, "html.parser")
        employeecount = employeecount_soup.text

        employeecounts = employeecounts + (budget, )


    # ratings
    for rating in soup.find_all(class_=""):
        rating = re.sub(r"\s", "", str(rating))

        rating_soup = BeautifulSoup(rating, "html.parser")
        rating = rating_soup.text

        ratings = ratings + (rating, )


    # taglines
    for tagline in soup.find_all(class_=""):
#        tagline = re.sub(r"\s", "", str(tagline))

        tagline_soup = BeautifulSoup(str(tagline), "html.parser")
        tagline = tagline_soup.text

        taglines = taglines + (tagline, )


    # locations
    for location in soup.find_all(class_=""):
        location = re.sub(r"\s", "", str(location))

        location_soup = BeautifulSoup(location, "html.parser")
        location = location_soup.text

        locations = locations + (location, )


    # domains
    for domain in soup.find_all(class_=""):
        domain = re.sub(r"\s", "", str(domain))

        domain_soup = BeautifulSoup(domain, "html.parser")
        domain_full = domain_soup.text

        parsed = urlparse(domain_full)
        domain = str(parsed.netloc)

        domains = domains + (domain, )



    data = [names, budgets, hourlyrates, employeecounts, ratings, taglines, locations, domains]
    export_data = zip_longest(*data, fillvalue = '')

    write = csv.writer(outfile, delimiter=';')
    write.writerow(("names", "budgets", "hourlyrates", "employeecounts", "ratings", "taglines", "locations", "domains"))
    write.writerows(export_data)
