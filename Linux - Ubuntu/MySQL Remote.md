# MySQl Remote

## Install
```
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
systemctl status mysql.service
```
ps. please look `Linux - Ubuntu/Initialize macro.md`

## Query
If you want to access MySQL at remote,
```
$ mysql -u root -p
$ CREATE USER '[username]'@'localhost' IDENTIFIED BY '[password]';
$ GRANT ALL PRIVILEGES ON *.* TO '[username]'@'localhost' WITH GRANT OPTION;
$ CREATE USER '[username]'@'%' IDENTIFIED BY 'password';
$ GRANT ALL PRIVILEGES ON *.* TO '[username]'@'%' WITH GRANT OPTION;
$ FLUSH PRIVILEGES;
```

## Edit mysql config
at `/etc/mysql/mysql.conf.d`, edit below content
```
bind-address = 127.0.0.1 -> bind-address = 0.0.0.0
```

## Manage user
```
SELECT User,Host FROM mysql.user;
```
will display as
```
+------------------+-----------+
| User             | Host      |
+------------------+-----------+
| debian-sys-maint | localhost |
| mysql.sys        | localhost |
| root             | localhost |
+------------------+-----------+
```

If you want to drop some user,
```
DROP USER '[username]'@'localhost'
```

## Ping Test
```
telnet 127.0.0.1 3306
telnet [some ip address] [port number]
```
to check connection, try that

## Don forget allow port from hosting site
If you are using some virtual hosting, please don't forget to `add firewall rule` on that site also!