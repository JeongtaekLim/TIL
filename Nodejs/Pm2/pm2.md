# pm2
To deploy node app in background, pm2 is recommend.
[Digital Ocean, Tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-node-js-application-for-production-on-ubuntu-14-04)

Before install & run pm2, please check your server's node js status

```
$ node -v 
// v0.10.24
```

If node is not installed on server, please install following [Digital Ocean, Node install](https://www.digitalocean.com/community/tutorials/how-to-use-pm2-to-setup-a-node-js-production-environment-on-an-ubuntu-vps)
```
$ sudo apt-get install build-essential
$ sudo apt-get install curl openssl libssl-dev
$ git clone https://github.com/joyent/node.git
$ cd node
$ git checkout v0.10.24
$ ./configure
$ make
$ sudo make install
```

Afterthat, just run app.js by type command as below
```
$ sudo pm2 start app.js
```

The result is..lol...
```
                        -------------

                      PM2 process manager

__/\\\\\\\\\\\\\____/\\\\____________/\\\\____/\\\\\\\\\_____
 _\/\\\/////////\\\_\/\\\\\\________/\\\\\\__/\\\///////\\\___
  _\/\\\_______\/\\\_\/\\\//\\\____/\\\//\\\_\///______\//\\\__
   _\/\\\\\\\\\\\\\/__\/\\\\///\\\/\\\/_\/\\\___________/\\\/___
    _\/\\\/////////____\/\\\__\///\\\/___\/\\\________/\\\//_____
     _\/\\\_____________\/\\\____\///_____\/\\\_____/\\\//________
      _\/\\\_____________\/\\\_____________\/\\\___/\\\/___________
       _\/\\\_____________\/\\\_____________\/\\\__/\\\\\\\\\\\\\\\_
        _\///______________\///______________\///__\///////////////__


                       Getting started

                        Documentation
                        http://pm2.io/

                      Start PM2 at boot
                        $ pm2 startup

                     Daemonize Application
                       $ pm2 start <app>

                     Monitoring/APM solution
                    https://app.keymetrics.io/

                        -------------

[PM2] Spawning PM2 daemon with pm2_home=/home/jtlim/.pm2
[PM2] PM2 Successfully daemonized
[PM2] Starting /home/jtlim/compilebox/API/app.js in fork_mode (1 instance)
[PM2] Done.
┌──────────┬────┬──────┬──────┬────────┬─────────┬────────┬─────┬───────────┬──────────┐
│ App name │ id │ mode │ pid  │ status │ restart │ uptime │ cpu │ mem       │ watching │
├──────────┼────┼──────┼──────┼────────┼─────────┼────────┼─────┼───────────┼──────────┤
│ app      │ 0  │ fork │ 8775 │ online │ 0       │ 0s     │ 73% │ 24.6 MB   │ disabled │
└──────────┴────┴──────┴──────┴────────┴─────────┴────────┴─────┴───────────┴──────────┘
 Use `pm2 show <id|name>` to get more details about an app
```

## With npm start
If you want to run pm2 with `npm start`, just
```
pm2 start npm -- start
```
In case of next.js(based on [Next.js Issues](https://github.com/zeit/next.js/issues/109))
```
# for development
pm2 start npm --name "next" -- run dev

# for production
npm run build
pm2 start npm --name "next" -- start
```

## Run pm2 as service
please look

[Digital Ocean - How To Use PM2 to Setup a Node.js Production Environment On An Ubuntu VPS](https://www.digitalocean.com/community/tutorials/how-to-use-pm2-to-setup-a-node-js-production-environment-on-an-ubuntu-vps)