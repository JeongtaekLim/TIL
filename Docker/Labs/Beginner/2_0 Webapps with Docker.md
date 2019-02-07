# 2.0 Webapps with Docker

```
$ docker run -d dockersamples/static-site
```
> Note: The current version of this image doesn't run without the -d flag. The -d flag enables detached mode, which detaches the running container from the terminal/shell and returns your prompt after the container starts. We are debugging the problem with this image but for now, use -d even for this first example.

```
$ docker run --name static-site -e AUTHOR="Your Name" -d -P dockersamples/static-site
e61d12292d69556eabe2a44c16cbd54486b2527e2ce4f95438e504afb7b02810
```
In the above command:

* `-d` will create a container with the process detached from our terminal
* `-P` will publish all the exposed container ports to random ports on the Docker host
* `-e` is how you pass environment variables to the container
* `--name` allows you to specify a container name
* `AUTHOR` is the environment variable name and Your Name is the value that you can pass

Now you can see the ports by running the `docker port` command.
```
$ docker port static-site
443/tcp -> 0.0.0.0:32772
80/tcp -> 0.0.0.0:32773
```

```
$ docker run --name static-site-2 -e AUTHOR="Your Name" -d -p 8888:80 dockersamples/static-site
```

```dockerfile
FROM ubuntu:18.04
ADD . /app
WORKDIR /app
# install things
RUN apt-get update && apt-get install -y python python-dev python3 python3-dev python-pip virtualenv libssl-dev libpq-dev git build-essential libfontconfig1 libfontconfig1-dev
RUN virtualenv venv -p python3
```

```
$ docker build -t <YOUR_USERNAME>/myfirstapp .
```