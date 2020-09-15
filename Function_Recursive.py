# Recursive function means calling the same function inside it

def findfact(n):
    if n == 1:
        return 1
    else:
        return n * findfact(n-1)

num = int(input("Enter a number : "))
f = findfact(num)
print("Factorial is : ", f)