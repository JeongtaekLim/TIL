# Cross Field Completion

- https://qbox.io/blog/multi-field-partial-word-autocomplete-in-elasticsearch-using-ngrams
- https://opensourceconnections.com/blog/2015/05/27/deep-dive-into-elasticsearch-cross-field-search/
- https://opensourceconnections.com/blog/2015/05/27/deep-dive-into-elasticsearch-cross-field-search/

## Example

아래정보를 담고있는 document를 가정해보자

```json
{
  "title": "Amanda",
  "year": 2016
}
```

단순 검색의 경우, `title`, `year`에 대해서 독립적인 검색밖에 안될것이다.

하지만, 실무에서는
검색어로 `A`를 쳐도 `Amanda 2016`이 나오길 원하며, `16`이라고 쳐도 `Amanda 16`이 제안되기를 바란다.

이를 위해 아래처럼 `nGram_analyzer`, `whitespace_analyzer`를 통해 검색하는 로직을 사용할 수 있다.

이때, 6.x 버전부터는 `_all`이 deprecated 되었으므로, `copy_to`를 사용해야 한다.

```json
curl -XPUT "http://localhost:9200/blurays" -d'
{
   "settings": {
      "analysis": {
    ...
      }
   },
   "mappings": {
      "movies": {
         "_all": {
            "index_analyzer": "nGram_analyzer",
            "search_analyzer": "whitespace_analyzer"
         },
         "properties": {
            "addToCartUrl": {
               "type": "string",
               "index": "no",
               "include_in_all": false
            },
            "format": {
               "type": "string",
               "index": "not_analyzed"
            },
            "genre": {
               "type": "string",
               "index": "not_analyzed"
            },
            "image": {
               "type": "string",
               "index": "no",
               "include_in_all": false
            },
            "mpaaRating": {
               "type": "string",
               "index": "not_analyzed",
               "include_in_all": false
            },
            "name": {
               "type": "string",
               "index": "not_analyzed"
            },
            "plot": {
               "type": "string",
               "index": "no",
               "include_in_all": false
            },
            "price": {
               "type": "double",
               "include_in_all": false
            },
            "quantityLimit": {
               "type": "integer",
               "include_in_all": false
            },
            "releaseDate": {
               "type": "date",
               "format": "yyyy-MM-dd"
            },
            "sku": {
               "type": "string",
               "index": "not_analyzed"
            },
            "studio": {
               "type": "string",
               "index": "not_analyzed"
            }
         }
      }
   }
}'
```
