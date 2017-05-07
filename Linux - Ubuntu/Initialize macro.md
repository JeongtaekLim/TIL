# Initialize macro
```
#!/bin/bash

# MySQL
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
systemctl status mysql.service

# pip
sudo apt-get install pip
# virtual-env
sudo apt-get install virtualenv
```
source : [digital ocean](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04)
