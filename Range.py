# Range Data Type: This is sequence of numbers
# range(10) => 0 to 9
# range(0,10) => 0 to 9
v = range(10)
print(type(v))  # <class 'range'>

for i in range(10):              # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    print(i, end=', ')
print()

for i in range(0, 10):           # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    print(i, end=', ')
print()

for i in range(5, 10):           # 5, 6, 7, 8, 9,
    print(i, end=', ')
print()

for i in range(0, 25, 2):        # 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24,
    print(i, end=', ')
print()

for i in range(1, 25, 2):        # 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23,
    print(i, end=', ')
print()

for i in range(1,25,3):
    print(i, end=', ')           # 1, 4, 7, 10, 13, 16, 19, 22,
print()


