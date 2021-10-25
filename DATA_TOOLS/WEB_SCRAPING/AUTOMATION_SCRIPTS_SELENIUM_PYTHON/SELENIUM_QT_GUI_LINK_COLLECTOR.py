#sudo apt update && sudo apt upgrade
#sudo apt install -y unzip xvfb libxi6 libgconf-2-4
#pip install selenium
#wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
#unzip chromedriver_linux64.zip
#sudo mv chromedriver /usr/bin/chromedriver
#sudo chown root:root /usr/bin/chromedriver
#sudo chmod +x /usr/bin/chromedriver

### IMPORT LIBRARIES ###

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from definitions import DRIVER_PATH

from bs4 import BeautifulSoup as bs

#DRIVER_PATH = "/usr/bin/chromedriver"

### INIT QT WINDOW ###

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(680, 120))
        self.setWindowTitle("QT GUI LINK COLLECTOR")

        self.LINKLabel = QLabel(self)
        self.LINKLabel.setText("Full Link from Web Page: ")
        self.LINKInsert = QLineEdit(self)

        self.LINKLabel.move(30, 30)
        self.LINKLabel.resize(400, 20)
        self.LINKInsert.move(250, 25)
        self.LINKInsert.resize(400, 32)

        pybutton = QPushButton("Save Links to CSV!", self)
        pybutton.clicked.connect(self.clickMethodRate)
        pybutton.move(250, 60)
        pybutton.resize(400, 34)

### QT BUTTON ###

    def clickMethodRate(self):

        entered_LINK = self.LINKInsert.text()
        if entered_LINK:

### DRIVER OPTIONS ###

            options = Options()
            options.add_argument('--start-maximized')
            options.headless = True

### DRIVER START ###

            driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)
            driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
            driver.get(str(entered_LINK))

            time.sleep(2)

### EXTRACT PAGE SOURCE AND PARSE LINKS ###

            html = driver.page_source
            soup = bs(html, "lxml")

            links = []
            for link in soup.find_all("a"):
                linkurl = link.get("href")

                if linkurl is not None and linkurl.startswith('http'):
                    links.append(linkurl + '\n')

### WRITE TO FILE ###

            with open("LINKS.csv", "w", encoding="utf-8", errors="replace") as f:
                f.writelines(links)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
