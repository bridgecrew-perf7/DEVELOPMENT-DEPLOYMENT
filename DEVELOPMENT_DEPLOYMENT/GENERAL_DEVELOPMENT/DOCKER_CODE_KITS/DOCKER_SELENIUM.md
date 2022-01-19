```
from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

def Selenium_Chrome_Launch():

    desiredCapabilities={
    "browserName": "chrome",
    "platform": "ANY",
    }

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

    # sudo docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:4.1.0-prerelease-20211105
    #http://172.17.0.2:4444
    #http://172.24.0.2:4444
    
    driver = webdriver.Remote(command_executor="http://chrome:4444/wd/hub", desired_capabilities=desiredCapabilities, options=options)

    #driver = driver = webdriver.Chrome(executable_path="./chromedriver")

    #stealth(driver,
     #       languages=["en-US", "en"],
      #      vendor="Google Inc.",
       #     platform="Win32",
        #    webgl_vendor="Intel Inc.",
         #   renderer="Intel Iris OpenGL Engine",
          #  fix_hairline=True,
           # )
```
```
version: "3"
services:

  chrome:
    image: selenium/standalone-chrome
    hostname: chrome
    shm_size: 2g
    ports:
      - "7900:7900"
      - "4444:4444"
    restart: unless-stopped

  webdecreate:
    build: "./pythonbuild"
    restart: unless-stopped
    depends_on:
      - chrome

networks:
  default:
    external:
      name: "db"
```
