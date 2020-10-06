try:
    a = int(input('Enter a number: '))
    b = int(input('Enter second number: '))
    c = a/b
    print(c)
except:
    print('Error occured. Please try again')
finally:
    print('finally block executed')