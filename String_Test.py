s1 = 'Python Welcome to Python'


print(s1.find('Python'))  # 11
print(s1.find('SLC'))     # -1

print(s1.index('Python')) # 11
#print(s1.index('SLC'))    # ValueError: substring not found

# print(s1.index("Python",4)) # TODO

print(s1.find(' Wel'))
print(s1.index('come'))