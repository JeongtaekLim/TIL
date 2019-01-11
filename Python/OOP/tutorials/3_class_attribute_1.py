# -*- coding: utf-8 -*-


class Employee:

    raise_amount = 1.1  # 1 클래스 변수 정의

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # 2 클래스 변수 사용


emp_1 = Employee('Sanghee', 'Lee', 50000)

class_of_emp_1 = emp_1.__class__
print('------ class part -------')
print('>>> dir(class_of_emp_1)')
print(dir(class_of_emp_1))
print('>>> id(class_of_emp_1)')
print(id(class_of_emp_1))
print('>>> id(Employee)')
print(id(Employee))
print('>>> id(c.raise_amount)')
print(id(class_of_emp_1.raise_amount))
print('------ object part -------')
print('>>> dir(emp_1)')
print(dir(emp_1))
print('>>> id(emp_1)')
print(id(emp_1))
print('>>> id(emp_1.raise_amount)')
print(id(emp_1.raise_amount))

emp_1.raise_amount = 0
print('>>> id(emp_1.raise_amount)')
print(id(emp_1.raise_amount))
print(Employee.raise_amount)

print('연봉출력')
print(emp_1.pay)  # 기존 연봉
emp_1.apply_raise()  # 인상률 적용
print(emp_1.pay)  # 오른 연봉
