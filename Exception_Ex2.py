try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = a / b
    print(c)
except (ValueError, ZeroDivisionError) as msg:
    print('Error: ', msg)
except:
    print('Error occured. Please try again ')

print('End of the program')