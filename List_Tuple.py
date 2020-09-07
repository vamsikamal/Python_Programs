list = [10, 20, 30, 1, 2, 3]
print(sorted(list))   # [1, 2, 3, 10, 20, 30]
print(list)           # [10, 20, 30, 1, 2, 3]


list1 = [10, 20, 30, 1, 2, 3]
list1.sort()
print(list1)          # [1, 2, 3, 10, 20, 30]


tup = (10,20,30,1,2,3)
print(sorted(tup))     # [1, 2, 3, 10, 20, 30]
print(tup)             # (10, 20, 30, 1, 2, 3)

tup.sort()             # Error