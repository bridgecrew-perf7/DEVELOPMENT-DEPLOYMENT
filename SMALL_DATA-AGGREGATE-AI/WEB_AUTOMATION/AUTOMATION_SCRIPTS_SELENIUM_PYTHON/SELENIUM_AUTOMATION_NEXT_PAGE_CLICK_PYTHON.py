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
from selenium.webdriver.common.keys import Keys
import time

#from definitions import DRIVER_PATH
DRIVER_PATH = "/usr/bin/chromedriver"
POST_NUM = 9999999

### CREATE CSV ###
with open('All_Content.csv', 'w') as f:
    f.write('All_Content_: \n')

### START WEB DRIVER ###
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
driver.get("https://example.com/")

for n in range(1, POST_NUM):
    content = driver.find_elements_by_id("content")
    with open('All_Content.csv', 'a', encoding='utf-8', errors='replace') as f:

        for k in range(len(content)):
            f.write(content[k].text)
    driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div[1]/a[1]").click()
    time.sleep(2)
driver.close()
