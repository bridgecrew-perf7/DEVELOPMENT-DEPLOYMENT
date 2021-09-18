#sudo apt update && sudo apt upgrade
#sudo apt install -y unzip xvfb libxi6 libgconf-2-4
#pip install selenium
#wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
#unzip chromedriver_linux64.zip
#sudo mv chromedriver /usr/bin/chromedriver
#sudo chown root:root /usr/bin/chromedriver
#sudo chmod +x /usr/bin/chromedriver

### IMPORT LIBRARIES ###

import csv
from selenium import webdriver
import time

p = 0

#from definitions import DRIVER_PATH
DRIVER_PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


with open('FILE.csv', 'w') as f:
    f.write('ID;NAME;POSITION;INFO\n')

page_num = 56

for n in range(-1, page_num ):
    url = "https://example" + str(page_num) + "/page/query.com"
    page_num = page_num - 1

    driver.get(url)
    content = driver.find_elements_by_tag_name("td")
    with open('FILE.csv', 'a', encoding='utf-8', errors='replace') as f:

        for k in range(len(content)):
            f.write(content[k].text + ";")
            p = p + 1
            if p % 4 == 0:
               f.write("\n")

    time.sleep(1)
driver.close()
