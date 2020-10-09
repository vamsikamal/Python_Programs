import csv
with open('emp.csv', 'w', newline='') as f:
    w = csv.writer(f)
    lstHeaders = ['EmpID', 'EmpName', 'Salary', 'Designation']
    w.writerow(lstHeaders)
    num = int(input('Enter employees count: '))
    for i in range(num):
        eid = input('Enter employee ID: ')
        ename = input('Enter employee name: ')
        esal = input('Enter employee salary: ')
        desn = input('Enter employee designation: ')
        lstData = [eid, ename, esal, desn]
        w.writerow(lstData)
print('Data added successfully')