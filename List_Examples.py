# List is collection of items of different type
# List mutable

# Empty list example
list1 = []
print(type(list1))  # <class 'list'>
print(list1)        # []

# List with data
list2 = [10, 20, 30, 25.5, 32.5, "SLC", "Python", True, False]
print(list2)  # Prints all items of list
# Index example
print(list2[0])  # 10
print(list2[4])  # 32.5
print(list2[-1]) # False

#Slicing
print(list2[1:4])   # [20, 30, 25.5]
print(list2[-7:-2]) # [30, 25.5, 32.5, "SLC", "Python"]
print(list2[-2:-7]) # []
print(list2[:])     # [10, 20, 30, 25.5, 32.5, "SLC", "Python", True, False]
print(list2[::2])   #  [10, 30, 32.5, "Python", False]

# Nested List
list3 = ["Hi","Hello",[10,20,30],"Good"]
print(list3[2])    # [10,20,30]
print(list3[2][0]) # 10
print(list3[2][2]) # 30
print(list3[1], list3[2][1])  # Hello 20
print(list3[2][0:2])  # [10,20]
print(list3)

# Adding elements
# append
list4 = [10, 20, 30]
print(list4)           # [10, 20, 30]
list4.append(50)
print(list4)           # [10, 20, 30, 50]

# insert
list4.insert(1,"Hi")
print(list4)           # [10, 'Hi', 20, 30, 50]

# extend
list5 = [10, 20, 30]
list6 = [50, 60, 70]
list5.extend(list6)
# list.extend([50, 60, 70])
print(list5)   # [10, 20, 30, 50, 60, 70]

list6 = [10, 20, 30]
list7 = [100, 200]
list6.append(list7)
print(list6)    #  [10, 20, 30, [100, 200]]

# Update elements
list8 = [10, 20, 30, 40]
list8[2] = 111
print(list8)    # [10, 20, 111, 40]

list9 = [10, 20, [100, 200, 300], 30]
list9[2][1] = 222
print(list9)    # [10, 20, [100, 222, 300], 30]

list10 = [1,2,3,4,5,6,7]
list10[2:5] = [10,20,30]
print(list10)  # [1, 2, 10, 20, 30, 6, 7]

# Delete elements from list
list11 = [10,20,30]
del list11[1]
print(list11)   # [10, 30]
list11.remove(30)
print(list11)   # [10]

list12 = [1,2,3,4,5,6,7,8,9]
del list12[2:5]
print(list12)   # [1, 2, 6, 7, 8, 9]

list13 = [10, 20, 10, 30]
list13.remove(10)
print(list13)   # [20, 10, 30]

t = list13.pop()
print(t)        # 30
print(list13)   # [20, 10]

list14 = [10,20,30,40]
t = list14.pop(1)
print(t)          # 20
print(list14)     # [10,30,40]

list14.clear()
print(list14)  # []

del list14
#print(list14)  # name 'list14' is not defined

# index
list15 = [10, 20, 30, 40, 30]
print(list15.index(30))   # 2

# count
print(list15.count(30))   # 2

print(len(list15))   # 5
print(max(list15))   # 40
print(min(list15))   # 10
print(sum(list15))   # 130
print(sum(list15) / len(list15))

list15.sort()
print(list15)    # [10, 20, 30, 30, 40]

list15.reverse()
print(list15)    # [40, 30, 30, 20, 10]