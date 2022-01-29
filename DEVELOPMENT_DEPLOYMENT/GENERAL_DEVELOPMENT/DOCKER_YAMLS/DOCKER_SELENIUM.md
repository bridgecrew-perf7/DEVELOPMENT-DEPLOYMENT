# Docker Compose File Selenium Grid Chrome Standalone
```console
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
