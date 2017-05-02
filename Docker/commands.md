```
/home/__user/compilebox/API/DockerTimeout.sh 20s -u mysql -e 'NODE_PATH=/usr/local/lib/node_modules' -i -t -v  "/home/__user/compilebox/API/temp/1870302ea341a736bb39":/usercode virtual_machine /usercode/script.sh python file.py
```

# commands

## container list
```
$ sudo docker ps
```
* `-a` : list all containers including stoped docker

## run container
```
$ sudo docker run -i -t --name hello ubuntu /bin/bash
```
* `--name` : assign new name
* `-i` + `-t`: interactive + Pseudo-tty, you can use container's bash