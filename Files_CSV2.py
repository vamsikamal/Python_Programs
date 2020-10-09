import csv
f = open('emp.csv', 'r')
r = csv.reader(f)
data = list(r)
for line in data:
    print(line)