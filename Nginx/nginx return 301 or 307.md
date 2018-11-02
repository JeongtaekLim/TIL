# Proxy pass
Django server를 패치하는 와중에, 가용성은 유지하기 위해서 서버 2대를 운용하며, service 서버를 스리슬쩍 교체하는 상황이 생겼다.

이런 상황에서 Django service서버는 admin 주소로 a.com, b.com을 패치때마다 번갈아가며 사용한다. (이 둘은 ELB에 묶여있기 때문에 고정적으로 사용할 수밖에 없다.)

하지만, Django admin에 접근해야 하는 기타 매니저들도 존재하므로 a-b.com이라는 별도의 url을 만들고, a-b.com으로 접근하는 사용자는 패치때마다 return url을 nginx 레벨에서 유효한 서버로 돌림으로써 관리자페이지 접근에 대한 이슈를 없애고자 하였다.

하지만, 아래와같은 코드를 사용하여 클라이언트 브라우저의 캐싱으로 인한 잘못된 접근이 빈번하게 발생했다.

```
return 301 블라블라
```
위 코드는 브라우저가 캐싱하므로 자연스러운 현상이었다.
아래와같이 고침으로써 문제를 해결했다.

```
return 307 블라블라
```

### 10.3.8 307 Temporary Redirect
The requested resource resides temporarily under a different URI. Since the redirection MAY be altered on occasion, the client SHOULD continue to use the Request-URI for future requests. This response is only cacheable if indicated by a Cache-Control or Expires header field.

The temporary URI SHOULD be given by the Location field in the response. Unless the request method was HEAD, the entity of the response SHOULD contain a short hypertext note with a hyperlink to the new URI(s) , since many pre-HTTP/1.1 user agents do not understand the 307 status. Therefore, the note SHOULD contain the information necessary for a user to repeat the original request on the new URI.

If the 307 status code is received in response to a request other than GET or HEAD, the user agent MUST NOT automatically redirect the request unless it can be confirmed by the user, since this might change the conditions under which the request was issued.

출처 - https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.8


### Stackoverflow

Don't try to avoid 301 caching. If you don't want any user agent to cache your redirect, then simply don't use a 301 redirect. In other words, 301 caching is here to stay, and semantically, it's a permanent redirect, so if you're planning to change the destination URL, 301 is not the right status code to use. On the other hand, 307 responses are not cached by default.

출처 - https://stackoverflow.com/questions/9020162/avoiding-301-redirect-caching