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
install docker compose,
```
CHANGE URL TO NEWEST VERSION FROM https://docs.docker.com/compose/install/
REMOVE OLD VERSIONS PRIOR
sudo curl -L https://github.com/docker/compose/releases/download/1.25.1-rc1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo usermod -aG docker username
docker–compose --version
# restart server
```
## Docker Commands
```console
docker-compose up -d
docker-compose -f /././././docker-compose.module.yml up --build -d
docker-compose logs -f
docker-compose down --volumes
docker-compose -f docker-compose.postgres.yml exec postgres bash
psql -U <database username you want to connect with> -d <database name>
docker-compose down && docker-compose up --build -d && docker-compose logs --follow
docker-compose exec web bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py shell
docker-compose exec db psql -U postgres app-name
docker-compose exec web python manage.py test
docker-compose exec web npm install
docker-compose exec web npm run build
docker-compose exec web npm run dev-watch
docker run
docker rmi 123
docker ps -a
docker container ls -a
docker exec -it 123 bin/bash
docker stop XXX
docker history
docker stats
docker info
docker ps -a
docker exec -it container /bin/bash
docker network ls
docker network create dock-net
docker network prune
docker network ls
docker network inspect bridge
docker network create custombridge
docker run --name netshoot --rm -it --network custombridge nikolaka/netshoot /bin/bash
ip a | grep ens18
docker network create -d macvlan --subnet 192.168.0.24 --gateway 192.168.0.1 --ip-range  192.168.0.253/32 -o parent=ens18 custommacvlan
docker run --name netshoot --rm -it --network custommacvlan nikolaka/netshoot /bin/bash
docker run -rm -d --name ngnix2 --network custommacvlan --ip 192.168.0.202 ngnix
sudo docker container ls -a
sudo docker container ls --filter "status=exited"
sudo docker container ls -a --filter "ancestor=image_name"
sudo docker container ls -a -q --filter "ancestor=ubuntu"
sudo docker container ls -a-n=-1
sudo docker container ls -a-s
sudo docker container NAME stop
sudo docker container prune

```
# Install Kubernetes
```
```
# Install Ansible
```
```
