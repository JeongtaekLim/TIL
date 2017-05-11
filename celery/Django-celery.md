# Django-celery

## Install celery
```
$ pip install celery
```

## make `celery.py`
At proj/proj, make `celery.py` file
```
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

```

## Install django-celery-results
```
$ pip install django-celery-results
```

## edit settings.py
```
INSTALLED_APPS = [
    ...
    'django_celery_results',
]
# CELERY STUFF
CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Seoul'
CELERY_RESULT_BACKEND = 'django-db'
```

## Write tasks.py in your app directory
```
# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
```

## Edit `__init__.py` in proj directory
```
from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ['celery_app']
```

## test command
```
$ celery -A proj worker -l info
```
please see [documentation](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)

## Error
If you get error like
```
[2017-05-11 13:01:11,644: ERROR/MainProcess] Received unregistered task of type 'simulation.tasks.add'.
The message has been ignored and discarded.

Did you remember to import the module containing this task?
Or maybe you're using relative imports?

Please see
http://docs.celeryq.org/en/latest/internals/protocol.html
for more information.

The full contents of the message body was:
b'[[1, 1], {}, {"chord": null, "callbacks": null, "errbacks": null, "chain": null}]' (81b)
Traceback (most recent call last):
  File "/Users/jtlim/Desktop/03_GraduationProject/00_mango-back/venv/lib/python3.5/site-packages/celery/worker/consumer/consumer.py", line 559, in on_task_received
    strategy = strategies[type_]
KeyError: 'simulation.tasks.add'
```
Then please check your `INSTALLED_APPS` in `settings.py`.

If you forget to add your new app to `INSTALLED_APPS`, that error will occur.