# SHELL

_everything is a file, including directories, everything has got an inode_
_a process is just a running instance of a file_
_every user, group has got an id, ids define who's got access to process execution_
_kernel, params + initramfs boostrap pseudo terminal, /etc/shells, 4xbins, .profile files; gives manual access to entire linux system starting at "/" directory_

_file suffix is .sh_  
_remember to chmod a+rx file.sh_  
_there are lots of different shells, but basics are the same_
_use www.explainshell.com_  
_always use vim, oh my zshell and tmux_

install zshell
```console
sudo apt update
sudo apt upgrade
sudo apt install zsh
```
.zsh shebang
```console
#!/bin/bash```
python3
```console
import os
import time
os.popen()
os.system()
time.asctime()
```
networks
```console
vi etc/services
last
w
traceroute
tracepath
ping
dig
nmap
ssh-agent sh -c 'ssh-add; ssh-add -L'
ssh-add -D
ssh-keygen -t ed25519 -C "your_email@example.com"
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
ip
ip link show
ip route show
ip a s
ip a s eth0
ip -4 a s enp2s0
hostname -I
netstat -t
netstat -tuln
netstat -tulnpa
nslookup domain.com
ss
nc
host
dig
ifconfig
route
ping
traceroute
iptables
telnet
getent hosts
nmcli
nmcli connection
man nmcli-examples
systemctl
systemctl status httpd
systemctl stop httpd
ssh
scp -r # domain:/
rsync -avn domain:/
rsync -av domain:/
sftp
cat known_hosts
```
bash config files order
```
/etc/.profile
/etc/.bashrc
~/.profile
~/.bashrc
~/.bash_login
~/.bash_profile
```
userid, groupid, other // modes -> pid file execution possibility, administration
```
id
0
1-999
1000+
ls -l
ls -l /home
ps
ps ef
ps aux
kill
kill -9
stat
cat /etc/hostname
cat /etc/passwd
cat /etc/issue
cat /etc/group
cat /proc/meminfo
ls /sys/fs/cgroup
ls -la /var/run/docker*
chroot folder /bin/bash
mdkir /proc
mount -t proc proc /proc
du
df -h
df -i
ps
ps alx
ps aux
htop
ctop
atop
lscpu
lshw
uname -a
alias
history
info
whereis
whoami
which
whatis
useradd -u -g -G -s -c -m
userdel
usermod -c 'Peter Baumann' peter
usermod -aG groupname
usermod -L
usermod -Ufa
groupadd -g 10000 groupname
groupdel
groupmod
chmod ugo +-= rwx /dir
chmod ugo +-= rwx file
chmod u-rwx file1
chmod o-rwx file1
chmod g-rwx file1
chmod ugo-rwx file1
chmod u+X file1
chmod u+s # suid // without x = S
chmod g+s # sgid // without x = S
chmod o+t # sticky bit // without x = T
passwd
umask # 777 - umask = 775 # subtracts rights as a priori default
umask -S
man passwd
chage # password aging scheme
grep user /etc/shadow
vi /etc/passwd
vi /etc/group
vi /etc/shadow
vi /etc/gshadow
vi /etc/login.devs
```
```
basic commands
```console
ls -la
ls -ls
ls -Rla
ls -d
man -a ls
man # 1 user # 5 config # 8 admin ls # \^STRING
ln # hard only files # old # new
ln -s # soft everything # old # new
ln -s /dev/null vortex
cd ~
cd /
cd ..
cp # rename # put inside # put inside dir
cp /file1 /file2 /here
cp -r
cat
cat -n
cat /file1 /file2
pwd
mkdir
rmdir
touch # >
touch file{1-9000} # bracket expansion
touch file{A-Z}
rm
rm -ri
mv
cat
file
crontab
time
timedatectl
tar -cvf etc.tar /etc/
tar -cvjf etc.tar.bz2 /etc/
tar -cvZf etc.tar.xz /etc/
tar -x
tar -tvf etc.tar.gz | less
tar -x -jvf debian9-rootfs.tar.bz2
diff file1 file2 # what to change in file1 to arrive at file 2, < delete > add
diff file1 file2 -W 60 -y
diff3 file1 file2 file3 # what to change in file1 to arrive at file 2 AND what to change in file1 to arrive at file3
find . -name file
find / -inum 123456 2> /dev/null
find /etc -type f -exec grep -i -n -H 'login' {} /dev/nul \;
find /etc -type f fgrep -Hn 'alias...=' {} \; 2> /dev/null
find /etc -type f 2> /dev/null | xargs fgrep -Hn 'alias...=' 2> /dev/null
grep -iaR
grep login$ /file
grep ^d /file
grep -i -n ~ * 2> /dev/null
echo $?
echo *
echo .*
chmod # prio d files, no ownership set theory, check with ls -ld, root transcends
su # keep shell
su - # new login shell
sudo -i # act like root
sudo visudo # ls -l /etc/sudoers
set -o extrace
set -o emacs
set -o vi
head
more
less
tr
env
export
set
unset
seq 1 10
set | less
lynx file.html
yum list chrony*
ls -l /etc/chrony.conf
chronyc sources -v
cd /
shred -n 8 -u
shred -n 8 -u ./././*/*/*/*/*
dd if=/dev/random of=/dev/sdb
dd if=/dev/zero of=/dev/sdb
dd if=/dev/urandom of=/dev/sdb
dd if=/dev/zero of=/dev/sdb
dd if=/dev/random of=/dev/sdb
dd if=/dev/random of=/dev/sdb
```
1 char filters
```console
# Regexp sets
[^abc]
[!abc]
[abc]
# POSIX sets
[[:alpha:]]
[[:digit:]]
[[:alnum:]]
[[:upper:]]
[[:punct:]]
[[:space:]]
```
shell meta commands
```console
[optional]
{mandatory}
| # std 1 to 0
; # separator
< # redirect input
> # redirect output
>> # redirect append output
2>&1 #input and output redirect
? # replace
[abc] # 1 char
[!abc] # 1 char
\x #escape
'string'
"string\$`"
`kdo` # substitute command
$var ${var}  # var
(kdo ; kmd) # isolate substitute commands in separate process
{kdos} # isolate substitute command in same process
BL,TAB # blank tab
NL # newline
CTRL + A, E
CTRL + U, K
Alt + U
Alt + L
Shift + 7
```
stdin (0) stdout (1) stderr (2)
```console
2>/dev/null
> stdout.txt
1> stdout.txt
```
shell vars
```
$ tab tab
echo $HOSTNAME
SURPRISE=CAT
export $SURPRISE
echo $SURPRISE
```
commando substitution
```console
echo $(tty)
echo $(seq 1 100)
echo $[5+7]
```
containerization example linux
```console
# get boot system
wget debian-distro
sudo mkdir rootfs
sudo tar -xjvf debian9-rootfs.tar.bz2 -C rootfs/
sudo mkdir rootfs/proc
# switch inside system
sudo chroot rootfs /bin/bash
ls -la
exit

# create namespace
sudo unshare -p -f --mount-proc=$PWD/rootfs/proc \
    chroot rootfs /bin/bash
ps aux
exit

# enter namespace
sudo ls -l /proc/$PID/ns
sudo nsenter --pid=/proc/$PID/ns/pid \
    unshare -f --mount-proc=$PWD/rootfs/proc \
    chroot rootfs /bin/bash
ps aux
exit

# bind mounts
mkdir readonlyfiles
echo "hello" > readonlyfiles/hi.txt
sudo mkdir -p rootfs/var/readonlyfiles
sudo mount --bind -o ro $PWD/readonlyfiles $PWD/rootfs/var/readonlyfiles
sudo chroot rootfs /bin/bash
cat /var/readonlyfiles/hi.txt
echo "bye" > /var/readonlyfiles/hi.txt
exit
sudo umount $PWD/rootfs/var/readonlyfiles

# control group example
ls /sys/fs/cgroup/
sudo -s
mkdir /sys/fs/cgroup/memory/demo
ls /sys/fs/cgroup/memory/demo/
echo "100000000" > /sys/fs/cgroup/memory/demo/memory.limit_in_bytes
echo "0" > /sys/fs/cgroup/memory/demo/memory.swappiness
# do memory overcommitting stuff...
# -> will get killed without crashing machine
exit

# remove examples
sudo rmdir /sys/fs/cgroup/memory/demo
sudo chroot rootfs /bin/bash
umount /proc
exit
rm debian9-rootfs.tar.bz2
rm -rf rootfs
```
awk
```console
awk -F: '{print $1}' /etc/passwd | while read user
do
id $user
sleep 1
done
```
```
awk pick from input stream
```console
ls -l | awk '{print $5}'
```
find with xargs
```console
find . -name '*.html' -print0 | xargs -0 file
```
sed delete lines
```console
sed 3,6d /etc/passwd

```
sed replace one instance per line of input
```console
sed 's/REPLACE/text/'

```
sed replace all instances of input
```console
sed 's/REPLACE/text/g'
```
sed delete all lines of input
```console
sed '/DELETE/d'
```
shell scripting functionality
```
while loop
```console
#!/bin/bashi=0

while [ $i -le 2 ]
do
echo Number: $i
((i++))
done
```
for loop
```console
#!/bin/bash
for (( counter=1; counter<=10; counter++ ))
do
echo -n "$counter "
done
printf "\n"
```
user input
```console
#!/bin/bash
echo -n "Enter Something:"
read something

echo "You Entered: $something"
```
if statement
```console
#!/bin/bash
echo -n "Enter a number: "
read num

if [[ $num -gt 10 ]]
then
echo "Number is greater than 10."
fi
```
if else
```console
#!/bin/bash
read n
if [ $n -lt 10 ];
then
echo "It is a one digit number"
else
echo "It is a two digit number"
fi
```
and operator
```console
#!/bin/bash
echo -n "Enter Number:"
read num

if [[ ( $num -lt 10 ) && ( $num%2 -eq 0 ) ]]; then
echo "Even Number"
else
echo "Odd Number"
fi
```
or operator
```console
#!/bin/bash
echo -n "Enter any number:"
read n

if [[ ( $n -eq 15 || $n -eq 45 ) ]]
then
echo "You won"
else
echo "You lost!"
fi
```
elif
```console
#!/bin/bash
echo -n "Enter a number: "
read num

if [[ $num -gt 10 ]]
then
echo "Number is greater than 10."
elif [[ $num -eq 10 ]]
then
echo "Number is equal to 10."
else
echo "Number is less than 10."
fi
```
switch
```console
#!/bin/bash
echo -n "Enter a number: "
read num

case $num in
100)
echo "Hundred!!" ;;
200)
echo "Double Hundred!!" ;;
*)
echo "Neither 100 nor 200" ;;
esac
```
arguments
```console
#!/bin/bashecho "Total arguments : $#"
echo "First Argument = $1"
echo "Second Argument = $2"
```
send mails
```console
#!/bin/bashrecipient=”admin@example.com”
subject=”Greetings”
message=”Welcome to UbuntuPit”
`mail -s $subject $recipient <<< $message`
```

sleep
```console
#!/bin/bash
echo "How long to wait?"
read time
sleep $time
echo "Waited for $time seconds!"
```

print last updated
```console
#!/bin/bashls -lrt | grep ^- | awk 'END{print $NF}'
```

staying updated
```console
#!/bin/bashecho -e "\n$(date "+%d-%m-%Y --- %T") --- Starting work\n"
apt-get update
apt-get -y upgrade
apt-get -y autoremove
apt-get autoclean
echo -e "\n$(date "+%T") \t Script Terminated"
```
monitor disk usage
```console
#!/bin/sh
# set -x
# Shell script to monitor or watch the disk space
# It will send an email to $ADMIN, if the (free available) percentage of space is &gt;= 90%.
# -------------------------------------------------------------------------
# Set admin email so that you can get email.
ADMIN="root"
# set alert level 90% is default
ALERT=90
# Exclude list of unwanted monitoring, if several partions then use "|" to separate the partitions.
# An example: EXCLUDE_LIST="/dev/hdd1|/dev/hdc5"
EXCLUDE_LIST="/auto/ripper"
#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#
function main_prog() {
while read output;
do
#echo $output
  usep=$(echo $output | awk '{ print $1}' | cut -d'%' -f1)
  partition=$(echo $output | awk '{print $2}')
  if [ $usep -ge $ALERT ] ; then
     echo "Running out of space \"$partition ($usep%)\" on server $(hostname), $(date)" | \
     mail -s "Alert: Almost out of disk space $usep%" $ADMIN
  fi
done
}
if [ "$EXCLUDE_LIST" != "" ] ; then
  df -H | grep -vE "^Filesystem|tmpfs|cdrom|${EXCLUDE_LIST}" | awk '{print $5 " " $6}' | main_prog
else
  df -H | grep -vE "^Filesystem|tmpfs|cdrom" | awk '{print $5 " " $6}' | main_prog
fi
```
monitor cpu usage
```console
#!/bin/bash
while [ true ] ;do
used=`free -m |awk 'NR==3 {print $4}'`

if [ $used -lt 1000 ] && [ $used -gt 800 ]; then
echo "Free memory is below 1000MB. Possible memory leak!!!" | /bin/mail -s "HIGH MEMORY ALERT!!!" user@mydomain.com

fi
sleep 5
done
```
add new users
```console
#!/bin/bash
# Script to add a user to Linux system
if [ $(id -u) -eq 0 ]; then
    read -p "Enter username : " username
    read -s -p "Enter password : " password
    egrep "^$username" /etc/passwd >/dev/null
    if [ $? -eq 0 ]; then
        echo "$username exists!"
        exit 1
    else
        pass=$(perl -e 'print crypt($ARGV[0], "password")' $password)
        useradd -m -p $pass $username
        [ $? -eq 0 ] && echo "User has been added to system!" || echo "Failed to add a user!"
    fi
else
    echo "Only root may add a user to the system"
    exit 2
fi
```
