# Shell and Shell Scripts Cheat Sheet Linux

_file suffix is .sh_  
_remember to chmod a+rx file.sh_  
_use www.explainshell.com_  
_kernel bootstaps pseudo terminal, /etc/shells, 4xbins, .profile files; gives manual access to entire linux system starting at "/" directory_

install zshell
```console
sudo apt update
sudo apt upgrade
sudo apt install zsh
```
.zsh shebang
```console
#!/bin/zsh
```
python3
```console
import os
import time
os.popen()
os.system()
time.asctime()
```
commands
```console
ls -la
ls -Rla
ls -d
ln
ln -s
ln -s /dev/null florian
cd ~
cd /
cd ..
cp /file1 /file2 /here
cat /file1 /file2
pwd
mkdir
rmdir
touch
rm
rm -r
mv
cat
file
du
df -h
df -i
ps
ps alx
ss
ping
dig
nmap
ifconfig
time
alias
find . -name file
grep -iaR
grep login$ /file
grep ^d /file
grep -i -n ~ * 2>/dev/null
find /etc -type f -exec grep -i -n -H 'login' {} /dev/nul \;
find /etc -type f fgrep -Hn 'alias...=' {} \; 2> /dev/null
find /etc -type f 2> /dev/null | xargs fgrep -Hn 'alias...=' 2> /dev/null
echo $?
echo *
echo .*
chmod # prio d files, no ownership set theory, check with ls -ld, root transcends
chmod ugo +-= rwx /dir
chmod ugo +-= rwx file
chmod u-rwx .
chmod o-rwx .
chmod g-rwx .
chmod ugo-rwx .
chusr
editusr
newusr
passwd
su -
su -l
id
groups root
whereis
whoami
which
whatis
man
man awk
man sed
man rsync
set -o extrace
set -o emacs
set -o vi
head
more
less
shred -n 8 -u 
shred -n 8 -u */*/*/*/*/*/*/*
dd if=/dev/random of=/dev/sdb
dd if=/dev/zero of=/dev/sdb
dd if=/dev/urandom of=/dev/sdb
dd if=/dev/zero of=/dev/sdb
dd if=/dev/random of=/dev/sdb
dd if=/dev/random of=/dev/sdb
```
ideos shell 
```console
| # std 1 to 0
; # separator
< # redirect input
> # redirect output
>> # append output to
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
```
stdin (0) stdout (1) stderr (2)
```console
2>/dev/null
> stdout.txt
1> stdout.txt
```
awk
```console
awk -F: '{print $1}' /etc/passwd | while read user
do
id $user
sleep 1
done
```
sed
```console
```
rsync
```console
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
while loop
```console
#!/bin/zsh
i=0

while [ $i -le 2 ]
do
echo Number: $i
((i++))
done
```
for loop
```console
#!/bin/zsh
for (( counter=1; counter<=10; counter++ ))
do
echo -n "$counter "
done
printf "\n"
```
user input
```console
#!/bin/zsh

echo -n "Enter Something:"
read something

echo "You Entered: $something"
```
if statement
```console
#!/bin/zsh

echo -n "Enter a number: "
read num

if [[ $num -gt 10 ]]
then
echo "Number is greater than 10."
fi
```
if else
```console
#!/bin/zsh

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
#!/bin/zsh

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
#!/bin/zsh

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
#!/bin/zsh

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
#!/bin/zsh

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
#!/bin/zsh
echo "Total arguments : $#"
echo "First Argument = $1"
echo "Second Argument = $2"
```
send mails
```console
#!/bin/zsh
recipient=”admin@example.com”
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
#!/bin/zsh
ls -lrt | grep ^- | awk 'END{print $NF}'
```

staying updated
```console
#!/bin/zsh
echo -e "\n$(date "+%d-%m-%Y --- %T") --- Starting work\n"
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
