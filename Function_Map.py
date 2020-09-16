# map() without using lambda
l = [1,2,3,4,5]
def squre(x):
    return x*x

l1 = list(map(squre, l))
print(l1)

# map() using lambda
l = [1,2,3,4,5]
l1 = list(map(lambda x : x*x, l))
print(l1)
