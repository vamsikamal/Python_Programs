# Purpose of the constructor is to initialise instance variables
# When an object is created constructor will be called automatically

class student:
    '''This is a demo class'''
    def __init__(self):
        self.RollNum = 10
        self.Name = 'SLC'
        self.Course = 'Python'

    def display(self):
        print(self.RollNum)
        print(self.Name)
        print(self.Course)

s = student()
s.display()