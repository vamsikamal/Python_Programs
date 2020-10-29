def feb():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b


n = int(input('Enter a value: '))
g = feb()
for i in range(n):
    print(next(g))