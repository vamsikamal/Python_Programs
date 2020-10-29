def countdown(num):
    print('Started: ')
    while num>0:
        yield num
        num = num - 1

values = countdown(5)
for i in values:
    print(i)
