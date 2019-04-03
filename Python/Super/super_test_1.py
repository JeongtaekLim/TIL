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

if __name__ == "__main__":
    print("MRO:", [x.__name__ for x in C.__mro__])
    C(a=1, b=2, c=3)
    # args_test('A','B','C', d=1, e=2)