studentsData=[]
def addStudent():
    print(".....Enter Student Details......")
    firstName=input("First Name: ")
    lastName=input("Last Name: ")
    idNum=input("Student ID: ")
    studentDict={"fname":"","lname":"","id":"x","s1":0.0,"s2":0.0,"s3":0.0,"s4":0.0,"flag":0, "average":0.0}
    for student in studentsData:
        if (student.get("fname")==firstName and student.get("lname")==lastName) or student.get("id")==idNum:
            print("The Name or ID you have entered is already existed in the records. Please Enter Correct Details")
            return
    studentDict["fname"]=firstName
    studentDict["lname"]=lastName
    studentDict["id"]=idNum
    studentsData.append(studentDict)
    print("{} {} is added to the student records.".format(firstName,lastName))
def assigningGrades(student):
    student["s1"]=float(input("Enter Subject1 Grade: "))
    student["s2"]=float(input("Enter Subject2 Grade: "))
    student["s3"]=float(input("Enter Subject3 Grade: "))
    student["s4"]=float(input("Enter Subject4 Grade: "))
    student["average"]=(student["s1"]+student["s2"]+student["s3"]+student["s4"])/4

def assignGrades():
    idnum=input("Enter Student ID: ")
    for student in studentsData:
        if student.get("id")==idnum:
            if student.get("flag")==1:
                print("The grades are already assigned to {} {}".format(student["fname"],student["lname"]))
                x=input("Do you want to modify? type 1 to modify else 0: ")
                if x=='1':
                    assigningGrades(student)
                    print("Grades are successfully modified for {} {}".format(student["fname"],student["lname"]))
                    return
                else:
                    return
            else:
                assigningGrades(student)
                student["flag"]=1
                print("Grades are successfully assigned to {} {}".format(student["fname"],student["lname"]))
                return
    print("Student with ID({}) not found in the records!".format(idnum))
def calculateAverage():
    idnum=input("Enter Student ID: ")
    for student in studentsData:
        if student.get("id")==idnum:
            # avg=(student["s1"]+student["s2"]+student["s3"]+student["s4"])/4
            print("The Average Grade of {} {} : {}".format(student["fname"],student["lname"],student["average"]))
            return
    print("Student with ID({}) not found in the records!".format(idnum))
def generateReports():
    print(".....Student Reports.....")
    print("FName"+" "*8+"LName"+" "*10+"ID"+" "*10+"AVG")
    for student in studentsData:
        print(student["fname"]+" "*8+student["lname"]+" "*8+student["id"]+" "*8+str(student["average"]))
    
def StudentsMain():
    print("welcome")
    while True:
        print("1. Add Student")
        print("2. Assign Grades")
        print("3. calculate Average")
        print("4. Generate Reports")
        print("5. Exit")
        ch=int(input("Enter your option: "))
        match ch:
            case 1: addStudent()
            case 2: assignGrades()
            case 3: calculateAverage()
            case 4: generateReports()
            case 5: break
StudentsMain()
