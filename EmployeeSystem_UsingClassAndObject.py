emplist = []
class Employee:
    def __init__(self, name, designation, salary):
        self.Name = name
        self.Designation = designation
        self.Salary = salary


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
        e = Employee(name, designation, sal)
        emplist.append(e)

    if choice == 2:
        print("List of employees are below: ")
        for emp in emplist:
            print("Name :", emp.Name)
            print("Designation :", emp.Designation)
            print("Salary :", emp.Salary)
            print()

    if choice == 3:
        empname = input("Enter employee name : ")
        isfound = False
        for emp in emplist:
            if emp.Name == empname:
                isfound = True
                print("Name :", emp.Name)
                print("Designation :", emp.Designation)
                print("Salary :", emp.Salary)
                print()
                break
        if isfound == False:
            print("Employee not found")

    if choice == 4:
        empname = input("Enter employee name : ")
        isfound = False
        for emp in emplist:
            if emp.Name == empname:
                isfound = True
                emp.Designation = input("Enter new designation: ")
                emp.Salary = input("Enter new salary: ")
                print("Updated successfully")
                break
        if isfound == False:
            print("Employee not found")

    if choice == 5:
        empname = input("Enter employee name : ")
        isfound = False
        for emp in emplist:
            if emp.Name == empname:
                isfound = True
                emplist.remove(emp)
                print("Deleted successfully")
                break
        if isfound == False:
            print("Employee not found")
