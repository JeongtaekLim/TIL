# Filebeat Installation

## apt-get
https://www.elastic.co/guide/en/beats/filebeat/6.5/setup-repositories.html

```
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-6.x.list
apt-get update && apt-get install filebeat
sudo update-rc.d filebeat defaults 95 10
```

## yum
https://www.elastic.co/guide/en/beats/filebeat/current/setup-repositories.html
