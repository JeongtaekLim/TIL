# Url vs Uri

출처: https://blog.lael.be/post/61

### URI

서버 리소스 이름은 통합 자원 식별자(uniform resource identifier) 혹은 URI라고 불린다.

1. rewrite 기술을 사용하여 만든 의미있는 식별자
   > http://test.com/company/location
2. REST 서비스 (url로 실행되는 서비스)
   > http://service.com/tv/turn/on
3. Web-oriented architecture (웹 기반의 구조문법)

   > kakaotalk://sendmsg?text=hello!

   이 uri는 kakaotalk 프로토콜을 해석할 수 있는 프로그램이 핸들링한다. 해당프로그램은 sendmsg 라는 식별자를 해석하고 동작한다.

### URL

통합 자원 지시자(uniform resource locator, URL)는 URI의 가장 흔한 형태이다.
요약하자면 URL 은 다음과 같다.

> http://test.com/work/sample.pdf

test.com 서버에서 work 폴더안의 sample.pdf 를 요청하는 URL.
