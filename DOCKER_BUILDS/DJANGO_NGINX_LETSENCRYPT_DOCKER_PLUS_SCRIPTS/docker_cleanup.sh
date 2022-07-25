#!/bin/bash

# Install jq thus:
# sudo apt-get install -y jq


# LOCKFILE=/tmp/block_file
#
# if ( set -o noclobber; echo "$$" > "$LOCKFILE") 2> /dev/null;
# then
#     trap 'rm -f "$LOCKFILE"; exit $?' INT TERM EXIT
#
# while true; do
#   DATE=`date '+%Y-%m-%d'`;

docker-compose -f docker-compose.yml down -v && docker container prune -f && docker network prune -f && docker rmi -f $(docker images -a -q) && docker images -a | awk '{print $3}' | xargs docker rmi && docker ps -a | grep Removal | cut -f1 -d' ' | xargs -rt docker rm  2>&1 >/dev/null | grep "dataset does not exist" |  awk '{print $(NF-4)}' | sed "s/'//g" | cut -f1 -d':' |  xargs -L1 sh -c 'for arg do sudo zfs destroy -R "$arg"; sudo zfs destroy -R "$arg"-init ; sudo zfs create "$arg" ; sudo zfs create "$arg"-init ; ...; done' _ ; docker ps -a | grep Removal | cut -f1 -d' ' | xargs -rt docker rm 2>&1 >/dev/null

stuck=$(docker ps -a | grep Removal | cut -f1 -d' ')
echo "$stuck"
for container in $stuck; do
	zfs_path=$(docker inspect "$container" | jq -c '.[] | select(.State | .Status == "dead")|.GraphDriver.Data.Dataset')
	zfs_path=$(echo "$zfs_path"|tr -d '"')
	sudo zfs destroy -R "$zfs_path"
	sudo zfs destroy -R "$zfs_path"-init
       	sudo zfs create "$zfs_path"
       	sudo zfs create "$zfs_path"-init
	docker rm "$container"
done

# docker-compose -f docker-compose.yml up --build

# # sleep 10 hours
#   sleep $((10 * 60 * 60))
# done
#
# rm -f "$LOCKFILE"
#    trap - INT TERM EXIT
#
# else
#    echo "Warning. Script is already running!"
#    echo "Block by PID  $(cat $LOCKFILE) ."
#    exit
# fi
#
# # nohup ./nohup.this.ampers.sh &
# # kill -11 thisPID
