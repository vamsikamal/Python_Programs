list = [10, 20, 30, 1, 2, 3, 11, 22, 33]
num = int(input("Enter a number to search: "))
IsFound = False
for i in list:
    if i == num:
        IsFound = True
        break

if IsFound == True:
    print("Number found")
else:
    print("Number not found")








'''
if num in list:
    print("Item Found")
else:
    print("Item not found")
'''