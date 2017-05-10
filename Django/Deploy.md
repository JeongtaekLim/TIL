# Deploy

* Caution

This turorial is based on [Digital Ocean, Django deploy tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-14-04), but not covering full content.
ex, following this instruction, you can't run guinicorn by
```
$ sudo service gunicorn start
```
and you may can't see log file in `/var/log/upstart/gunicorn.log`

1. static file
```
$ python manage.py collectstatic
```
about more details, please look [stack overflow](http://stackoverflow.com/questions/8687927/django-static-static-url-static-root)

2. gunicorn
* install
```
$ pip install gunicorn
```
* run
```
$ gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application
```

3. nginx
```
server {
    listen 80;
    server_name my_domain;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/user/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
    }
}
```

That's all!

This guide has to be updated in future with some content about
```
$ sudo service gunicorn start
```
and should be tested with static files