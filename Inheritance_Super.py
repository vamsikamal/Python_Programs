class Person:
    def __init__(self):
        print('Person Constructor')

    def m1(self):
        print('M1 method from Person class')


class Student(Person):
    def __init__(self):
        print('Student Constructor')
        super().__init__()

    def m2(self):
        print('M2 from Student class')
        super().m1()

s1 = Student()
s1.m1()
s1.m2()