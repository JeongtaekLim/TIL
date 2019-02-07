# Introduction
기본적인 Docker 명령어에 대한 요약입니다.

## Build
### docker build from specific file
```
$ docker build -t XXX --file `pwd`/Dockerfile `pwd`
```

## Container
### 실행중인 container 조회
```
// a means all containers, default shows just running
docker ps -a
```

### 실행중인 container에서 bash 실행(내장된 shell 종류에 따라 약간 상이)
```
docker exec -it [container id] /bin/bash
docker exec -it [container id] /bin/sh
```

### 모든 컨테이너 삭제
```
docker rm $(docker ps -aq)
```

