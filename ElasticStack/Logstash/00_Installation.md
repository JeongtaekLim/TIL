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

## Install - logstash
Follow it
[7.0 Docs link](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

## Install - jdbc driver
```
apt-get install libmysql-java
```

## Run demo
If `logstash` command is not found, make symbolic link to `/usr/bin/logstash`
```
$ ln -s /usr/share/logstash/bin/logstash /usr/bin/logstash
```

## Edit Config
Absolutely if you run elasticsearch with Elastic Cloud, then you should edit `logstash-sample.conf` first.
```json
input {

  jdbc {

    jdbc_connection_string => "jdbc:mysql://dabase-endpoint-url"
    jdbc_user => "database_username"
    jdbc_password => "database_password"
    jdbc_driver_library => "/usr/share/java/mysql-connector-java-5.1.38.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    statement => "select * from my_table limit 10"
  }
}
output {
        amazon_es {
                hosts => ["https://elasticsearch-endpoint-url.com"]
                region => "my_region"
                index => "name_of_index"
                aws_access_key_id => 'my_access_key'
                aws_secret_access_key => 'my_secret_key'
                ssl => true
        }
}
```

## AWS security policy example
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::111111111111:user/this-is-user-arn",
          "arn:aws:iam::111111111111:role/cognito-arn"
        ]
      },
      "Action": "es:*",
      "Resource": "arn:aws:es:ap-northeast-2:111111111111:domain/my-elasticsearch/*"
    }
  ]
}
```