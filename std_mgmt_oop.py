class Student:
    def __init__(self,id,name,age,courses,percentage):
        self.id=id
        self.name=name
        self.age=age
        self.courses=courses
        self.percentage=percentage

    def to_record(self):
        return f"{self.id},{self.name},{self.age},{self.courses},{self.percentage}\n"
    
    @staticmethod
    def from_record(line):
        id,name,age,courses,percentage=line.strip().split(',')
        return Student(int(id),name,int(age),courses,float(percentage))
    
    def __str__(self):
        return f"{self.id} | {self.name} | {self.age} | {self.courses} | {self.percentage}"

class StudentManager:
    def addstudent(self,student):
        with open("students.txt","a") as f:
            f.write(student.to_record())
    def getstudents(self):
        students=[]
        try:
            with open("students.txt", "r") as f:
                lines=f.readlines()
                for line in lines:
                    students.append(Student.from_record(line))
        except FileNotFoundError:
            pass
        return students
    
    def search(self,id):
        students=self.getstudents()
        for student in students:
            if student.id==id:
                return student
        return None
        
                
    def update(self,id,new):
        found=False
        students=self.getstudents()
        for student in students:
            if student.id==id:
                found=True
                student.age=new
                break
        if found:
            with open("students.txt", "w") as f:
                for s in students:
                    f.write(s.to_record())
        return found

    def delete(self,id):
        students=self.getstudents()
        newStudents=[]
        found = False
        for student in students:
            if student.id==id:
                found=True
            else:
                newStudents.append(student)

        if found:
            with open("students.txt","w") as f:
                for s in newStudents:
                    f.write(s.to_record())
        return found

def menu():
    manager=StudentManager()
    while True:
        print("MENU")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by ID")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit program")
        choice = int(input("Enter your choice: "))
        if choice==1:
            id = int(input("ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            courses = input("Courses: ")
            percentage = float(input("Percentage: "))
            manager.addstudent(Student(id, name, age, courses, percentage))
        elif choice==2:
            students=manager.getstudents()
            if not students:
                print("No students found.")
            for s in students:
                print(s)
        elif choice==3:
            search_id=int(input("Enter id to search: "))
            result=manager.search(search_id)
            if result!=None:
                print("Student found: ",result)
            else:
                print("Student not found")
        elif choice==4:
            id=int(input("Enter student id: "))
            new=int(input("Enter students new age: "))
            if manager.update(id,new):
                print("Updated successfully")
            else:
                print("Not found")
        elif choice==5:
            delete_id=int(input("Enter id of student to be deleted: "))
            if manager.delete(delete_id):
                print("Deleted successfully")
            else:
                print("Not found")
        elif choice==6:
            break
        else:
            print("Invalid choice!")
menu()