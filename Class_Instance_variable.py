class student:
    def __init__(self):
        self.Course = 'Python'
        self.Org = 'slc'
    def display(self):
        print(self.name)
        print(self.age)
        print(self.Course)
        print(self.Org)

s1 = student()
s1.name = 'ram'
s1.age=22

s2 = student()
s2.name = 'kumar'
s2.age = 23
s2.Org = 'XYZ'

s1.display()
s2.display()