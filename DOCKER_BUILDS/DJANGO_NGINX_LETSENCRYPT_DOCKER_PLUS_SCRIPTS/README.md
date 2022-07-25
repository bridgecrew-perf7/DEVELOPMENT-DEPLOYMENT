```
chmod u+rwx *.yml
chmod u+rwx *.sh
chmod u+rwx ./nginx_data
make init
./init_letsencrypt_staging.sh

check if works, delete archive
# ./init_letsencrypt_live.sh
```
