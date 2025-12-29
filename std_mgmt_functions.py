def addstudent():
    id=input("Enter student id: ").strip()
    if id=="":
        print("ID cannot be empty.")
        return
    name=input("Enter student's name: ").strip()
    if name == "":
        print("Name can't be empty.")
        return
    age=input("Enter student's age: ").strip()
    if not age.isdigit() or int(age)<0:
        print("Invalid")
        return
    courses=input("Enter student's courses separated by a hyphen(-): ")
    if courses=="":
        print("Courses cannot be empty.")
        return
    percentage=input("Enter student's percentage: ")
    try:
        if float(percentage) < 0 or float(percentage)>100:
            print("Invalid! Percentage can't be negative.")
            return
    except ValueError:
        print("Percentage must be a number")
    record='{},{},{},{},{}\n'.format(id,name,age,courses,percentage)
    with open("students.txt","a+") as f:
        f.write(record)

def viewstudents():
    try:
        with open("students.txt", "r") as f:
            lines=f.readlines()
            if not lines:
                print("No record found.")
                return
            for line in lines:
                student=line.strip().split(",")
                print(f"""
                      ID: {student[0]}
                      Name: {student[1]}
                      Age: {student[2]}
                      Courses: {student[3]}
                      Percentage: {student[4]}
                      ---------------
                      """)     
    except FileNotFoundError:
        print("File not found.")

def search(id):
    try:
        with open("students.txt","r") as f:
            for line in f:
                student=line.strip().split(",")
                if student[0] == str(id):
                    return True
        return False
    except FileNotFoundError:
        print("File not Found.")
    except:
        print("Something went wrong.")
    
def update(id,new):
    try:
        with open("students.txt", "r") as f:
            lines=f.readlines()
        found = False
        with open("students.txt","w") as f:
            for line in lines:
                student=line.strip().split(",")
                if student[0]==str(id):
                    student[2]=str(new)
                    found = True
                f.write(",".join(student)+"\n")

        if found:
            print("Student updated successfully")
        else:
            print("Student not found")
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Something went wrong.")

def delete(id):
    try:
        with open("students.txt","r") as f:
            lines=f.readlines()
        found = False
        with open("students.txt","w") as f:
            for line in lines:
                student=line.strip().split(",")
                if student[0]==str(id):
                    found = True
                    continue
                f.write(line)
        if found:
            print("Student deleted susuccessfully")
        else:
            print("Not found")
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Something went wrong.")

def menu():
    while True:
        print("MENU:")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by ID")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit program")
        choice = int(input("Enter your choice: "))
        if choice==1:
            addstudent()
        elif choice==2:
            viewstudents()
        elif choice==3:
            search_id=int(input("Enter id to search: "))
            if search(search_id)==True:
                print("Student found.")
            else:
                print("Sttudent not found")
        elif choice==4:
            id=int(input("Enter tudent id: "))
            new=int(input("Enter students new age: "))
            update(id,new)
        elif choice==5:
            delete_id=int(input("Enter id of student to be deleted: "))
            delete(delete_id)
        elif choice==6:
            break
        else:
            print("Invalid choice!")


menu()