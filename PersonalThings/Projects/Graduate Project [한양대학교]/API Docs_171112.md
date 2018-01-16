# APIDocs

* localhost:8000의 부분은 따로 전달된 [IP address]:[port]로 수정하여 사용해주시기 바랍니다.


## Simulation
Simulation 관련 API는 EMA 실물을 받음에 따라 사용하지 않는다.
(내부 개발용으로 관리자만 사용할 것을 권장한다.)

## OEMS, EMS, Device 조회

### OEMS 조회 [__GET__]
* url
```
http://localhost:8000/oems/list/
```
* params

| 필드명                 | 유효값          | 예시               | 비고                      |
|----------------------|---------------|-------------------|--------------------------|
| __[선택]__ include_ems | true<br>false | include_ems=true  | 대소문자 상관없음             |

* request example
```
http://localhost:8000/oems/list/
http://localhost:8000/oems/list/?include_ems=true
http://localhost:8000/oems/list/?include_ems=false
```
* response
```json
[
    {
        "id": 1,
        "name": "Hanyang University",
        "created": "2017-10-07T11:56:23.505625Z"
    },
    {
        "id": 2,
        "name": "NuriGgoom",
        "created": "2017-10-07T11:58:07.631718Z"
    }
]
```
```json
[
    {
        "id": 1,
        "emss": [
            {
                "id": 1,
                "name": "MIR Lab",
                "gateway": 2,
                "created": "2017-10-07T11:57:26.907484Z",
                "oems": 1
            }
        ],
        "name": "Hanyang University",
        "created": "2017-10-07T11:56:23.505625Z"
    },
    {
        "id": 2,
        "emss": [
            {
                "id": 2,
                "name": "Simulation",
                "gateway": 777,
                "created": "2017-10-07T11:58:15.560823Z",
                "oems": 2
            }
        ],
        "name": "NuriGgoom",
        "created": "2017-10-07T11:58:07.631718Z"
    }
]
```
-------------
### EMS 조회 [__GET__]
* url
```
http://localhost:8000/ems/list/
```
* params

| 필드명              | 유효값          | 예시               | 비고                      |
|-------------------|---------------|-------------------|--------------------------|
| __[필수]__ oems_id | 자연수          | oems_id=1  | 현재 존재하는 oems에 속해있는 ems 반환          |

* request example
```
http://localhost:8000/ems/list/?oems_id=1
```
* response
```json
[
    {
        "id": 1,
        "name": "MIR Lab",
        "gateway": 2,
        "created": "2017-10-07T11:57:26.907484Z",
        "oems": 1
    }
]
```
-------------
### Device 조회 [__GET__]
* url
```
http://localhost:8000/device/list/
```
* params

| 필드명              | 유효값          | 예시               | 비고                      |
|-------------------|---------------|-------------------|--------------------------|
| __[필수]__ ems_id | 자연수          | ems_id=1  | 현재 존재하는 ems에 속해있는 device 반환          |

* request example
```
http://localhost:8000/ems/list/?ems_id=1
```
* response
```json
{
    "ess": [
        8
    ],
    "pv": [
        7
    ],
    "led": [
        1,
        2,
        3,
        4,
        5,
        9
    ]
}
```
-------------


## Monigoring
모니터링은 다음과 같이 구성되어 있다.(총 1개)

### 최근 로그 조회 [__GET__]
* url
```
http://localhost:8000/device/logs/recent/
```
* params

| 필드명    | 유효값     | 예시                | 비고                       |
|---------|-----------|-------------------|----------------------------|
| __[필수]__ oems_id   | 자연수     | oems_id=1  |                        |
| __[필수]__ ems_id    | 자연수     | ems_id=1   |                        |
| __[필수]__ num       | 자연수     | num=5    | 권장: 1~10                |
| __[선택]__ led_ids   | 자연수     | led_ids=1\|2\|3 | 권장: 하단참조          |
| __[선택]__ pv_ids    | 자연수     | pv_ids=1\|2    | 권장: 하단참조          |
| __[선택]__ ess_ids   | 자연수     | ess_ids=1\|2   | 권장: 하단참조          |

* 현재 유효 led, pv, ess id 목록

| EMS 이름    | LED                          | PV                | ESS                       | 비고 |
|------------|------------------------------|-------------------|----------------------------|----|
| MIR Lab    | 가상: 1, 2, 3, 4, 5<br>실제: 9     | 7                 | 8                       |  LED 실제(9) 제외하고 모두 가상값  |
| Simulation | 1, 2     |  1, 2  |      1, 2                   |  모두 가상값 |

* request example
```
http://localhost:8000/device/logs/recent/?oems_id=1&ems_id=1&num=1&led_ids=1|2|3|4|5&pv_ids=7&ess_ids=8
http://localhost:8000/device/logs/recent/?oems_id=1&ems_id=1&num=2&led_ids=1|2|3&pv_ids=7
http://localhost:8000/device/logs/recent/?oems_id=1&ems_id=1&num=2&led_ids=1
```

* response

