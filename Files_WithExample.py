with open('demo.txt', 'r') as f:
    data = f.read()
    #print(data)
    print(f.closed)
print('End of the program')
print(f.closed)