class Human:
    age = 1

    def __init__(self, age=1):
        print("Human, __init__ start")
        self.age = age
        print("Human, __init__ end")

    def show_age(self):
        print("Human, age: {}".format(self.age))


class Employee:
    resno = 'thisis CLASS ATTRIBUTE resno'

    def __init__(self, resno='thisis INSTANCE ATTRIBUTE DEFAULT resno'):
        print("Employee, __init__ start")
        self.resno = resno
        print("Employee, __init__ end")

    def show_resno(self):
        print("Employee, resno: {}".format(self.resno))


class Student(Human, Employee):
    def __init__(self, student_id='123'):
        print("Student, __init__ start")
        self.student_id = student_id
        # Human.__init__(self, 18)
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
    student.show_age()
    student.show_resno()
