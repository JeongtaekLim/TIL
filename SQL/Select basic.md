# 특정 문자열을 포함하는 record 필터
```
SELECT * FROM mytable
WHERE column1 LIKE '%word1%'
   OR column1 LIKE '%word2%'
```
대소문자를 무시하고 싶다면
```
SELECT * FROM mytable
WHERE upper(column1) LIKE '%WORD1%'
   OR lower(column1) LIKE '%word2%'
```
특정 글자로 시작하는 조건을 걸고싶다면
```
SELECT * FROM mytable
WHERE upper(column1) LIKE 'WORD1%'
```
특정 글자로 끝나는 조건
```
SELECT * FROM mytable
WHERE upper(column1) LIKE '%WORD1'
```