def calc(a, b):
    s = a + b
    d = a - b
    p = a * b
    return s,d,p

x, y, z = calc(20, 10)
print("Sum is ", x)
print("Difference is ", y)
print("Product is ", z)