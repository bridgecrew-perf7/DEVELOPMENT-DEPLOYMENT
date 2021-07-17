import csv
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

POST_NUM = 9999999

#create CSV file with headers
with open('All_Content.csv', 'w') as f:
    f.write('abc \n')

#start webdriver file
driver = webdriver.Chrome(executable_path=r'C:\bin\chromedriver.exe')


driver.get("https://example.com/")

for n in range(1, POST_NUM):
    content = driver.find_elements_by_id("content")
    with open('All_Content.csv', 'a', encoding='utf-8', errors='replace') as f:

        for k in range(len(content)):
            f.write(content[k].text)
    driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/div[1]/a[1]").click()
    time.sleep(2)
