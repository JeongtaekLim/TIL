### Init of project
When you want to install django with python3 you should set virtualenv as python3 first
```
$ virtualenv -p python3 venv
```
Then, install django
```
$ pip install django
```
Also you may need mysqlclient for using MySQL
```
$ pip install mysqlclient
```
If you want to start mysite,
```
$ django-admin startproject mysite
```
When you have to add new app,
```
$ python manage.py startapp blog
```
```
DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'testdb',   # Name of database instance
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'USER': 'root',
    'PASSWORD': 'password',
}}
```
