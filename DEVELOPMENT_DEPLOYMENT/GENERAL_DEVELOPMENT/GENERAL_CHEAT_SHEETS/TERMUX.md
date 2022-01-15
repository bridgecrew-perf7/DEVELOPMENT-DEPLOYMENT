# TERMUX CHEAT SHEET
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

tmux new-session
new
Start a new session

tmux new -s mysession
new -s mysession
Start a new session with the name mysession

tmux kill-ses -t mysession
tmux kill-session -t mysession
kill/delete session mysession

tmux kill-session -a
kill/delete all sessions but the current

tmux kill-session -a -t mysession
kill/delete all sessions but mysession

Ctrl + b $
Rename session

Ctrl + b d
Detach from session

attach -d
Detach others on the session (Maximize window by detach other clients)

tmux ls
tmux list-sessions
Ctrl + b s
Show all sessions

tmux a
tmux at
tmux attach
tmux attach-session
Attach to last session

tmux a -t mysession
tmux at -t mysession
tmux attach -t mysession
tmux attach-session -t mysession
Attach to a session with the name mysession

Ctrl + b w
Session and Window Preview

Ctrl + b (
Move to previous session

Ctrl + b )
Move to next session
