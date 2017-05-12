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
"'6f412d81-fc7b-4eed-a015-c83f642e432c' is created"
```
-----------------


### Publisher 조회 [__GET__]
* url & request
```
// 현재 active publisher 조회
http://localhost:8000/simulation/pub/list/?is_active=true
// 현재 inactive publisher 조회
http://localhost:8000/simulation/pub/list/?is_active=false
// 모두 조회
http://localhost:8000/simulation/pub/list/?is_active=all
```
* response
```json
[
  {
    "id": 12,
    "unique_id": "906c266b-68b6-4db2-993c-a0f5a640a9ae",
    "topic": "/test/asdf",
    "noise": 1,
    "low": 0,
    "high": 10,
    "created": "2017-05-12T05:43:33.267239Z",
    "is_active": false
  },
  {
    "id": 13,
    "unique_id": "6f412d81-fc7b-4eed-a015-c83f642e432c",
    "topic": "/test/asdf",
    "noise": 1,
    "low": 0,
    "high": 10,
    "created": "2017-05-12T05:43:48.527486Z",
    "is_active": false
  },
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
"'6f412d81-fc7b-4eed-a015-c83f642e432c' is killed"
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
"Total num of 6 tasks are killed"
```

---------------

### Publisher 삭제 [__DELETE__]

active여부에 상관없이 모든 publisher를 삭제합니다.

* url
```
http://localhost:8000/simulation/pub/kill/all/
```
* request
no body data is required

* response
```
"Total num of 6 tasks are deleted"
```

