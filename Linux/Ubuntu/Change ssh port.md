# Change ssh port

1. open sshd_config file
```
vi /etc/ssh/sshd_config
```

2. change below line to port you want
```
# Port 22
```

3. restart sshd
```
service sshd restart
```