# Firt Class Function(퍼스트 클래스 함수)
출처: [파이썬 - 퍼스트클래스 함수, SCHOOL OF WEB](http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8D%BC%EC%8A%A4%ED%8A%B8%ED%81%B4%EB%9E%98%EC%8A%A4-%ED%95%A8%EC%88%98-first-class-function/)

퍼스트클래스 함수란, 프로그래밍 언어가 함수(function)을 first-class citizen으로 취급하는 것을 뜻한다. 쉽게 설명하자면, 함수 자체를 인자(argument)로써 다른 함수에 전달하거나 다른 함수의 결과값으로 리턴 할 수도 있고, 함수를 변후에 할당하거나 데이터 구조안에 저장할 수 있는 함수를 뜻합니다.

```py
# -*- coding: utf-8 -*-
def logger(msg):
    
    def log_message(): #1
        print 'Log: ', msg
    
    return log_message

log_hi = logger('Hi')
print log_hi # log_message 오브젝트가 출력됩니다.
log_hi() # "Log: Hi"가 출력됩니다.
```
이런 log_message와 같은 함수를 "클로저 (closure)"라고 부르며 클로저는 다른 함수의 지역변수를 그 함수가 종료된 이후에도 기억을 할 수가 있습니다.
