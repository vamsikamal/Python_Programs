list = [1,2,3, (10,20,30), 4, 5]
tup = (1,2,3, [10,20,30], 4,5)

# list[3][1] = 111   # Error 
# print(list)
tup[3][1] = 111
print(tup)