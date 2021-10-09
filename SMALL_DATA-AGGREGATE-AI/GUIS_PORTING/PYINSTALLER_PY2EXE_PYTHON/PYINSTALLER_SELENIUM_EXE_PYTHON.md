# Pyinstaller and mingw crosscompiler setup linux hippo
Install dependencies
```console
sudo apt install pip
sudo apt install pipenv

sudo apt install glibc
sudo apt install libc-bin
sudo apt install objdump
sudo apt install objcopy
sudo apt install binutils

pipenv shell
pipenv install selenium pyinstaller

sudo pip install pyinstaller
```
```
pyinstaller xxx.spec
```

build spec, then run again

## definitions.py DRIVER_PATH
```console
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

DRIVER_PATH = resource_path("/driver/chromedriver")
```

