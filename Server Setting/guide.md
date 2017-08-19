# Deploy Server Setting guide - Django

1. Linux - Ubuntu

- see `Create User`

2. Install minimum requirements
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev nginx
```

3. Set virtualenv activate command
```
vim proj/venv/bin/activate
```
```
DJANGO_SETTINGS_MODULE="proj.production_settings"
export DJANGO_SETTINGS_MODULE
```

4. Set gunicorn command
```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=username
Group=www-data
WorkingDirectory=/home/username/proj/proj-back
Environment="DJANGO_SETTINGS_MODULE=proj.production_settings"
ExecStart=/home/username/proj/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/username/proj/proj-back/proj.sock proj.wsgi:application

[Install]
WantedBy=multi-user.target
```

# Deploy Server Setting guide - React
