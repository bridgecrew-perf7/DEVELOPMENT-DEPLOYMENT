# Docker Best Practice Cheat Sheet Python

_Always use and read OFFICIAL DOCKER HUB https://hub.docker.com/_

## All Minimized, No Frills, Resilient, Fractal, Clean and Secure Images
1. Use multi-stage building in Dockerfile FROM>COP>RUN>COPY... #FROM>COPY>RUN
2. Do not run unnecessary Dockerfile commands FROM>ENV>COPY>RUN>COPY...
2. No secrets in Docker Container
3. No ROOT in Docker Container
4. Use .dockerignore File
5. Use slimmest "-slim" available working shelf Docker Images
6. Use && Commands
7. Use COPY, not ADD
8. Sequentialize ENTRYPOINT and CMD Commands
8. Run one logical process per Docker Container
9. Limit memory and processor per Docker Container
10. Logging to stdout stderr
11. Use Docker Compose
12. Use Docker Network
13. Use Docker Swarm (for secrets)
14. Use Docker Scan
15. Use Docker Content Trust

## Examples
```
# temp stage
FROM python:3.9-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
DOCKER_CONTENT_TRUST=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


# final stage
FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*
```
```
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r /requirements.txt

COPY sample.py .
```
```
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    matplotlib \
    pillow  \
    && rm -rf /var/lib/apt/lists/*
```
```
RUN addgroup --system app && adduser --system --group app

USER app
```
```
# copy local files on the host  to the destination
COPY /source/path  /destination/path
ADD /source/path  /destination/path

# download external file and copy to the destination
ADD http://external.file/url  /destination/path

# copy and extract local compresses files
ADD source.file.tar.gz /destination/path
```
```
ENTRYPOINT ["gunicorn", "config.wsgi", "-w"]
CMD ["4"]
gunicorn config.wsgi -w 4
```
```
Project name: web
Environment name: prod
Git commit hash: a072c4e5d94b5a769225f621f08af3d4bf820a07
Semantic version: 0.1.
docker build -t web-prod-a072c4e5d94b5a769225f621f08af3d4bf820a07-0.1.4 .
```
```
.dockerignore
**/.git
**/.gitignore
**/.vscode
**/coverage
**/.env
**/.aws
**/.ssh
Dockerfile
README.md
docker-compose.yml
**/.DS_Store
**/venv
**/env
```
```
docker build --no-cache --progress=plain --secret id=mysecret,src=secrets.txt .
```
```
version: "3.9"
services:
  redis:
    image: redis:alpine
    deploy:
      resources:
        limits:
          cpus: 2
          memory: 512M
        reservations:
          cpus: 1
          memory: 256M
```
