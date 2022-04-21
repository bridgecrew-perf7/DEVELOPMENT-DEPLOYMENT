#!/bin/bash

LOCKFILE=/tmp/block_file_2

if ( set -o noclobber; echo "$$" > "$LOCKFILE") 2> /dev/null;
then
    trap 'rm -f "$LOCKFILE"; exit $?' INT TERM EXIT

while true; do
  DATE=`date '+%Y-%m-%d'`;

  sudo apt update && sudo apt upgrade

  sleep $((24 * 60 * 60))
done

rm -f "$LOCKFILE"
   trap - INT TERM EXIT

else
   echo " - keepOS_updated Process ALREADY RUNNING! - "
   echo "Block by PID  $(cat $LOCKFILE) ."
   echo "Start with: nohup ./nohup_FILE.sh &, End with: kill -11 thisPID"
   exit
fi

# nohup ./nohup.this.ampers.sh &
# kill -11 thisPID
