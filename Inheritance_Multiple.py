class Class1:
    def display(self):
        print('Hey from class 1')

class Class2:
    def wish(self):
        print('Good morning')

class Class3(Class1, Class2):
    def func3(self):
        print('Hello from Class3')


c = Class3()
c.wish()
c.display()
c.func3()
