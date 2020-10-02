# Hierarchical Inheritance
class Class1:
    def m1(self):
        print('Parent class method')

class Class2(Class1):
    def m2(self):
        print('Child class method')

class Class3(Class1):
    def m3(self):
        print('Child class method')


c = Class2()
c.m1()
c.m2()
c1 = Class3()
c1.m1()
c1.m3()

