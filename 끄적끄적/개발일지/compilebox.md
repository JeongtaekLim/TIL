# compilebox

## 1일 - 성능 테스트

compilebox의 강건함(?)을 테스트해보기 위해, 간단한 성능테스트를 진행해보았다. 세팅은 아래와 같다.

- server
    - ubuntu
    - Nginx
    - Django
    - celery
    - compilebox

- client
    - postman

방식은,
1. postman에서 Django로 http request
2. Django에서 celery로 task 전달 후 바로 response
3. celery에서 compilebox로 http request(테스트 케이스 별 요청)
4. 모든 테스트 케이스 요청 이후 celery task 종료

로 이루어 졌다.

결론부터 말하면, __망했다.__

[ 결과 ]
- 11테스트케이스, python

- 동시요청 1: 평균 8.5초 
- 동시요청 2:  평균 9.7초
- 동시요청 3: 평균 11초
- 동시요청 4: 평균 15초
- 동시요청 5: 평균 18초
- 동시요청 6: 평균 20초

심지어, 동시요청이 10개 이상일 경우 간혹 JSON 관련 에러도 발생한다. 굉장한데?
여기서 더 digging 하기보단, compilebox 구조 변경이 필요해 보인다.

## 2일차 - 문제 해결방안 구상

[ 문제점 1 ]

기존의 소스는 여러개의 테스트케이스에 대한 채점을 지원하지 않는다.

[ 해결방안 2 ]

input파일 들이 있는 특정 디렉토리를 지정하여 iterate하면서 결과물을 만들어야겠다.

[ 문제점 2 ]

기존 소스를 단순히 input파일들이 있는 디렉토리를 iterate하게끔 수정하면, 매번 iterate할때마다 build를 한다.

[ 해결방안 2 ]

이럴바엔 새로운 shell 스크립트를 짜서 아예 다른 방향으로 develop해야겠다.

[ 결론 ]

Docker 생성 및 돌리는 핵심 코드가 script.sh인 것을 파악해서, 소스를 수정해서 docker 운영하고자 합니다. 시간은 좀더 걸리겠으나 충분히 시간투자할 가치가 있다고 판단, shell script 공부해서 만드는 것으로 결론