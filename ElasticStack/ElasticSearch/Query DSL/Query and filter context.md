# Introduction
query clause는 `query context` `filter context`에 따라 다르게 동작한다.

## Query context
query clause는 "이 document가 얼마나 query clause와 잘 매치됩니까?" 라는 질문에 대한 답으로 `query context`에서 사용된다.
`query context`에서는 `_score`가 계산되며, 이는 다른 document에 비해서 얼마나 상대적으로 query clause에 잘 매칭되는지를 나타냅니다.

## Filter context
`filter context`에서는, query clause는 "이 document는 이 query clause의 조건을 만족합니까?"로 사용된다. 그저 Yes or No이다. 스코어는 계산되지 않는다. `timestamp`는 2015 에서 2016 사이입니까? `status` 필드는 `"published"` 입니까? 등에서 사용된다.
