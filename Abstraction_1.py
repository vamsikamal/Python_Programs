# We cannot create object for interface or abstract class
# We cannot instantiate interface or abstract class

from abc import *
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

class Demo(Test):
    def m1(self):
        print('Hello World')


d = Demo()
d.m1()

