# Single Inheritance
class Class1:
    def m1(self):
        print('Parent class method')

class Class2(Class1):
    def m2(self):
        print('Child class method')


c = Class2()
c.m1()
c.m2()

