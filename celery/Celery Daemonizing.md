# Celery Daemonizing

# 키워드 정리
* 설정파일 1 : `/etc/celery/celery.conf`

```bash
# Name of nodes to start
# here we have a single node
CELERYD_NODES="w1"
# or we could have three nodes:
#CELERYD_NODES="w1 w2 w3"

# Absolute or relative path to the 'celery' command:
# CELERY_BIN="/usr/local/bin/celery"
CELERY_BIN="/home/[username]/alms/venv/bin/celery"

# App instance to use
# comment out this line if you don't use an app
CELERY_APP="[appname]"
# or fully qualified:
#CELERY_APP="proj.tasks:app"

# How to call manage.py
CELERYD_MULTI="multi"

# Extra command-line arguments to the worker
CELERYD_OPTS="--time-limit=300 --concurrency=8"

# - %n will be replaced with the first part of the nodename.
# - %I will be replaced with the current child process index
#   and is important when using the prefork pool to avoid race conditions.
CELERYD_PID_FILE="/var/run/celery/%n.pid"
CELERYD_LOG_FILE="/var/log/celery/%n%I.log"
CELERYD_LOG_LEVEL="INFO"```

*  설정파일 2 : `/etc/systemd/system/celery.service`

```bash
[Unit]
Description=Celery Service
After=network.target

[Service]
Type=forking
User=celery
Group=celery
EnvironmentFile=-/etc/celery/celery.conf
WorkingDirectory=/home/[username]/[app location]
ExecStart=/bin/sh -c '${CELERY_BIN} multi start ${CELERYD_NODES} \
  -A ${CELERY_APP} --pidfile=${CELERYD_PID_FILE} \
  --logfile=${CELERYD_LOG_FILE} --loglevel=${CELERYD_LOG_LEVEL} ${CELERYD_OPTS}'
ExecStop=/bin/sh -c '${CELERY_BIN} multi stopwait ${CELERYD_NODES} \
  --pidfile=${CELERYD_PID_FILE}'
ExecReload=/bin/sh -c '${CELERY_BIN} multi restart ${CELERYD_NODES} \
  -A ${CELERY_APP} --pidfile=${CELERYD_PID_FILE} \
  --logfile=${CELERYD_LOG_FILE} --loglevel=${CELERYD_LOG_LEVEL} ${CELERYD_OPTS}'

[Install]
WantedBy=multi-user.target
```

* create user and group : `celery`
commands
  * manage user
    * view user list 
    ```
    $ sudo cat /etc/passwd
    ```
    * create new user and add to some group 
    ```
    $ sudo adduser username grouptoadd
    ```
  * manage group
    * view group list 
    ```
    $ sudo cat /etc/group
    ```
    * create new group
    ```
    $ sudo groupadd group1
    ```
    * delete group
    ```
    $ sudo groupdel group1
    ```
  * change owner:group
  ```
  $ sudo chown [new_user]:[new_group] celery/
  ```