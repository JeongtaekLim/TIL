# Location 블럭

네이버 사이트소유확인 관련 업무를 하는 중, nginx server 블록 내부의 location 블록을 이전 사용보다 정밀하게 다룰 기회가 있어 기록해본다.

아래 location 블록은 보이다시피 regex로 작성되어 있다.

- (none): If no modifiers are present, the location is interpreted as a prefix match. This means that the location given will be matched against the beginning of the request URI to determine a match.
- =: If an equal sign is used, this block will be considered a match if the request URI exactly matches the location given.
- ~: If a tilde modifier is present, this location will be interpreted as a case-sensitive regular expression match.
- ~\*: If a tilde and asterisk modifier is used, the location block will be interpreted as a case-insensitive regular expression match.
- ^~: If a carat and tilde modifier is present, and if this block is selected as the best non-regular expression match, regular expression matching will not take place.

대략 요약하면 위와 같고, 세부사항은 https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms 에서 참고가능하다.

regex 테스트는 https://regexr.com/ 여기서

```
server {
    ...

        location ~* (naver).*\.(html)$
        {
           root    /var/www/html;
        }
        location / {
           proxy_pass http://localhost:4000;
        }
}
```

## 테스트 가능 링크

https://nginx.viraptor.info/
