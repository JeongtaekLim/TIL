# gunicorn.service

```

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=jtlim
Group=www-data
WorkingDirectory=/home/jtlim/proj/proj-back
Environment="DJANGO_SETTINGS_MODULE=proj.production_settings"
ExecStart=/home/jtlim/proj/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/myusername/proj/proj.sock proj.wsgi:application

[Install]
WantedBy=multi-user.target
```