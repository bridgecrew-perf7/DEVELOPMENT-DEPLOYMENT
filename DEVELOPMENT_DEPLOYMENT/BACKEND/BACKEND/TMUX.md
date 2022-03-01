# Tmux Cheat Sheet
```
sudo apt update
sudo apt install tmux
sudo apt install vim
sudo apt install curl wget git
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
tmux commands
```
tmux new -s SESSION
Ctrl + b c
Ctrl + ,
Ctrl + b %
Ctrl + b o
Ctrl + b p
Ctrl + b '
Ctrl + b d
Ctrl + b (
Ctrl + b )
tmux kill-ses -t SESSION
tmux kill-session -a
tmux kill-session -a -t SESSION
tmux attach -d
tmux ls
tmux list-sessions
tmux a -t SESSION
tmux at -t SESSION
tmux attach -t SESSION
tmux attach-session -t SESSION
Attach to a session with the name SESSION
Ctrl + b $
Ctrl + b ,
Ctrl + b s
Ctrl + b w
```
helpful standard shell commands
```
cp -v	used to print informative massage
cp -r	used to copy any directory
mv -u	update-move when the source is newer than the destination
mv -v	to move any directory
ls -n	to display UID and GID directory
ls –version	to check the version of ls command
cd —	show last working directory from where we moved
ls -l	show file action like – modified, date and time, owner of file, permissions Etc.
ls help	show display how to use “ls” command
cp -n	no file overwrite
cd ~	move to users home directory from anywhere
cd –	move one directory back from the current location
mv [file name]	move any file and folder
ls	list directory
ls -a	list all files including hidden files
pwd -	it shows your current working directory
mv -i	interactive prompt before overwrite
wget [url] - 	install tool , apt install wget
git clone [url]- 	install any tools with git clone, apt install git
ls -al	formatted listing with hidden files
mv -f	force move by overwriting destination files without prompt
ls -i	Display the number of file or directory
cp	copy any file
cd /	change to the root directory
cd	change directory
cd ..	change the current directory to parent directory
```
