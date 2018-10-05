# Environment

Environment는 Postman에서 monitoring, 및 기타 API 테스트시 매우 유용하게 쓰인다.
[local] 회원가입, [remote] 회원가입 등으로 메뉴를 구분해서 url을 별도로 저장해서 사용하던 때가 부끄러울정도로..

* local
```
server-url: http://localhost:8000
jwt-token: local 서버의 token
```
* develop
```
server-url: http://개발서버url
jwt-token: 개발서버의 token
```

