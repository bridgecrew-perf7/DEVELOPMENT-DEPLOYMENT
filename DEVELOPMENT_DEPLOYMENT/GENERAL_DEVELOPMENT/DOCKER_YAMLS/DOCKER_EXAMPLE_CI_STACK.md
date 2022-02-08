version: '3'

networks:
  ci_net:

services:

  nexus:
    image: sonatype/nexus3:3.28.1
    restart: always
    volumes:
      - nexus_data:/nexus-data
    ports:
      - "127.0.0.1:8081:8081"
    networks:
      - ci_net
    environment:
      - JAVA_MIN_MEM=256m
      - JAVA_MAX_MEM=1200m

  nexus-provision:
    build: ./nexus-provision
    networks:
      - ci_net

  jenkins:
    image: rgielen/jenkins-training
    restart: always
    volumes:
      - jenkins_data:/var/jenkins_home/
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - "127.0.0.1:8082:8080"
    networks:
      - ci_net
    depends_on:
      - nexus

  # HTTPS config (also for proxy mode): https://docs.gitlab.com/omnibus/settings/nginx.html#enable-https
  gitlab:
    image: gitlab/gitlab-ce:11.2.3-ce.0
    restart: always
    networks:
      - ci_net
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://git.127.0.0.1.nip.io'
        nginx['listen_port'] = 80
        nginx['listen_https'] = false
        gitlab_rails['gitlab_shell_ssh_port'] = 2222
    ports:
      - "127.0.0.1:8083:80"
      - "2222:22"
    volumes:
      - gitlab_config:/etc/gitlab
      - gitlab_log:/var/log/gitlab
      - gitlab_data:/var/opt/gitlab


  front-httpd:
    build: ./front-httpd
    restart: always
    ports:
      - 80:80
      - 5000:5000
    environment:
      - REAL_IP=1.2.3.4
    networks:
      - ci_net
      # Optional: Beteiligung an übergreifendem Netzwerk (siehe oben)
      # - proxy_net


volumes:
  nexus_data:
  jenkins_data:
  gitlab_config:
    driver: local
  gitlab_data:
    driver: local
  gitlab_log:
    driver: local
