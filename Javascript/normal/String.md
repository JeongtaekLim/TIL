# String
## toString
```js
var a = 1
a.toString()
```
## replace

```js
// #를 공백으로 변경한다.
str.replace("#",""); 
```

하지만, 이는 첫 번째 등장하는 '#' 만 바꿀뿐이다.
모든 '#'을 교체하기 위해서는 아래 코드를 사용한다.

```js
// #를 감싼 따옴표를 슬래시로 대체하고 뒤에 gi 를 붙이면 
// replaceAll 과 같은 결과를 볼 수 있다.
str.replace(/#/gi, "");
```

* g : 발생할 모든 pattern에 대한 전역 검색
* i : 대/소문자 구분 안함
* m: 여러 줄 검색 (참고)

출처 : [codejs](http://www.codejs.co.kr/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EC%97%90%EC%84%9C-replace%EB%A5%BC-replaceall-%EC%B2%98%EB%9F%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/)