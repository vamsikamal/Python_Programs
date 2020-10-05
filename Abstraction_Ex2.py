from abc import *

class Person(ABC):
    @abstractmethod
    def displaydetails(self):
        pass

    @abstractmethod
    def displayfullname(self, fname, lname):
        pass
    @abstractmethod
    def removecandidate(self):
        pass

class Faculty(Person):
    def wish(self):
        print('Hello')
    def displaydetails(self):
        print('Faculty Details')
    def displayfullname(self, fname, lname):
        print(fname + lname)

    def removecandidate(self):
        print('Faculty remove')


class Student(Person):
    def wish2(self):
        print('Good morning')
    def displaydetails(self):
        print('Student Details')
    def displayfullname(self, fname, lname):
        print(fname + lname)
    def removecandidate(self):
        print('Student remove')

f = Faculty()
s = Student()