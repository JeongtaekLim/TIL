# Terms Aggregation
> By default, the terms aggregation will return the buckets for the top ten terms ordered by the doc_count. One can change this default behaviour by setting the size parameter.

기본으로, term aggregation은 top 10개의 bucket만 보여준다.
1.0까지는 아래와 같이 `"size": 0`을 통해 해결가능했지만,
2.0부터는 메모리이슈로 인해 `1` to `2147483647` 값중 1개로 explicit 하게 남겨야 한다.
```
GET /used_car/_search
{
  "size": 0,
  "aggs" : {
      "tictoc" : {
          "terms" : {
            "field" : "brand.keyword",
            "size": 0
          }
      }
  }
}
```

https://stackoverflow.com/questions/22927098/show-all-elasticsearch-aggregation-results-buckets-and-not-just-10
