# Date

### 년, 월 출력하기

```
Date := A_Now
Date += -90,D
FormatTime Date, %Date%, MM yyyy
msgbox about to send %date%
send %date%
Sleep, 100
return
```

### 년, 월 파싱하기

```
str = " 00121"
MsgBox %str%
str := str + 100
MsgBox %str%
```
