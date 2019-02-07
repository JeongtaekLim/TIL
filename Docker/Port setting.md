# Docker port settting

### Expose
When writing your Dockerfiles, the instruction EXPOSE tells Docker the running container listens on specific network ports. This acts as a kind of port mapping documentation that can then be used when publishing the ports.
```
EXPOSE <port> [<port>/<protocol>...]
```
```
docker run --expose=1234 my_app
```
But EXPOSE will not allow communication via the defined ports to containers outside of the same network or to the host machine. To allow this to happen you need to publish the ports.

```
// `[host port]:[container port]`
docker run -p 80:80/tcp -p 80:80/udp my_app
```
In the above example, the first number following the -p flag is the host port, and the second is the container port.

These are the flags `-p` and `-P`, and they differ in terms of whether you want to publish one or all ports.