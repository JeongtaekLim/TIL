# Installation
[7.0 Docs link](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

## Java
To install Logstash, java should be installed first.
https://tecadmin.net/install-oracle-java-8-ubuntu-via-ppa/

## JAVA_HOME
Logstash installation also require JAVA_HOME env in system.
To set it, follow [here](https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_$JAVA_HOME_%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98_%EC%84%A4%EC%A0%95)

For checking, run
```
sudo env | grep JAVA_HOME
```

## Install
Follow it
[7.0 Docs link](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

## Run demo
If `logstash` command is not found, make symbolic link to `/usr/bin/logstash`
```
$ ln -s /usr/share/logstash/bin/logstash /usr/bin/logstash
```

## Edit Config
Absolutely if you run elasticsearch with Elastic Cloud, then you should edit `logstash-sample.conf` first.
