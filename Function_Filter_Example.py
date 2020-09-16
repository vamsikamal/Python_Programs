# Filter function: We can use it to apply a condition on a sequence
# filter (function, sequence)

# filter () Without lambda funtion

def isEven(x):
    if x%2 ==0:
        return True
    else:
        return  False
l = [0,2,3,7,6,4,19]
l1 = list(filter(isEven, l))
print(l1)

# filter () With lambda funtion
l = [0,2,3,7,6,4,19]
l1 = list(filter(lambda x:x%2 ==0, l))
print(l1)