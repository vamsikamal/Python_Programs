import csv
f = open('emp.csv', 'r')
r = csv.reader(f)
data = list(r)
f.close()
print('Employee details: ', end='\n\n')

for line in data[1:]:
    for i in range(len(data[0])):
        print(data[0][i],' : ',line[i])
    print()