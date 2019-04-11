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

class `C`의 super().\_\_init\_\_(a=1, b=2, c=3) 은 MRO(['C', 'A', 'B', 'object'])에 따라 class `A`의 \_\_init\_\_을 호출하고 한다.

만약, A와 B가 각각 특수한 서로 다른 일을 하고 있는 클래스이고

C는 A와 B의 동작을 모두 각각 수행하고 싶은 경우에는 super를 사용하면 안된다.

이런 경우에는 [Stackoverflow - Multiple inheritance in python3 with different signatures
](https://stackoverflow.com/questions/26927571/multiple-inheritance-in-python3-with-different-signatures) 에 따라, 

아래와 같이 self를 explicitly 하게 전달하여 \_\_init\_\_을 호출함으로써 문제를 해결 할 수 있다.

```
class A(object):
    def __init__(self, a, b):
        print('Init {} with arguments {}'.format(self.__class__.__name__, (a, b)))

class B(object):
    def __init__(self, q):
        print('Init {} with arguments {}'.format(self.__class__.__name__, (q)))

class C(A, B):
    def __init__(self):
        # Unbound functions, so pass in self explicitly
        A.__init__(self, 1, 2)
        B.__init__(self, 3)
```