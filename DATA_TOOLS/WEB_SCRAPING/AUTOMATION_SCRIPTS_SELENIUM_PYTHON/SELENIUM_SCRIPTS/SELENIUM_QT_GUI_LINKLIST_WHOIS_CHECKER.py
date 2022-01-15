#!/usr/bin/env python3

#sudo apt update && sudo apt upgrade
#sudo apt install -y unzip xvfb libxi6 libgconf-2-4
#pip install selenium
#wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
#unzip chromedriver_linux64.zip
#sudo mv chromedriver /usr/bin/chromedriver
#sudo chown root:root /usr/bin/chromedriver
#sudo chmod +x /usr/bin/chromedriver

#amass
#https://github.com/OWASP/Amass

#sublist3r
#https://github.com/aboul3la/Sublist3r

#theHarvester
#https://github.com/laramies/theHarvester

### IMPORT LIBRARIES ###import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

import whois
from urllib.parse import urlparse

import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from definitions import DRIVER_PATH

from bs4 import BeautifulSoup as bs

#DRIVER_PATH = "/usr/bin/chromedriver"

### INIT QT ###

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(680, 120))
        self.setWindowTitle("QT GUI LINKLIST WHOIS CHECKER")

        self.LINKLabel = QLabel(self)
        self.LINKLabel.setText("Enter entire link (http://...) :")
        self.LINKInsert = QLineEdit(self)

        self.LINKLabel.move(30, 30)
        self.LINKLabel.resize(330, 20)
        self.LINKInsert.move(330, 25)
        self.LINKInsert.resize(300, 32)

        pybutton = QPushButton("Save all Whois data!", self)
        pybutton.clicked.connect(self.clickMethodRate)
        pybutton.move(330, 60)
        pybutton.resize(300, 32)

### BUTTON CLICK ###

    def clickMethodRate(self):

        entered_LINK = self.LINKInsert.text()
        if entered_LINK:

### CHROME DRIVER OPTIONS ###

            options = Options()
            options.add_argument("--start-maximized")
            options.headless = True

### CHROME DRIVER START ###

            driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)
            driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})
            driver.get(str(entered_LINK))

            time.sleep(2)

### GET PAGE SOURCE ###

            html = driver.page_source
            soup = bs(html, "lxml")

### SAVE STARTLINK WHOIS INFO TO FILE ###

            with open("Whois of target link.txt", "w", encoding="utf-8", errors="replace") as f:
                f.write("Whois of link: " + str(entered_LINK) + "\n\n")
                f.write(str(whois.whois(entered_LINK).text))

### CLEAN DERIVATE LINKS AGAINST REDUNDANCY ###

            parsed = urlparse(entered_LINK)

            def link_cleaner(linkurl):
                if linkurl.__contains__(str(parsed.netloc)):
                    return False
                elif linkurl.__contains__("google.com"):
                    return False
                elif linkurl.__contains__("twitter.com"):
                    return False
                elif linkurl.__contains__("facebook.com"):
                    return False
                elif linkurl.__contains__("youtube.com"):
                    return False
                else:
                    return True

### SAVE EACH DERIVATE LINK'S WHOIS TO FILE ###

            with open("Whois of derivate links.txt", "w", encoding="utf-8", errors="replace") as f:

                links = []
                for link in soup.find_all("a"):
                    linkurl = link.get("href")

### CHECK ALL STRINGS FOR HTTP.* ###

                    if linkurl is not None and linkurl.startswith("http"):

### INVOKE LINK CLEANER ###

                        if link_cleaner(linkurl):

                                w = whois.whois(str(linkurl))
                                f.write("Whois of link: " + str(linkurl) + "\n\n")
                                f.write(w.text)
                                time.sleep(5)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
