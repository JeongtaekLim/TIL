# Celery Run

```
celery -A proj worker -l info
celery -A proj worker --loglevel=INFO --concurrency=10 -n worker1@%h &
```

# Celery Kill
```
pkill -9 'celery worker'
```