# Basic usages
### 특정 숫자를 string으로 변환하고 싶을 때
보통 `atoi`, `itoa`를 사용하는 경우가 있지만, 이는 표준함수가 아니다.
아래와 같은 형식으로 `buf`에 `a`를 문자열로 넣을 수 있다.
```c
char buf[100];
int a = 123;
sprintf(buf, "%d", a);
```

### Find location of the string in a string
```c
#include <string.h>
char s[] = "this is my 1'st string"
char* p1 = &s[0];
char* p2 = strstr(s, "1");
prinf("%d", p2-p1);
```