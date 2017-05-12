# Initialize macro
Target OS : Ubuntu 16.06 LTS
```
#!/bin/bash

# MySQL
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
systemctl status mysql.service

# redis
sudo apt-get install redis-server

# Ready for 'pip install mysqlclient'
sudo apt-get install libmysqlclient-dev

# python-dev
sudo apt-get install python-dev
sudo apt-get install python3-dev

# pip
sudo apt-get install pip

# virtual-env
sudo apt-get install virtualenv

# nginx
sudo apt-get install nginx


```
source : [digital ocean](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04)
