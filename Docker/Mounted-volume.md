# Show mounted volume list of docker containers

```
$ docker inspect -f '{{ .Mounts }}' containerid
```
