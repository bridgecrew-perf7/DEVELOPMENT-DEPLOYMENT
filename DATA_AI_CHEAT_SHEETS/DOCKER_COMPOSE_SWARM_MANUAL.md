# Docker and Docker Compose Docker Swarm manual Ubuntu

1. Docker layers all images on top of the base image and reuses them
2. There are images, builds, containers, running processes and networks
3. Dockerfile to specify close app layering, base image etc
3. docker-compose.yml for each functonal unit including the Dockerfiles, images, networks etc
4. Use supervisord
5. Use CI/CD Git versioning
6. file structure: /docker-builds/project-modules/module-builds/dockerbuild/docker-compose.yml, appbuild/Dockerfile

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
sudo docker-compose -f /././././docker-compose.module.yml -d
sudo docker-compose logs -f
sudo docker-compose down --volumes
sudo docker-compose -f docker-compose.postgres.yml exec postgres bash
psql -U <database username you want to connect with> -d <database name>

```
docker network commands
```console
sudo docker network ls
sudo docker network create dock-net
sudo docker network prune
```
docker container commands
```console
sudo docker container ls -a
sudo docker container ls --filter "status=exited"
sudo docker container ls -a --filter "ancestor=image_name"
sudo docker container ls -a -q --filter "ancestor=ubuntu"
sudo docker container ls -a-n=-1
sudo docker container ls -a-s
sudo docker container NAME stop
sudo docker container prune
```
docker commands
```console
sudo docker run
sudo docker images ls -a
sudo docker rmi 123
sudo docker ps -a
sudo docker container ls -a
sudo docker exec -it 123 bin/bash
exit
docker stop XXX
```
docker swarm commands
```console
docker swarm init --advertise-addr <MANAGER-IP>
docker swarm init --advertise-addr 192.168.99.100
docker info
docker node ls
```
