# Docker Compose, Kubernetes, Ansible

## Install Docker Compose Centos
purge docker
```
sudo yum remove docker \
                 docker-client \
                 docker-client-latest \
                 docker-common \
                 docker-latest \
                 docker-latest-logrotate \
                 docker-logrotate \
                 docker-engine
sudo yum remove docker-ce docker-ce-cli containerd.io
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```
install docker
```
dnf groupinstall "Development tools"
sudo yum install -y yum-utils
sudo yum-config-manager \
   --add-repo \
   https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker
```
install docker compose
```
sudo curl -L https://github.com/docker/compose/releases/download/1.25.1-rc1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo usermod -aG docker username
# restart server
```
## Install Docker Compose Ubuntu 21.10
```console
sudo purge docker
sudo install docker
```
sudo apt update
sudo apt upgrade
sudo apt install docker
```
install docker compose
```console
sudo apt install docker-compose
docker–compose –version
```
## Docker Commands
```console
sudo docker-compose up -d
sudo docker-compose -f /././././docker-compose.module.yml -d
sudo docker-compose logs -f
sudo docker-compose down --volumes
sudo docker-compose -f docker-compose.postgres.yml exec postgres bash
psql -U <database username you want to connect with> -d <database name>
docker-compose down && docker-compose up --build -d && docker-compose logs --follow
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
# Install Kubernetes Centos
```
```
# Install Ansbible Centos
```
```
