#sudo apt update && sudo apt upgrade
#sudo apt install -y unzip xvfb libxi6 libgconf-2-4
#pip install selenium
#wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
#unzip chromedriver_linux64.zip
#sudo mv chromedriver /usr/bin/chromedriver
#sudo chown root:root /usr/bin/chromedriver
#sudo chmod +x /usr/bin/chromedriver

### IMPORT LIBRARIES ###

### IMPORT QT ###
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

### IMPORT SELENIUM WEB DRIVER ###
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

DRIVER_PATH = "/usr/bin/chromedriver"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(700, 110))
        self.setWindowTitle("QT GUI GET LINKS TOOL")

### QLABEL AND QLINE EDIT ###
        self.connectionLabel = QLabel(self)
        self.connectionLabel.setText('Enter full link:')
        self.connection = QLineEdit(self)

        self.connectionLabel.move(30, 30)
        self.connectionLabel.resize(400, 20)
        self.connection.move(400, 25)
        self.connection.resize(250, 32)

### BUTTON GET LINKS ###

        pybutton = QPushButton('Get Links!', self)
        pybutton.clicked.connect(self.clickMethodExtensive)
        pybutton.move(400, 60)
        pybutton.resize(250, 34)

    def clickMethodExtensive(self):

### CALL WEB DRIVER EXTENSIVE ###
        options = Options()
        options.add_argument('--start-maximized')
        options.headless = False
        options.add_argument('disable-gpu')
        options.add_argument('window-size=1200,600')
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        if connection:
            driver.get(str(connection))

### BUTTON CLICK DIALOGUE ###
    def clickMethodDialogue(self):

        target = self.target.text()
        topic = self.topic.text()
        connection = self.connection.text()

### CALL WEB DRIVER DIALOGUE ###
        driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

        if connection:
            driver.get("https://www.twitter.com/search?q=" + "from:" + str(target)
                       + " " + "to:" + str(connection) + " " + "*" + str(topic) + "*")
            driver = webdriver.Chrome(executable_path='C:/bin/chromedriver')
            driver.get("https://www.twitter.com/search?q=" + "from:" + str(connection)
                       + " " + "to:" + str(target) + " " + "*" + str(topic) + "*")
        else:
            print('If Dialogue, then input!')

    def clickMethodExtensive(self):

        def get_links(url):
            response = requests.get(url)
            data = response.text
            soup = BeautifulSoup(data, 'lxml')

            links = []
            for link in soup.find_all('a'):
                link_url = link.get('href')

                if link_url is not None and link_url.startswith('http'):
                    links.append(link_url + ';\n')

                    write_to_file(links)
                    return links

        def write_to_file(links):
            with open('Links.csv', 'a') as f:
                f.writelines(links)

        def get_all_links(url):
            for link in get_links(url):
                get_all_links(link)

        connection = self.connection.text()
        if connection:
            write_to_file([connection])
            get_all_links(connection)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
