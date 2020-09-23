class student:
    '''This is a demo class'''
    def __init__(self, rnum, name, course):
        self.RollNum = rnum
        self.Name = name
        self.Course = course

    def display(self):
        self.country = 'India'
        print(self.RollNum)
        print(self.Name)
        print(self.Course)
        print(self.age)

s1 = student(101, 'SLC', 'Python')
s1.age = 1
s1.display()
print(s1.country)


s2 = student(102, 'Shyam', 'Python')
s2.age = 22
s2.display()
print(s2.country)

print(s1.Name, s2.Name)