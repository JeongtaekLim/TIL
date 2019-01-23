# Problem
채점하는 task, 컴파일&실행 하는 task, 시험종료 점검 task, 등 알고리즘랩스 서비스에는 여러가지 celery task가 존재한다.
이때, 1개의 celery queue와 4개의 worker를 운영중이라고 가정해보자.
하필이면 오래걸리는 무한루프 코드를 4개 연달아 제출 받은 경우, 4개의 가용한 worker는 모두 채점코드를 수행하느라 worker가 남아있지 않을 것이다.
이런 상황에서 시험종료 task는 매 1초마다 수행되어야 하는데, 남아있는 worker가 존재하지 않으므로 수행될 수 없다.

# Solution
## Introduction
여러개의 queue를 독립적으로 운영함으로써 이 문제를 해결가능하다.
문서에서는 [celery routing](http://docs.celeryproject.org/en/latest/userguide/routing.html) 라는 명칭을 사용한다.


## Routing example
```
task_routes = {'feed.tasks.import_feed': {'queue': 'feeds'}}
```
```
app.conf.update({
    'task_routes': {
        'qjudge.tasks.compile_run_task': {'queue': 'compile_run'},
        'qjudge.tasks.submission_task': {'queue': 'submission'},
        'othersite_linker.tasks.run_other_user_register_bot': {'queue': 'run_other_user_register_bot'}
    }
})
```