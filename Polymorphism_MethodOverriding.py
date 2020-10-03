class Parent:
    def method1(self):
        print('I am from parent class')

class Child(Parent):
    def method1(self):
        print('I am from child class')



c = Child()
c.method1()

p = Parent()
p.method1()