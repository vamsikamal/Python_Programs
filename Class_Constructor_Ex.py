class Test:
    def __init__(self):
        self.a = 10
    def m1(self):
        print("I am from m1 method")


t = Test()
print(t.a)
t.m1()
t.a = 100
print(t.a)