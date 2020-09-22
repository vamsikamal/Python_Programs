emplist = []
while True:
    print("Welcome to EMP List :")
    print("1. Add Employee")
    print("2. Show all Employees")
    print("3. Details of an employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    print()  # To have some space after enter your choice

    if choice == 6:
        print("Thank you. End of the program")
        break

    if choice == 1:
        name = input("Enter employee name: ")
        designation = input("Enter designation: ")
        sal = input("Enter salary: ")
        dict = {'name' : name, 'designation':designation, 'sal':sal}
        emplist.append(dict)

    if choice == 2:
        print("List of employees are below: ")
        for emp in emplist:
            for k in emp.keys():
                print(k, ":", emp[k])
            print()

    if choice == 3:
        empname = input("Enter employee name : ")
        isfound = False
        for emp in emplist:
            if emp['name'] == empname:
                isfound = True
                for k in emp.keys():
                    print(k, ":", emp[k])
                print()
                break
        if isfound == False:
            print("Employee not found")

    if choice == 4:
        empname = input("Enter employee name : ")
        isfound = False
        for emp in emplist:
            if emp['name'] == empname:
                isfound = True
                designation = input("Enter new designation: ")
                salary = input("Enter new salary: ")
                emp['designation'] = designation
                emp['sal'] = salary
                print("Updated successfully")
                print()
                break
        if isfound == False:
            print("Employee not found")

    if choice == 5:
        empname = input("Enter employee name : ")
        isfound = False
        for emp in emplist:
            if emp['name'] == empname:
                isfound = True
                emplist.remove(emp)
                print("Deleted successfully")
                print()
                break
        if isfound == False:
            print("Employee not found")
