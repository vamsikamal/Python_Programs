# ex: static variable
class student:
    org = 'slc'       # Static variable
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

s1 = student('ram', 22, 'Python')
print(s1.name)
print(s1.age)
print(s1.course)
print(student.org)

s2 = student('Kumar', 25, 'Python')
print(s2.name)
print(s2.age)
print(s2.course)
print(student.org)