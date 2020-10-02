# Multi Level Inheritance
class Class1:
    def m1(self):
        print('M1 Method called')

class Class2(Class1):
    def m2(self):
        print('M2 Method called')

class Class3(Class2):
    def m3(self):
        print('M3 Method called')

c = Class3()
c.m1()
c.m2()
c.m3()

