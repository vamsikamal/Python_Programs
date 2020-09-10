num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Non positive number given. Please try again.")