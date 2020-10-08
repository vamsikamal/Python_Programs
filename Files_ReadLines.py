f = open('demo.txt','r')
data = f.readlines()
print(data)
print(type(data))
for line in data:
    print(line, end='')
f.close()