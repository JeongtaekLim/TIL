```
/home/__user/compilebox/API/DockerTimeout.sh 20s -u mysql -e 'NODE_PATH=/usr/local/lib/node_modules' -i -t -v  "/home/__user/compilebox/API/temp/1870302ea341a736bb39":/usercode virtual_machine /usercode/script.sh python file.py
```

# run

## run container
```
$ sudo docker run -i -t --name hello ubuntu /bin/bash
$ sudo docker run -i -t ubuntu /bin/bash
```
* `--name` : assign new name
* `-i` + `-t`: interactive + Pseudo-tty, you can use container's bash
* `-v`:
-v, --volume=[]: 데이터 볼륨을 설정입니다. 호스트와 공유할 디렉터리를 설정하여 파일을 컨테이너에 저장하지 않고 호스트에 바로 저장합니다. 호스트 디렉터리 뒤에 :ro, :rw를 붙여서 읽기 쓰기 설정을 할 수 있으며 기본 값은 :rw입니다. 자세한 내용은 ‘6.4 Docker 데이터 볼륨 사용하기’를 참조하기 바랍니다.
    - `<컨테이너 디렉터리>` 예) `-v /data`
    - `<호스트 디렉터리>:<컨테이너 디렉터리>` 예) `-v /data:/data`
    - `<호스트 디렉터리>:<컨테이너 디렉터리>:<ro, rw>` 예) `-v /data:/data:ro`
    - `<호스트 파일>:<컨테이너 파일>` 예) `-v /var/run/docker.sock:/var/run/docker.sock`
    
출처 : [pyrasis.com](http://pyrasis.com/book/DockerForTheReallyImpatient)

for more information about run command, please look [pyrasis.com](http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter20/28)