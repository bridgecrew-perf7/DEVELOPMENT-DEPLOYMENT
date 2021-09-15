#sudo apt update && sudo apt upgrade
#sudo apt install -y unzip xvfb libxi6 libgconf-2-4
#pip install selenium
#wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
#unzip chromedriver_linux64.zip
#sudo mv chromedriver /usr/bin/chromedriver
#sudo chown root:root /usr/bin/chromedriver
#sudo chmod +x /usr/bin/chromedriverimport sys

### IMPORT LIBRARIES
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

from selenium import webdriver
import time
import random

DRIVER_PATH = "/usr/bin/chromedriver"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(680, 350))
        self.setWindowTitle("Twitter-Shotgun")

# Handle 1
        self.targetLabel = QLabel(self)
        self.targetLabel.setText('Twitter Handle ohne \"@\": ')
        self.target = QLineEdit(self)

        self.targetLabel.move(30, 20)
        self.targetLabel.resize(400, 20)
        self.target.move(400, 20)
        self.target.resize(250, 32)

# Handle 2
        self.target2Label = QLabel(self)
        self.target2Label.setText('(Optional) Zweites Twitter Handle ohne \"@\": ')
        self.target2 = QLineEdit(self)

        self.target2Label.move(30, 70)
        self.target2Label.resize(400, 20)
        self.target2.move(400, 70)
        self.target2.resize(250, 32)

# Topic 1
        self.topicLabel = QLabel(self)
        self.topicLabel.setText('Stichwort eingeben: ')
        self.topic = QLineEdit(self)

        self.topicLabel.move(30, 120)
        self.topicLabel.resize(400, 20)
        self.topic.move(400, 120)
        self.topic.resize(250, 32)

# Button Search
        pybutton = QPushButton('Stichwort suchen!', self)
        pybutton.clicked.connect(self.clickMethodExtensive)
        pybutton.move(400, 190)
        pybutton.resize(250, 34)

# Button Dialogue
        pybutton = QPushButton('Interaktion suchen! ', self)
        pybutton.clicked.connect(self.clickMethodDialogue)
        pybutton.move(400, 240)
        pybutton.resize(250, 34)

# Button Extensive
    def clickMethodExtensive(self):
        target = self.target.text()
        topic = self.topic.text()

        driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        hattrick = random.randint(0,5)

        if topic:
            if target:
                time.sleep(4)
                driver.get("https://www.twitter.com/search?q=" + "from:" + str(target) + " " + str(topic) + " " + "OR" + " " + "to:" + str(target) + " " + str(topic))

# Button Dialogue
    def clickMethodDialogue(self):

        target = self.target.text()
        topic = self.topic.text()
        target2 = self.target2.text()

        driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        if target2:
            if target:
                time.sleep(4)
                driver.get("https://www.twitter.com/search?q=" + "from:" + str(target) + " " + "to:" + str(target2))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
