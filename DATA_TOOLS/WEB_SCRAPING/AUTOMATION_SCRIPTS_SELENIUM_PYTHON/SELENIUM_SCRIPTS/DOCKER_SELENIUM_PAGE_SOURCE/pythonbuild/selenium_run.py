#!/usr/bin/env python3

import os
import subprocess
import random
import string
import shutil
import time
import sys
import traceback

import csv

from enum import Enum
from typing import List, Dict, Union
from pathlib import Path


# selenium grid imports

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import InvalidSessionIdException

from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

from util import get_random_ua, random_wait


# import selenium stealth
from selenium_stealth import stealth


# xpaths constants
BUTTON_CONSENT = '//*[@id="CybotCookiebotDialogBodyButtonAccept"]'


def handle_cookie_consent_popup(driver):

    wait = WebDriverWait(driver, 10)

    try:
        random_wait(1, 1)
        button_consent = wait.until(ec.visibility_of_element_located((By.XPATH, BUTTON_CONSENT)))
        random_wait(1, 2)
        button_consent.click()

    except Exception as e:
        print(traceback.format_exc())
        print(str(e))
        print("Error Exception - after handle_cookie_consent_popup")


def click_next(driver):

    wait = WebDriverWait(driver, 10)

    try:
        random_wait(1, 2)
        button_next = wait.until(ec.visibility_of_element_located((By.XPATH, BUTTON_NEXT)))
        random_wait(1, 2)
        button_next.click()

    except Exception as e:
        print(traceback.format_exc())
        print(str(e))
        print("Error Exception - after click_next")


def Selenium_Run(driver, URL):

    # get link first time for cookie consent
    driver.get(URL)
    random_wait(3, 5)
    handle_cookie_consent_popup(driver)
    random_wait(3, 5)

    with open('./This.csv', 'a', encoding='utf-8', errors='replace') as f:

        try:
            page_num = 1000
            for n in range(-1, page_num):
                url = "https://example.com/this?page=" + str(page_num)
                page_num = page_num - 1

                driver.get(url)

                # save running url
                time.sleep(1)
                running_url = driver.current_url
                time.sleep(1)

                print("PAGE_SOURCE_OF_URL: \n")
                print(running_url)

                f.write("PAGE_SOURCE_OF_URL: \n")
                f.write(running_url)
                f.write("\n")

                # save page source
                time.sleep(1)
                page_source = driver.page_source
                time.sleep(1)

                print(page_source)
                f.write(page_source)

                random_wait(11,22)


        except Exception as e:
            print(traceback.format_exc())
            print(str(e))
            print("Error Exception - after Selenium_Run")

            #launch lte reconnect
            #Selenium_Run(driver, running_url)
            #time.sleep(60)

        finally:
            driver.quit()


def main():

    desiredCapabilities={
    "browserName": "chrome",
    "platform": "ANY"}

    options = ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--disable-extensions')
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--whitelisted-ips=''")
    options.add_argument(f'--user-agent="{get_random_ua()}"')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

#    driver = webdriver.Remote(command_executor="http://chrome:4444/wd/hub", desired_capabilities=desiredCapabilities, options=options)
    driver = webdriver.Chrome(executable_path="./chromedriver")

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    # sudo docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:4.1.0-prerelease-20211105
    #http://172.17.0.2:4444
    #http://172.24.0.2:4444

    try:
        Selenium_Run(driver, URL)

    except Exception as e:
        print(traceback.format_exc())
        print(str(e))
        print("Error Exception after main")

        #launch lte reconnect
        #Selenium_Run(driver, running_url)
        #time.sleep(60)

if __name__ == "__main__":
    main()
