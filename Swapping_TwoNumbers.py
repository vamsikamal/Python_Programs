a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swap: ")
print("First number is ", a , " Second number is ",b)

temp = a
a = b
b = temp

print("After swap: ")
print("First number is ", a , " Second number is ",b)