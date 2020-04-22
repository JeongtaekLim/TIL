# External Access

https://stackoverflow.com/a/19359062/2627126

```
$ mysql -uroot -proot
```

```
C:\Users\UserName> cd C:\Program Files (x86)\MySQL\MySQL Server 5.0\bin

C:\Program Files (x86)\MySQL\MySQL Server 5.0\bin>mysql -uroot -proot

mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root';
Query OK, 0 rows affected (0.27 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.25 sec)
```

```
mysql> GRANT ALL PRIVILEGES ON *.* TO 'testUser'@'%' IDENTIFIED BY 'testUser';
Query OK, 0 rows affected (0.00 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)
```

# Root password 변경

```
mysql -u root -p
mysql> use mysql;
mysql> select host, user, password from user;
mysql> update user set password=password('asdf1234') where user='root';
mysql> select host, user, password from user;
mysql> exit

```

서버 재시작
