# Reindex
```
POST _reindex
{
  "source": {
    "index": "twitter"
  },
  "dest": {
    "index": "new_twitter"
  }
}
```
* Create new index
* Set Alias
* Remove original index

https://www.elastic.co/kr/blog/changing-mapping-with-zero-downtime

## Create new index
```
PUT my_new_index
{
    "mappings": { blabla... },
    "settings": { blabla... }
}
```

## Set Alias
```
POST /_aliases
{
  "actions": [
    {
      "add": {
        "index": "used_car_0510_1603",
        "alias": "used_car_latest"
      },
      "remove":{
        "index: "abcd",
        "alias": "my_alias"
      }
    }
  ]
}
```
