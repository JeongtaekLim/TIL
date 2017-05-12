# Manage Tasks

## Create
In `views.py`, below code will create new celery task and send to message queue.

Don't forget to store result's id to kill that
```
result = some_task.delay(arg1, arg2, ...)
```

## Kill
When you want to kill some celery task ongoing, you should have its id.
`revoke()` method can kill celery task.
```
celery_app.control.revoke(task_id, terminate=True)
celery_app.control.revoke(task_id, terminate=True, signal='SIGKILL')
```