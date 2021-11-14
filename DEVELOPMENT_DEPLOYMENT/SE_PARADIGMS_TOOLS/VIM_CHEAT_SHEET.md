# VIM Cheat Sheet
```console
sudo apt install zsh
zsh
sudo apt install vim
vim file_name
```
meta command
```
esc key
```
window
```console
G
gg
e
b
/forward
?backward
#
n
N
$
CTRL+u
CTRL+d
```
copy paste delete undo redo
```console
c
w
cw
yy
p
11yy
x
s
D
dd
22dd
u
4u
CTRL+R
ZZ
```
write
```console
i
a
I
A
o
O
```
last line commands
```console
:wq
:q!
o
:r append.txt
:sh
:s/old/new/
:s/old/new/g #entire row
:1,$s/old/new #1st each column
:%s/old/new/g #each column, each row
:%s/old/new/gc #each column, each row, safe mode
:h
:make
:e filename 
:set
:! zsh
exit
```
vim misc
```
cd ~ 
vi .vimrc
jobs

ps -ef | grep vim

set -o vi
set -o -emacs

vim -r file

:w file2
:q!
diff file file2
rm .file.swp file2

rm .file.swp
mv file2 file
