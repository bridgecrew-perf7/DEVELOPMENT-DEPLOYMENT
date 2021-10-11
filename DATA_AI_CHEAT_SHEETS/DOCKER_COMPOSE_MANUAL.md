# Docker and Docker Compose manual Ubuntu

_Dockerfile is for the single apps_
_docker-compose.yml is for the entire functional container including the Dockerfiles and additional specifications_

## Docker setup
```console
sudo apt update
sudo apt upgrade
sudo apt install docker
```
## Docker Compose setup
```console
sudo apt install docker-compose
docker–compose –version
```
docker compose commands
```console
sudo docker-compose up -d
sudo docker-compose logs -f
```
docker network commands
```
sudo docker network ls -s
sudo docker network create dock-net

```
docker commands
```console
sudo docker run
sudo docker container ls -a
sudo docker container ls --filter "status=exited"
sudo docker container ls -a --filter "ancestor=image_name"
sudo docker container ls -a -q --filter "ancestor=ubuntu"
sudo docker container ls -a-n=-1
sudo docker container ls -a-s
sudo docker container NAME stop
sudo docker images
sudo docker-compose down --volumes
```
docker container commands
```
sudo docker exec -it XXX bin/bash
exit
docker stop XXX

```
