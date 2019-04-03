# Introduction

파이썬은 Java와는 다르게, multi-inheritance를 지원하는 언어이다.

이를 구현하기 위해, MRO(Method Resolution Order)를 따른다.

MRO란, Derived class에서 Super class의 method를 호출할 때, 어떤 method를 호출 할 지 정하는 것을 칭한다.

아래 상황을 가정했을 때,
```
# -*- coding: utf-8 -*-
class A:
    def __init__(self, a=111, *args, **kwargs):
        self.a=a
        print("This is A")
        print(self.a)
class B:
    def __init__(self, b=222, *args, **kwargs):
        self.b=b
        print("This is B")
        print(self.b)

class C(A, B):
    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        super().__init__(a=1, b=2, c=3)
```

class `C`의 super().__init__(a=1, b=2, c=3) 은 MRO(['C', 'A', 'B', 'object'])에 따라 class `A`의 __init__을 호출하고 끝난다.