# APIDocs

* localhost:8000의 부분은 따로 전달된 [IP address]:[port]로 수정하여 사용해주시기 바랍니다.


## Simulation
Simulation 관련 API는 EMA 실물을 받음에 따라 사용하지 않는다.
(내부 개발용으로 관리자만 사용할 것을 권장한다.)

## Monigoring
모니터링은 다음과 같이 구성되어 있다.(총 1개)
* LED, PV, ESS 가장 최근 10개 log 조회

--------------
### 최근 로그 조회 [__GET__]
* url
```
http://localhost:8000/device/logs/recent/
```
* params

| 필드명    | 유효값     | 예시                | 비고                      |
|---------|-----------|-------------------|--------------------------|
| selectors | led pv ess | selectors=led\|pv<br>selectors=ess<br>selectors=led\|ess\|pv | 대소문자 상관없음 순서 상관없음 구분자 : \| ('or' character) |
| num       | 자연수     | num=20   | 권장: 1~20                         |

* response
```json
{
    "ess_logs": [
        {
            "id": 129,
            "gateway": "gw/777",
            "essId": 1,
            "mode": 1,
            "power": 6.45576425377521,
            "state": 0,
            "changedEnergy": 0,
            "capacity": 0,
            "soc": 0,
            "volt": 0,
            "hz": 0,
            "created": "2017-10-05T06:08:43.618613Z"
        }
    ],
    "led_logs": [
        {
            "id": 514,
            "gateway": "gw/777",
            "device": 1,
            "state": 1,
            "dimming": 6,
            "priority": 0,
            "created": "2017-10-05T06:08:43.088442Z"
        }
    ],
    "pv_logs": [
        {
            "id": 129,
            "gateway": "gw/777",
            "pvId": 1,
            "power": 6.45576425377521,
            "mode": 0,
            "priority": 0,
            "created": "2017-10-05T06:08:43.347681Z"
        }
    ]
}
```
-----------------

