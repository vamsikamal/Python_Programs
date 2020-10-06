try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = a / b
    print(c)
except ValueError:
    print('Value error occurred. Please input valid numbers.')
except ZeroDivisionError:
    print('Cannot divide with zero. Please try with non - zero value')
except:
    print('Error occured. Please try again ')

print('End of the program')