class Test:
    def m1(self):
        print('I am m1 method')
    def m1(self, a, b):
        print(a+b)

t = Test()
t.m1(10,20)