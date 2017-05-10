# Remote Code Edit
## Environment
* vscode
* ubuntu 16.06
* osx sierra

## Vscode - install
install remote-vscode.
at this point, the most import concept is 'server is your local machine(osx).'
so, in your local machine(osx) vscode preference is below.
```
"remote.host": "127.0.0.1",
"remote.onstartup": false,
```

## Ubuntu - install and setup
install rmate.
```
$ sudo wget -O /usr/local/bin/rmate 
$ https://raw.github.com/aurora/rmate/master/rmate
$ sudo chmod a+x /usr/local/bin/rmate
```

remote server(ubuntu) is your(osx) client at this time.

* caution - this tip is not stable!

if you are using some other port for ssh, please try change some conde in `/etc/ssh/ssh_config`, `port=22`

Then all setup is completed, so ready to go.1

## Vscode - start server
by typing F1 in vscode, and searching 'remote', you can get menu `start server`
this means, make your local machine(osx) run as server.

## OSX - run command
run below command. this command mean, you make tunnel. it's result is same as just ssh connect command.
```
ssh -p [some remote server(ubunt)'s ssh port] -R 52698:localhost:52698 [username]@[remote address]
```

## Ubuntu - run command
```
rmate [some file you want]
```

## Error
If you get no response from
```
rmate [some file]
```
then, 
```
sudo netstat -plant  | grep 52698
```
and
```
sudo kill -9 xxxx
```
It works well!