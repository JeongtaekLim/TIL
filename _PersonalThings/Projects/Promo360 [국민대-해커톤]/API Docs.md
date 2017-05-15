# APIDocs

## __버튼 클릭 이벤트__

### 신규등록 [ POST ]
* url
```
http://localhost:8000/record/button_click_evt/create/
```
* request
```json
{
  "uuid":"first_uuid",
  "promotion_id":"1",
  "button_id":"1",
}
```
* response
```json
{
  "id": 4,
  "created": "2017-05-13T01:20:34.665943Z",
  "profile": 2,
  "promotion": "1",
  "button": "1"
}
```
--------------
## __아이트랙킹 이벤트__

### 신규등록 [ POST ]

* url
```
http://localhost:8000/record/button_click_evt/create/
```
* request
```json
{
  "uuid":"first_uuid",
  "promotion_id":1,
  "button_id":1,
  "started":"2017-5-13T11:00:00Z",
  "ended":"2017-5-13T11:30:00Z"
}
```
* response
```json
{
  "id": 5,
  "created": "2017-05-13T02:12:16.702403Z",
  "started": "2017-05-13T11:00:00Z",
  "ended": "2017-05-13T11:30:00Z",
  "profile": 2,
  "promotion": "1",
  "button": "1"
}
```
-------
## __유저__

### 신규등록 [ POST ]
* url

```
http://localhost:8000/account/profile/create
```
* request
```json
{
  "uuid":"second_uuid",
  "age":25,
  "gender":"male", // should be in ['male', 'female']
  "region_id":1,
  "promotion_id":1
}

```
* response

```json
{
  "id": 3,
  "uuid": "second_uuid",
  "age": 25,
  "gender": "male",
  "region": "1"
}
```
-------

## 지역

### 조회 [ GET ]
* url
```
http://localhost:8000/account/region/list
```
* request

no data required

* response
```json
[
  {
    "id": 1,
    "name": "서울"
  }
]
```

