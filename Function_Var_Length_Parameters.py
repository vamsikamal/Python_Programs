def totalbill(*n):
    # print(type(n))    # <class 'tuple'>
    sum = 0
    for i in n:
        sum = sum + i
    print("Total Bill is : ", sum)

totalbill(10,20,30)
totalbill(1,2,3,4,5,6,7,8,9,10)