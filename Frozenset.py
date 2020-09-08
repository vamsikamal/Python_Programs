# Frozenset is similar to sets but it is immutable
s = {1,2,3,4}
f = frozenset(s)

print(type(f))
print(f)

for i in f:
    print(i)

# f.add(111)   # Not possible
# f.update([22,33])  # Not possible
# f.discard(3)
