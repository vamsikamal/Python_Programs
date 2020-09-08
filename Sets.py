# Set is a collection of items without duplicates
# Order of the items will not be preserved
a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(type(a))   # <class 'set'>
print(a)         # {1, 2, 3, 4, 5}

# Union
print(a|b)       # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b)) # {1, 2, 3, 4, 5, 6, 7, 8}

#Intersection
print(a&b)        # {4,5}
print(a.intersection(b))   # {4,5}

# Difference
print(a-b)        # {1,2,3}
print(a.difference(b))  # {1,2,3}

# Symmetric difference => (A union B) - (A intersection B)
print(a^b)        # {1, 2, 3, 6, 7, 8}


a = {1,2,3,4,5}
b = {4,5,6,7,8}
a.update(b)  # a = a |b
print(a)     # {1, 2, 3, 4, 5, 6, 7, 8}

a = {1,2,3,4,5}
b = {4,5,6,7,8}
a.intersection_update(b)   # a = a & b
print(a)

a = {1,2,3,4,5}
b = {4,5,6,7,8}
a.difference_update(b)     # a = a - b
print(a)                   # {1,2,3}

a = {1,2,3,4,5}
b = {4,5,6,7,8}
a.symmetric_difference_update(b)     # a = a ^ b
print(a)                              # {1, 2, 3, 6, 7, 8}


s = {1,2,3}
s.add(10)
print(s)        # {10, 1, 2, 3}

s.update([111,222,333])
print(s)        # {1, 2, 3, 10, 333, 111, 222}

# Remove
s.discard(111)
print(s)        # {1, 2, 3, 10, 333, 222}

A = {1,2,3}
B = {1,2,3,4,5}
print(A.issubset(B))   # True
print(B.issuperset(A))  # True

n = {}    # null set
