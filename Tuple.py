# Tuple is collection of items of different types
# Tuple is immutable

# Declaratioin
tup1 = (10, 20, 30, 40, 50)
print(type(tup1))    # <class 'tuple'>
print(tup1)          # (10, 20, 30, 40, 50)

# Declaration
tup2 = 10,20,30,40   # Packing
print(type(tup2))    # <class 'tuple'>
print(tup2)          # (10, 20, 30, 40)

# Unpacking
a,b,c,d = tup2
print(a)     # 10
print(b)     # 20
print(c)     # 30
print(d)     # 40

# Reading
print(tup2)   # (10, 20, 30, 40)
print(tup2[1])  # 20

# tup2[2] = 100  # Error
# tup2.append(100)
# del tup2[1]
print(tup2[-1])
print(tup2[1:3])
print(len(tup2))

print(sorted(tup2))

