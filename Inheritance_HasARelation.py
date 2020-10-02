class Engine:
    cc = 1199
    def __init__(self):
        self.Brand = 'Suzuki'
        print('Engine specific constructor ')

    def m2(self):
        print('M2 Function called')

class Car:
    def __init__(self):
        self.engine = Engine()

    def displaySpec(self):
        print('Car Specification: ')
        print('CC is ', self.engine.cc)
        print('Brand is ', self.engine.Brand)
        self.engine.m2()

c = Car()
c.displaySpec()
