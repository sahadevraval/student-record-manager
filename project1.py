class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, marks):
        s = Student(roll_no, name, marks)
        self.students.append(s)

    def display_all(self):
        for s in self.students:
            s.display()

    def search_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                s.display()
                return
        print("Student not found.")

    def delete_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                self.students.remove(s)
                print("Student deleted.")
                return
        print("Student not found.")


def main():
    sm = StudentManager()
    
    while True:
        print("\n1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")
        
        if choice == '1':
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            sm.add_student(roll, name, marks)

        elif choice == '2':
            sm.display_all()

        elif choice == '3':
            roll = input("Enter Roll No to search: ")
            sm.search_student(roll)

        elif choice == '4':
            roll = input("Enter Roll No to delete: ")
            sm.delete_student(roll)

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

main()

