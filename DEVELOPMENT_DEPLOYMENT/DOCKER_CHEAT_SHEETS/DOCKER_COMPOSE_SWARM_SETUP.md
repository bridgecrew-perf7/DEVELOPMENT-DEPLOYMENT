# Docker and Docker Compose Docker Swarm manual Ubuntu

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
sudo docker history
```
docker swarm commands
```console
docker swarm init --advertise-addr <MANAGER-IP>
docker swarm init --advertise-addr 192.168.99.100
docker info
docker node ls
```
