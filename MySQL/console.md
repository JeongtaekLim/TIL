# Login
```
mysql --host=test-db.this_is_my_db_address.ap-northeast-2.rds.amazonaws.com --port my_port_3306 --user=my_id --password
```

# binlog 생성이 되고있는지 확인하기 위해서
```
SHOW VARIABLES LIKE 'log_bin';
```