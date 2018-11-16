# Question list

```py
class Human:
    def __init__(self, age=1):
        print("Human, __init__ start")
        self.age = age
        print("Human, __init__ end")

    def show(self):
        print("Human, age: {}".format(self.age))


class Employee:
    resno = 'thisis CLASS ATTRIBUTE resno'

    def __init__(self, resno='thisis INSTANCE ATTRIBUTE DEFAULT resno', **kwargs):
        print("Employee, __init__ start")
        self.resno = resno
        print("Employee, __init__ end")

    def show_resno(self):
        print("Employee, resno: {}".format(self.resno))


class Student(Human, Employee):
    def __init__(self, student_id='123'):
        print("Student, __init__ start")
        self.student_id = student_id
        Human.__init__(self, 18)
        print("Student, __init__ end")

    def show(self):
        print("Student, student_id: {}".format(self.student_id))


class Professor(Human, Employee):
    def __init__(self, professor_id='xyz'):
        print("Professor, __init__ start")
        self.professor_id = professor_id
        Employee.__init__(self, 'thisis INSTANCE ATTRIBUTE GIVEN resno')
        print("Professor, __init__ end")

    def show(self):
        print("Professor, professor_id: {}".format(self.professor_id))


if __name__ == '__main__':
    student = Student()
    print("I've skip to call Employee's __init__")
    print(student.resno)
    student.show_resno()

```
1.
Q. Derived class에서 some base class의 __init__ 생략하면?
- Student 객체를 생성하여 student라는 변수에 할당하였다. Student는 Human과 Employee를 상속하고 있는데, Student의 __init__ 에서는 Human의 __init__ 만 호출했다.
- student의 resno를 호출하였다. ('thisis CLASS ATTRIBUTE resno'가 불렸다.)

A. __init__ 만 안될뿐 object는 chainning하게 자동으로 생성된다.

2.
super를 사용하는 경우(super가 base class들의 __init__을 호출해준다고 가정한다. 이 가정이 틀렸을수도 있다.), 자동으로 arguments들을 base class의 __init__ 과 연관지어서 매칭시키며 base class들의 __init__ 을 호출해주는 것 같은데, 서로다른 두 base class의 __init__에서 같은 이름의 argument를 취하면 어떤 상황이 발생되는지.

3.
Q. derived class의 instance 2개가 있다고 가정하자. derived class의 1개 instance에서 base class의 class attribute를 수정할 경우, 수정이 되는지, derived class namespace에 새로운 변수가 할당되는지

