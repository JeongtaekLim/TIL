# 특정 문자열을 포함하는 record 필터
```
SELECT * FROM mytable
WHERE column1 LIKE '%word1%'
   OR column1 LIKE '%word2%'
   OR column1 LIKE '%word3%'
```