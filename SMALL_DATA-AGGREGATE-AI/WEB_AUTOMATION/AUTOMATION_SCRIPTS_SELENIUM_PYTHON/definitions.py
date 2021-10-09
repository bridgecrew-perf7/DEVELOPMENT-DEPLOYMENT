import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

DRIVER_PATH = "./driver/chromedriver"
#DRIVER_PATH = resource_path("/driver/chromedriver")
VERSION = "1.0.0"


