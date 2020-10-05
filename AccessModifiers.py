class A:
    __x = 10
    def m1(self):
        print('M1 method', A.__x)

class B(A):
    def m2(self):
        print('M2 Method')

a = A()
a.m1()

b = B()
b.m2()

print('Outside the class' , A.__x)