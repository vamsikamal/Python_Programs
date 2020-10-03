# Operator Overloading Example

class Book:
    def __init__(self, pages):
        self.PagesCount = pages

    # for + operator __add__ is the method
    def __add__(self, other):
        return self.PagesCount + other.PagesCount
    def __sub__(self, other):
        return  self.PagesCount - other.PagesCount
    def __mul__(self, other):
        return self.PagesCount * other.PagesCount
    def __floordiv__(self, other):
        return self.PagesCount // other.PagesCount

b1 = Book(100)
b2 = Book(50)
print(b1+b2)
print(b1-b2)
print(b1*b2)
print(b1//b2)
