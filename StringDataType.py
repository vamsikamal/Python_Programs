# String data type

s1 = "Welcome to Python"
print(type(s1))  # <class 'str'>
print(s1[0])     # W
print(s1[4])     # o
print(len(s1))   # 17
# print(s1[200])   # IndexError: string index out of range

# Reverse indexing
print(s1[-1])  # n
print(s1[-17]) # W

# Slicing operation
print(s1[1:4])   # elc
print(s1[-4:-1]) # tho
print(s1[4:])    # ome to Python
print(s1[:15])   # Welcome to Pyth
print(s1[:])     # Welcome to Python
print(s1[::2])   # Wloet yhn
print(s1[::3])   # Wceoyo

name1 = "SLC"
name2 = "Python"
print(name1 + name2)
print(name1 * 5)
# print('\n' * 5)

a1 = "  SLC  "
print(a1)
print(a1.lstrip())  # SLC     => Left space will be trimmed
print(a1.rstrip())  #    SLC  => Right space will be trimmed
print(a1.strip())   # SLC     => Both sides space will be trimmed

# find()
s1 = "Welcome to Python"
print(s1.find("Python"))  # Returns index if exists and returns -1 if not exists
print(s1.index("Python")) # Returns index if exists and returns error if not exists
print(s1.count('o'))   # 3

# Case funtions
s1 = "Welcome to Python"
print(s1.capitalize())  # Welcome to python
print(s1.lower())   # welcome to python
print(s1.upper())   # WELCOME TO PYTHON
print(s1.title())   # Welcome To Python

# Reverse a string
print(s1[::-1])               # nohtyP ot emocleW
print(''.join(reversed(s1)))  # nohtyP ot emocleW

# IsUpper and IsLower
print(s1.isupper())   # False
print(s1.islower())   # False