i = 5
while i >= 1:
    for j in reversed(range(i)):
        print(j+1, end=" ")
    print()
    i = i - 1