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
print(list5)

