# Three ways comparison

https://hackernoon.com/elasticsearch-building-autocomplete-functionality-494fcf81a7cf

* Prefix Query
* Edge Ngram
* Completion Suggester

## Prefix Query
Prefix Query의 경우, 말그대로 전방매치 밖에 안된다.
`가나초콜릿` 의 경우, `초콜릿` 만 치면 `가나초콜릿`이 나오질 않는 것이다.
실용적으로 쓸모가 없으므로 배제

## Edge Ngram
ngram 알고리즘에 근거하는 방식이다. 아래 `Completion Suggester`보다 성능이 좋지 않다.
하지만, reindex하지 않아도 된다는 점에서 성능과 조금 타협을 보고 `Edge Ngram`을 사용해 보는 방향으로 리서치하기 시작

https://www.elastic.co/guide/en/elasticsearch/guide/master/_index_time_search_as_you_type.html

## Completion Suggester
- 세 가지 방법중에 자동완성기능을 위해 태어난 가장 좋은 방법이다. 하지만 index 생성 시점에 Completion type으로 Suggester를 운영해야 하므로 제외
- reindexing 하여, alias를 세팅해주는 방법으로 어렵지 않게 세팅할 수 있다.
https://www.elastic.co/kr/blog/you-complete-me
https://hackernoon.com/elasticsearch-using-completion-suggester-to-build-autocomplete-e9c120cf6d87

