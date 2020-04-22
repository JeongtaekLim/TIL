# Basics

```java
Calendar curCal = Calendar.getInstance();

SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'", Locale.ENGLISH);
try {
    curCal.setTime(format.parse(startISO)); // 2019-12-17T19:58:00Z
    // if clone이 필요한 경우
    // Calendar newCal = (Calendar) curCal.clone();
} catch (ParseException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}

```

# 비교

```java
Calendar c1 = Calendar.getInstance();
Calendar c2 = Calendar.getInstance();
c1.compareTo(c2);
```

만약, c2보다 c1이 과거이면, return 음수
