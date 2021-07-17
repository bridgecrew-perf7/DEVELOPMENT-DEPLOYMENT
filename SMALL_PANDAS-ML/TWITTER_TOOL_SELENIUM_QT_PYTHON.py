#### IMPORT LIBRARIES ###

#### IMPORT QT ####
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

#### IMPORT SELENIUM WEB DRIVER #####

from selenium import webdriver
import time

### SET SELENIUM WEB DRIVER OPTIONS ####

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(680, 300))
        self.setWindowTitle("TOTH MANUAL PRINT")

#### TOPIC QLABEL AND QLINE EDIT ####
        self.targetLabel = QLabel(self)
        self.targetLabel.setText('Enter Twitter Target Handle without \"@\": ')
        self.target = QLineEdit(self)

        self.targetLabel.move(30, 30)
        self.targetLabel.resize(400, 20)
        self.target.move(400, 25)
        self.target.resize(250, 32)

#### TOPIC QLABEL AND QLINE EDIT ####
        self.topicLabel = QLabel(self)
        self.topicLabel.setText('(Optional) Enter Topic: ')
        self.topic = QLineEdit(self)

        self.topicLabel.move(30, 73)
        self.topicLabel.resize(400, 20)
        self.topic.move(400, 68)
        self.topic.resize(250, 32)

#### CONNECTION QLABEL AND QLINE EDIT ####
        self.connectionLabel = QLabel(self)
        self.connectionLabel.setText('(Optional) Enter Second Twitter Target Handle without \"@\": ')
        self.connection = QLineEdit(self)

        self.connectionLabel.move(30, 114)
        self.connectionLabel.resize(400, 20)
        self.connection.move(400, 110)
        self.connection.resize(250, 32)

#### BUTTON EXTENSIVE SEARCH ####

        pybutton = QPushButton('Extensive Search!', self)
        pybutton.clicked.connect(self.clickMethodExtensive)
        pybutton.move(400, 180)
        pybutton.resize(250, 34)

#### BUTTON SEARCH DIALOGUE ####
        pybutton = QPushButton('Find Interaction! (2 Windows)', self)
        pybutton.clicked.connect(self.clickMethodDialogue)
        pybutton.move(400, 220)
        pybutton.resize(250, 34)

#### BUTTON CLICK EXTENSIVE ####

    def clickMethodExtensive(self):
        target = self.target.text()
        topic = self.topic.text()
        connection = self.connection.text()

#### CALL WEB DRIVER EXTENSIVE ####
        driver = webdriver.Chrome(executable_path='C:/bin/chromedriver')

        if connection:
            driver.get("https://www.twitter.com/search?q=" + "from:" + str(target) + " " + "OR" + " " + "to:" + str(target) + " " + "*" + str(topic) + "*" +  " " + "OR" + " " +  "from:" + str(connection) + " " + "OR" + " " + "to:" + str(connection))
        else:
            driver.get("https://www.twitter.com/search?q=" + "from:" + str(target) + " " + "OR" + " " + "to:" + str(target) + " " + "*" + str(topic) + "*")

#### BUTTON CLICK DIALOGUE ####
    def clickMethodDialogue(self):

        target = self.target.text()
        topic = self.topic.text()
        connection = self.connection.text()

#### CALL WEB DRIVER DIALOGUE ####
        driver = webdriver.Chrome(executable_path='C:/bin/chromedriver')

        if connection:
            driver.get("https://www.twitter.com/search?q=" + "from:" + str(target) + " " + "to:" + str(connection) + " " + "*" + str(topic) + "*")
            driver = webdriver.Chrome(executable_path='C:/bin/chromedriver')
            driver.get("https://www.twitter.com/search?q=" + "from:" + str(connection) + " " + "to:" + str(target) + " " + "*" + str(topic) + "*")
        else:
            print('If Dialogue, then input!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
