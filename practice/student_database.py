class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

    def enroll_student(self):
        if not self.is_enrolled:
            self.is_enrolled = True
            print(f"{self.name} has been enrolled.")
        else:
            print(f"{self.name} is already enrolled.")

    def drop_student(self):
        if self.is_enrolled:
            self.is_enrolled = False
            print(f"{self.name} has been dropped.")
        else:
            print(f"{self.name} is  not enrolled.")

    def view_student_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, "
              f"Department: {self.department}, Enrolled: {self.is_enrolled}")


class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def find_student(cls, student_id):
        for student in cls.student_list:
            if student.student_id == student_id:
                return student
        return None


# Sample Data ------------------
StudentDatabase.add_student(Student(101, "Manik Sarker", "CSE", False))
StudentDatabase.add_student(Student(102, "Rahim Ahmed", "EEE", True))
StudentDatabase.add_student(Student(103, "Karim Uddin", "BBA", False))


# Menu System ------------------
while True:
    print("\n===== Student Management System =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- All Students ---")
        for student in StudentDatabase.student_list:
            student.view_student_info()

    elif choice == "2":
        sid = int(input("Enter Student ID to enroll: "))
        student = StudentDatabase.find_student(sid)
        if student:
            student.enroll_student()
        else:
            print("Student not found.")

    elif choice == "3":
        sid = int(input("Enter Student ID to drop: "))
        student = StudentDatabase.find_student(sid)
        if student:
            student.drop_student()
        else:
            print("Student not found.")

    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice. Please try again.")