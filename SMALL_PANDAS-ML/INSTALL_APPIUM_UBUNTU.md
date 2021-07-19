# Install Appium on Ubuntu 20.4
* reboot liberally inbetween steps
```console
sudo apt update && sudo apt upgrade
sudo apt install -y git
sudo apt install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv
 ```

## Install openjdk
```console
which java
java --version
sudo apt install -y openjdk-8-jdk
``` 

* Debugging:
```console
sudo apt purge openjdk-11-*
sudo apt purge openjdk-8-*
sudo apt remove --autoremove openjdk-11-*
sudo apt purge oracle-java16-*
...
sudo rm /etc/apt/sources.list.d/*

sudo add-apt-repository main
sudo add-apt-repository universe
sudo add-apt-repository restricted
sudo add-apt-repository multiverse
sudo add-apt-repository ppa:ondrej/php
sudo apt-get update
sudo apt-get install php-curl
sudo reboot
```

## Optional: Use SDKman to install openjdk
```console 
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"  
sdk install java
```

## Install Android Studio and Android SDK
* Download and install https://developer.android.com/studio/
* to /opt/android-studio
* Android SDK Build-Tools
* Android SDK Command-line Tools
* Android emulator
* Android SDK Platform-Tools
```console
sdkmanager --install "platforms;android-30"
sdkmanager -- install "build-tools;30.0.2"
sdkmanager --sdk_root=${ANDROID_HOME} "tools"
sdkmanager --install
```

## Install Node.js and npm
```console
rm package-lock.json && npm i
sudo npm install
npm cache clean --force
npm install -g npm
npm install

sudo chmod -R 755 /usr/local/lib/node_modules/
sudo chmod 755 /usr/local/bin/node
sudo chown -R $USER /usr/local/lib/node_modules/
sudo chown -R 1000:1000 "/home/mac/Desktop/.npm
````

## Install Appium and Appium Desktop:

```console
sudo npm install -g appium@latest --unsafe-perm=true --allow-root
```
* Download and install https://github.com/appium/appium-desktop/releases 
```console 
chmod +x Appium-linux-1.21.0.AppImage`
mkdir -p ~/Android/Appium
mv Appium-linux-1.21.0.AppImage ~/Android/Appium/

sudo apt update
sudo apt install npm
sudo npm cache clean -f
sudo npm install -g n
sudo n stable
sudo chown -R 1000:1000 "/home/mac/.npm"
sudo chown -R $USER /usr/local/lib/node_modules/
sudo npm install -g appium
sudo npm install -g opencv4nodejs --unsafe-prem --allow-root
```

## Optional: Appium Doctor 
```console
npm install -g appium-doctor
appium-doctor
```
* set up  PATHs
```console
sudo nano ~/.bashrc
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$ANDROID_HOME/emulator/emulator:$PATH
export PATH=$ANDROID_HOME/tools/android:$PATH
export PATH=$ANDROID_HOME/platform-tools/adb:$PATH
export PATH=$JAVA_HOME=/usr/share/doc/openjdk-8-jre-headless:$PATH
export PATH=$JAVA_HOME/bin:$PATH

JAVA_HOME=$(dirname $( readlink -f $(which java) ))
JAVA_HOME=$(realpath "$JAVA_HOME"/../)
export JAVA_HOME

sudo update-alternatives --config java

```
* temp access fix for screwed PATH: export PATH="/usr/bin:$PATH"

## Install Chrome and Chrome-Driver
```console
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
google-chrome --version
```
* Download version at https://chromedriver.chromium.org/downloads
```console
sudo unzip chromedriver_linux64.zip -d /usr/local/bin
```
## Set Desired Capabilities as .json
```json
{
  "platformName": "Android",
  "deviceName": "emulator-5554",
  "platformVersion": "11.0",
  "orientation": "PORTRAIT",
  "automationName": "UiAutomator2",
  "noReset": true,
  "newCommandTimeout": 0,
  "appPackage": "com.myapp.android.alpha",
  "appActivity": "com.myapp.android.ui.activity.LoginActivity"
} 
```
