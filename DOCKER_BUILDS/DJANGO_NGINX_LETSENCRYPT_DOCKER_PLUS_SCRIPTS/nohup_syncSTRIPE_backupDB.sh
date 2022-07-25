#!/bin/bash

LOCKFILE=/tmp/block_file

if ( set -o noclobber; echo "$$" > "$LOCKFILE") 2> /dev/null;
then
    trap 'rm -f "$LOCKFILE"; exit $?' INT TERM EXIT

while true; do
  DATE=`date '+%Y-%m-%d'`;
  docker exec -ti web_container python manage.py djstripe_sync_models
  sleep $((1 * 60 * 60))
  docker exec -ti postgres_container pg_dump -U postgres csync > postgres_dump.dump && docker exec -ti postgres_container pg_dump --insert -U postgres csync > sql_insert.sql
  sleep $((24 * 60 * 60))
done

rm -f "$LOCKFILE"
   trap - INT TERM EXIT

else
   echo "syncSTRIPE_backupDB Process ALREADY RUNNING"
   echo "Block by PID  $(cat $LOCKFILE) ."
   echo "Start with: nohup ./nohup_FILE.sh &, End with: kill -11 thisPID"
   exit
fi

# nohup ./nohup.this.ampers.sh &
# kill -11 thisPID
