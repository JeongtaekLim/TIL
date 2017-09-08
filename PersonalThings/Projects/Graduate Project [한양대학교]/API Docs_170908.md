# APIDocs

localhost:8000의 부분은 따로 전달된 [IP address]:[port]로 수정하여 사용해주시기 바랍니다.


## Simulation
Publisher 생성, 상태조회, 종료

--------------
### Publisher 생성 [__POST__]
* url
```
http://localhost:8000/simulation/pub/create/
```
* request
```json
{
  topic:"/test/asdf",
  noise:"1",
  low:"0",
  high:"10"
}
```
`noise`, `low`, `high` 필드는 publisher의 정해진 범위 내에서 일정한 추세(?)선을 지니는 값을 만들기 위해 사용되는 파라미터 들입니다.

range(low, high)의 범위로 오르락내리락 하며,random.uniforn(-noise, noise)의 값을 더하여 나오는 값을 주어진 topic으로 publish합니다.
* response
```
"6f412d81-fc7b-4eed-a015-c83f642e432c"
```
-----------------


### Publisher 조회 [__GET__]
* url & request
```
// 현재 active publisher 조회
http://localhost:8000/simulation/pub/list/
```
* response
```json
[
    "3200e948-03eb-447d-b738-1bf20c0fa3e9",
    "906c266b-68b6-4db2-993c-a0f5a640a9ae"
]
```
-----------


### Publisher 종료 [__POST__]

단일 종료, 전체 종료 2가지 API가 존재합니다.



* url - 단일 종료
```
http://localhost:8000/simulation/pub/kill/
```
* request
```json
{
  unique_id:"6f412d81-fc7b-4eed-a015-c83f642e432c"
}
```
* response
```
"6f412d81-fc7b-4eed-a015-c83f642e432c"
```

```
invalid id // 400 Bad Request
```
-------------------

* url - 전체 종료
```
http://localhost:8000/simulation/pub/kill/all/
```
* request
no body data is required

* response
```
[
    "a01da1c2-8954-4b18-8d55-fb2940b91a50",
    "ee054c27-09ea-4ae8-b158-687d01b226d9",
    "e60e139f-a810-4763-8346-ae91c63e0669"
]
```

---------------