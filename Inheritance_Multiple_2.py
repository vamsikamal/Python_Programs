class Class1:
    def display(self):
        print('Hey from class 1')
    def m1(self):
        print('I am from Class1')

class Class2:
    def wish(self):
        print('Good morning')
    def m1(self):
        print('I am from Class2')

class Class3(Class1, Class2):
    def func3(self):
        print('Hello from Class3')


c = Class3()
c.wish()
c.display()
c.func3()
c.m1()
print(Class3.mro())