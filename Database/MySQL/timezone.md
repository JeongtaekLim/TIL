# timezone error
If you have some timezone error with Django, 
(stackoverflow - Database returned an invalid value)[https://stackoverflow.com/questions/21351251/database-returned-an-invalid-value-in-queryset-dates]

```
$ mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -D mysql -u root -p 
```

```
$ mysql -u root -p -e "flush tables;" mysql 
```

