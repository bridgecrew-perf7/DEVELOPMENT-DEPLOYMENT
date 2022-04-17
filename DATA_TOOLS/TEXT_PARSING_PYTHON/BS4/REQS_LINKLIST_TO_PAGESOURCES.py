#!/usr/bin/env python3

from bs4 import BeautifulSoup

import time
import csv
import io
import requests
import datetime
import traceback

def main():

    try:

        url = ""
        in_filename = './links.csv'
        out_filename = './html.html'

        content = None
        with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:

            links = infile
            for url in links:
                page = requests.get(url)

                outfile.write(f"START OF REQUEST OF URL: {url} \n {requests.get(url).text} \n END OF REQUEST OF URL: {url}")
                time.sleep(3)

    except Exception as e:
        print(traceback.format_exc())
        print(str(e))
        print("stopped at" + url)

if __name__ == "__main__":
    main()
