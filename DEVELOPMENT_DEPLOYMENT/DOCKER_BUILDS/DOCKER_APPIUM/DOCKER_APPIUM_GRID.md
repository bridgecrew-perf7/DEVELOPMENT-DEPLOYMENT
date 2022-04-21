version: "3.5"

services:
  selenium-hub:
    image: selenium/hub:4.1.1
    expose:
      - "4442"
      - "4443"
    ports:
      - "4444:4444"
  android-node:
    image: selenium/node-docker:4.1.1
    depends_on:
      - selenium-hub
      - android
    volumes:
      # named volume with the android config information
      - "./android.toml:/opt/bin/config.toml"
    environment:
      - SE_EVENT_BUS_HOST=selenium-hub
      - SE_EVENT_BUS_PUBLISH_PORT=4442
      - SE_EVENT_BUS_SUBSCRIBE_PORT=4443
  android:
    image: budtmo/docker-android-x86-7.1.1
    expose:
      - 5554
      - 5555
      - 4567
      - 4723
    ports:
    - "6080:6080"
    environment:
      - DEVICE=Samsung Galaxy S7
      - ATD=true
      - APPIUM=true
      - EMULATOR_ARGS=-memory 4096 -partition-size 5120
      - GA=false
    privileged: true
    volumes:
      - "android-a-data:/root/.android"
      - "android-b-data:/root/android_emulator"
volumes:
  android-a-data:
  android-b-data:
