def MyGen():
    yield 'Sunday'
    yield 'Monday'
    yield 'Tuesday'

g = MyGen()
# print(g)
# print(type(g))

print(next(g))
print(next(g))
print(next(g))
