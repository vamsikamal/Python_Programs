f = open('demo.txt', 'r')
data = f.read(10)
print(f.tell())
data2 = f.read(10)
print(f.tell())
f.seek(5)
print(f.tell())
f.close()
print(data)
print(data2)