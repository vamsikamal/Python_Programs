f = open('demo.txt', 'a+')
f.write('Adding new data from a+ mode\n')
f.seek(0)
data = f.read()
print(data)

f.close()