> http://localhost:8000/device/logs/recent/?oems_id=1&ems_id=1&num=1&led_ids=1|2|3|4|5&pv_ids=7&ess_ids=8
```json
{
    "pv_logs": {
        "7": [
            {
                "id": 55540,
                "pvId": 7,
                "power": 83,
                "mode": 1,
                "priority": 0,
                "created": "2017-10-08T05:38:46.266821Z",
                "ems": 1
            }
        ]
    },
    "led_logs": {
        "1": [
            {
                "id": 59618,
                "device": 1,
                "state": 1,
                "dimming": 2,
                "priority": 0,
                "created": "2017-10-08T05:38:45.332721Z",
                "ems": 1
            }
        ],
        "2": [
            {
                "id": 59619,
                "device": 2,
                "state": 1,
                "dimming": 4,
                "priority": 1,
                "created": "2017-10-08T05:38:45.493547Z",
                "ems": 1
            }
        ],
        "3": [
            {
                "id": 59620,
                "device": 3,
                "state": 1,
                "dimming": 6,
                "priority": 2,
                "created": "2017-10-08T05:38:45.699544Z",
                "ems": 1
            }
        ],
        "4": [
            {
                "id": 59621,
                "device": 4,
                "state": 1,
                "dimming": 8,
                "priority": 3,
                "created": "2017-10-08T05:38:45.887783Z",
                "ems": 1
            }
        ],
        "5": [
            {
                "id": 59622,
                "device": 5,
                "state": 1,
                "dimming": 9,
                "priority": 4,
                "created": "2017-10-08T05:38:46.060965Z",
                "ems": 1
            }
        ]
    },
    "ess_logs": {
        "8": [
            {
                "id": 55546,
                "essId": 8,
                "mode": 0,
                "power": 0,
                "state": 0,
                "changedEnergy": 0,
                "capacity": 250000,
                "soc": 0,
                "volt": 270.1,
                "hz": 59.9,
                "created": "2017-10-08T05:38:46.441259Z",
                "ems": 1
            }
        ]
    }
}
```
> http://localhost:8000/device/logs/recent/?oems_id=1&ems_id=2&num=1&led_ids=1|2|3&pv_ids=7
```json
{
    "pv_logs": {
        "7": [
            {
                "id": 55540,
                "pvId": 7,
                "power": 83,
                "mode": 1,
                "priority": 0,
                "created": "2017-10-08T05:38:46.266821Z",
                "ems": 1
            },
            {
                "id": 55539,
                "pvId": 7,
                "power": 80,
                "mode": 1,
                "priority": 0,
                "created": "2017-10-08T05:38:40.824357Z",
                "ems": 1
            }
        ]
    },
    "led_logs": {
        "1": [
            {
                "id": 59618,
                "device": 1,
                "state": 1,
                "dimming": 2,
                "priority": 0,
                "created": "2017-10-08T05:38:45.332721Z",
                "ems": 1
            },
            {
                "id": 59612,
                "device": 1,
                "state": 1,
                "dimming": 2,
                "priority": 0,
                "created": "2017-10-08T05:38:39.971055Z",
                "ems": 1
            }
        ],
        "2": [
            {
                "id": 59619,
                "device": 2,
                "state": 1,
                "dimming": 4,
                "priority": 1,
                "created": "2017-10-08T05:38:45.493547Z",
                "ems": 1
            },
            {
                "id": 59613,
                "device": 2,
                "state": 1,
                "dimming": 4,
                "priority": 1,
                "created": "2017-10-08T05:38:40.158810Z",
                "ems": 1
            }
        ],
        "3": [
            {
                "id": 59620,
                "device": 3,
                "state": 1,
                "dimming": 6,
                "priority": 2,
                "created": "2017-10-08T05:38:45.699544Z",
                "ems": 1
            },
            {
                "id": 59614,
                "device": 3,
                "state": 1,
                "dimming": 6,
                "priority": 2,
                "created": "2017-10-08T05:38:40.301325Z",
                "ems": 1
            }
        ]
    }
}
```
> http://localhost:8000/device/logs/recent/?oems_id=1&ems_id=1&num=2&led_ids=1
```json
{
    "led_logs": {
        "1": [
            {
                "id": 59618,
                "device": 1,
                "state": 1,
                "dimming": 2,
                "priority": 0,
                "created": "2017-10-08T05:38:45.332721Z",
                "ems": 1
            },
            {
                "id": 59612,
                "device": 1,
                "state": 1,
                "dimming": 2,
                "priority": 0,
                "created": "2017-10-08T05:38:39.971055Z",
                "ems": 1
            }
        ]
    }
}
```
-----------------

## Control

### LED 전원 컨트롤 [__POST__]
* url
```
http://localhost:8000/device/control/
```
* params

| 필드명    | 유효값     | 예시                | 비고                       |
|---------|-----------|-------------------|----------------------------|
| __[필수]__ gateway_id   | 자연수     | gateway_id=1  |                        |
| __[필수]__ device_name    | 문자열     | device_name="LED"   |     LED, PV, ESS         |
| __[필수]__ device_id       | 자연수     | device_id=1    | 권장: 1~10                |
| __[선택]__ state   | 자연수     | state=0 | 0 또는 1          |

* 현재 유효 led, pv, ess id 목록

| EMS 이름    | LED                          | PV                | ESS                       | 비고 |
|------------|------------------------------|-------------------|----------------------------|----|
| MIR Lab(gateway_id: 2)    | 가상: 1, 2, 3, 4, 5<br>실제: 9     | 7                 | 8                       |  LED 실제(9) 제외하고 모두 가상값  |
| Simulation(gateway_id: 777) | 1, 2     |  1, 2  |      1, 2                   |  모두 가상값 |

* response

> http://localhost:8000/device/control/
```json
"success"
```