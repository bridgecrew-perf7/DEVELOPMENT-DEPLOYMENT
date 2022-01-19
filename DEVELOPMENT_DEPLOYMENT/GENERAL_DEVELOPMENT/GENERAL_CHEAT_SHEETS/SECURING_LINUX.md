# Securing Linux / CentOS

_Root does not "host"_
_Disable root SSH_
_Domain name SPOC is load balancer_
_Unused ports are deactvated_
_User content is on different domain_
_Shelf Object Relational Mapper (ORM)_  
_Shelf HTML template library (ORM)_
_Shelf CSRF Tokens_
_Use DNF whenever possible_

```
sudo dnf groupinstall "Development tools"
```
users
```
adduser newsudouser
usermod -a -d -m -G wheel newsudouser
passwd newsudouser secret
grep newsudouser /etc/passwd
deluser -f -r newsudouser
su -
```
```
sshd setup
```
vi /etc/ssh/sshd_config
PermitRootLogin yes
PermitEmptyPasswords yes
PasswordAuthentication no
PubkeyAuthentication yes
Port 7753
systemctl restart sshd
systemctl enable sshd
```
ssh keys
```
ssh-keygen -b
ssh-copy-id newuser@ip_address
```
setup iptables
```
iptables -L
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 7822 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

iptables -P INPUT DROP

iptables-save > /etc/sysconfig/iptables
iptables-restore < /etc/sysconfig/iptables
iptables-restore -n < /etc/sysconfig/iptables

dnf install iptables-services
systemctl start iptables
systemctl enable iptables
service iptables save
```
```
fail2ban
```
dnf upgrade
dnf install epel-release -y
dnf install fail2ban -y
vi /etc/fail2ban/jail.local
[DEFAULT]
ignoreip = Your-server-ip
bantime = 1d
findtime = 1d
maxretry = 5
banaction = iptables-multiport
backend = systemd
[sshd]
enabled = true
systemctl start fail2ban
systemctl enable fail2ban
systemctl status fail2ban
```
```
setup firewalld
```
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --permanent --zone=public --add-service=https
firewall-cmd --reload
systemctl start firewalld
systemctl enable firewalld
```
