def simpleinterest(p, n, r = 8):
    si = (p * n * r)/100
    return si


p = int(input("Enter principle amount: "))
n = int(input("Enter num of months: "))
s = simpleinterest(p, n)         # In this call r value is 8
print(s)
s = simpleinterest(p, n, 10)     # In this call r value is 10
print(s)