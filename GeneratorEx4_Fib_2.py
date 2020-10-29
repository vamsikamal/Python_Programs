def feb():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b


n = int(input('Enter a value: '))
c = 0
for i in feb():
    if c == n:
        break
    c = c + 1
    print(i)
