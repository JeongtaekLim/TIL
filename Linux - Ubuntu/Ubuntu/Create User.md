# Create User

1. add user
```
# adduser username
```

2. If this user is admin account,
```
# usermod -aG sudo username
```

3. test new user account
```
# su - username
```

4. If you want to list all users,
```
vim /etc/passwd
```