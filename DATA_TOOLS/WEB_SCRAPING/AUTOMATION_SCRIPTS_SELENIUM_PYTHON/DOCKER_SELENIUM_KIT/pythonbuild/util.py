import os
import random
import subprocess
import time
from contextlib import closing
from typing import List

import psutil
from random_user_agent.params import SoftwareName, OperatingSystem, Popularity
from random_user_agent.user_agent import UserAgent
from selenium.webdriver.chrome.webdriver import WebDriver

def get_random_resolution(min_width=1000, max_width=1700, min_height=800, max_height=1100):
    width = random.randint(min_width, max_width)
    height = random.randint(min_height, max_height)

    resolution = {'height': height,'width': width}
    return resolution

def get_random_ua():

    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value]
    popularity = [Popularity.POPULAR.value]

    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, popularity=popularity, limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()

    return user_agent


def random_wait(min_wait, max_wait):
    time.sleep(random.randint(min_wait, max_wait))
