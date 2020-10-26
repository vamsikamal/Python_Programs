import pyodbc

while(True):
    print('Welcome to Student Management: ')
    print("1. Add student")
    print("2. Update student")
    print("3. Delete student")
    print("4. Get student")
    print("5. Get all students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        break
    elif choice == 1:
        FirstName = input("Enter First Name : ")
        LastName = input("Enter Last Name: ")
        Course = input("Enter Course: ")
        Address = input("Enter Address: ")

        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server=DESKTOP-JPG196B\\SQLEXPRESS;Database=dbSLC;Trusted_Connection=yes;')
        cursor = conn.cursor()
        sql_command = "INSERT INTO tblStudent(FirstName, LastName, Course, Address) VALUES('{0}','{1}','{2}','{3}')".format(FirstName, LastName, Course, Address)
        cursor.execute(sql_command)
        conn.commit()  # Required for insert, update and delete operations. Not required for READ
        conn.close()
        print('Data added successfully.')
    elif choice == 5:
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server=DESKTOP-JPG196B\\SQLEXPRESS;Database=dbSLC;Trusted_Connection=yes;')
        cursor = conn.cursor()
        sql_command = "SELECT * FROM tblStudent"  #
        cursor.execute(sql_command)
        for row in cursor:
            print(row.FirstName)
            print(row[1])
        conn.close()
