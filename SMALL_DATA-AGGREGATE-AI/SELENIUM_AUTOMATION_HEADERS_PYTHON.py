#sudo apt update && sudo apt upgrade
#sudo apt install -y unzip xvfb libxi6 libgconf-2-4
#wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
#unzip chromedriver_linux64.zip
#sudo mv chromedriver /usr/bin/chromedriver
#sudo chown root:root /usr/bin/chromedriver
#sudo chmod +x /usr/bin/chromedriver

import csv
from selenium import webdriver

DRIVER_PATH = "/usr/bin/chromedriver"

MAX_PAGE_NUM = 387
MAX_PAGE_DIG = 3

#create CSV file with headers
with open('Headers_and_Dates.csv', 'w') as f:
    f.write('Headers; Date \n')

#start webdriver file
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#loop through all pages defined in MAX_PAGE_NUM
for n in range(1, MAX_PAGE_NUM + 1):
    page_num = (MAX_PAGE_DIG - len(str(n))) * '0' + str(n)
    url = "https://www.example.com/page/" + page_num

    driver.get(url)

    titles = driver.find_elements_by_tag_name("h3")
    dates = driver.find_elements_by_css_selector(".shadowedHeader")

    with open('Headers_and_Dates.csv', 'a', encoding='utf-8', errors='replace') as f:
        for k in range(len(dates)):
            f.write(titles[k].text + "; " + dates[k].text + "\n")

driver.close()
