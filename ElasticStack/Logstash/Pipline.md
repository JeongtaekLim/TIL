# Pipline

## pipeline.yml Example
```
- pipeline.id: alms_back_dev_pipeline
  path.config: "/etc/logstash/conf.d/alms-back-dev2.conf"
- pipeline.id: used-car-rds-pipeline
  path.config: "/etc/logstash/conf.d/used-car-rds.conf"
```

## Run with pipeline.yml
`pipeline.yml` 파일이 위치하는 경로를 `--path.settings` 옵션으로 지정

```
$ logstash --path.settings /etc/logstash/
```