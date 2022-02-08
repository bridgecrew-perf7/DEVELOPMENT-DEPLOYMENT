# Docker - Kubernetes Administration

## Some Resources:
- https://docs.docker.com/
- https://docs.docker.com/compose/install/
- https://docs.docker.com/compose/compose-file/
- https://docs.docker.com/storage/volumes/
- https://hub.docker.com/_/postgres/
- https://github.com/wagoodman/dive/releases
- https://github.com/nicolaka/netshoot
- https://github.com/bcicen/ctop
- https://github.com/GoogleContainerTools/distroless
- https://containerd.io/
- https://kubernetes.io/
- https://semver.org/
- https://opencontainers.org/
- https://docs.microsoft.com/en-us/windows/wsl/

## Install Docker and Docker Compose Centos

```console
# first always purge all legacy containerization files
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
```console
dnf groupinstall "Development tools"
sudo yum install -y yum-utils
sudo yum-config-manager \
   --add-repo \
   https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker
```
docker compose
```console
CHANGE URL TO NEWEST VERSION FROM
https://github.com/docker/compose/releases/
https://docs.docker.com/compose/install/
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo usermod -aG docker username
docker–compose --version
```
docker dive
```console
https://github.com/wagoodman/dive/releases
# debian
sudo apt install ./dive_X.X.X_linux_amd64.deb
# centos
rpm rpm -i dive_X.X.X_linux_amd64.rpm
```
```
docker debugging
```console
docker inspect
dive IMAGENAME
docker run --name netshoot --rm -it --network custombridge nikolaka/netshoot /bin/bash
docker exec -it container /bin/bash
docker start -i IMAGENAME
dive IMAGENAME
$PWD/pgtest.dump:/docker-entrypoint-initdb.d/init.sql:ro  # bind mount (temp storage only)
pgdata:/var/lib/postgresql/data # named volume (long term storage)
docker exec -ti POSTGRES_CONTAINER pg_dump -U postgres postgres > pgtest.dump # pg docker container backup functionality
```
docker image container network volume compose
```console
docker image rm / ls -a / create / inspect
docker container rm / ls -a / create / inspect
docker volume rm / ls / create / inspect
docker network rm / ls / create / inspect
docker logs -f CONTAINERNAME
docker stop CONTAINERNAME
docker start CONTAINERNAME
docker exec -ti CONTAINERNAME bash
docker run --rm --name CONTAINERNAME IMAGENAME
docker run --rm --name myhttpd -p 9090:80 httpd:latest
docker run --name mypg postgres:12
docker run --name mypg --rm -e POSTGRES_PASSWORD=postgres -v $PWD/pgdata:/var/lib/postgresql/data  postgres:12
docker run --name mypg --rm -e POSTGRES_PASSWORD=postgres -v $PWD/pgtest.dump:/docker-entrypoint-initdb.d/init.sql:ro  -v pgdata:/var/lib/postgresql/data -p 127.0.0.1:5432:5432  postgres:12
docker exec -ti pgtest pg_dump -U postgres postgres > pgtest.dump
docker start -a mypg
docker rmi IMAGENAME
docker volume rm pgdata
docker ps -a
docker history
docker stats
docker info
docker container ls -a
docker container ls --filter "status=exited"
docker container ls -a --filter "ancestor=image_name"
docker container ls -a -q --filter "ancestor=ubuntu"
docker container ls -a-n=-1
docker container ls -a-s
docker container NAME stop
docker container prune
docker commit --help
docker-compose rm --all &&
docker-compose build --no-cache &&
docker-compose up -d --force-recreate &&
docker-compose up -d
docker-compose down && docker-compose up --build -d && docker-compose logs --follow
docker-compose -f /././././docker-compose.module.yml up --build -d
docker-compose -f docker-compose.postgres.yml exec postgres bash
docker-compose logs -f
docker-compose down --volumes
```
docker network
```console
docker network ls
docker network create dock-net
docker network prune
docker network ls
docker network inspect bridge
docker network create custombridge
ip a | grep ens18
ps aux | grep docker
docker network create -d macvlan --subnet 192.168.0.24 --gateway 192.168.0.1 --ip-range  192.168.0.253/32 -o parent=ens18 custommacvlan
docker run --name netshoot --rm -it --network custommacvlan nikolaka/netshoot /bin/bash
docker run -rm -d --name ngnix2 --network custommacvlan --ip 192.168.0.202 ngnix
```
docker django
```console
docker-compose exec web bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py shell
docker-compose exec db psql -U postgres app-name
docker-compose exec web python manage.py test
docker-compose exec web npm install
docker-compose exec web npm run build
docker-compose exec web npm run dev-watch
```
linux
```console
id
ps
ps ef
ps alx
ps aux
kill
kill -9
du
df -h
df -i
ps
lscpu
lshw
stat
cat /etc/hostname
cat /etc/passwd
cat /etc/issue
cat /etc/group
cat /proc/meminfo
ls /sys/fs/cgroup
ls -la /var/run/docker*
chroot folder /bin/bash
```
dockerfiles
```
# docker build . DOCKER CLI -> DOCKER DAEMON
# .dockerignore

# DECLARE IMAGE SOURCE 1. LAYER HASH / SAVES TO HDD
FROM ubuntu:18.04

# CHANGE DATA OF IMAGE 2. LAYER HASH / SAVES TO HDD
RUN apt-get update && apt-get upgrade -y \
      && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
           apache2 \
           curl \
           ca-certificates \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/* \
      && rm -rf /tmp/*

# CHANGE DATA OF IMAGE 3. LAYER HASH SAVES TO HDD
COPY httpd-foreground /usr/local/bin/

# CHANGE METADATA / IMAGE MANIFEST OF IMAGE 4., 5. / THIS IS THE DOCKER INSPECT METADATA
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

# CONTAINER RUNTIME: ADDS READ WRITE LAYER
```
docker compose files
```
```
install kubernetes
```
```
