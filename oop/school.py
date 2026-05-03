# multiple casses to create a school

class Student:
    def __init__(self,name,current_class,id):
        self.name = name
        self.id = id
        self.current_class = current_class

    #for represent the class
    def __repr__(self):
        return f'Student with name {self.name}, class : {self.current_class}, id: {self.id}'


class Teacher:
    def __init__(self,name,subject,id):
        self.name =name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f'Teacher : {self.name}, subject: {self.subject}'
    

class School:
    def __init__(self,name,):
        self.name =name
        self.teachers = []
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll_student(self,name,fee):
        if fee > 6500:
            return f'Not engough fee'
        else:
            id = len(self.students) + 1
            student = Student(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'
    def __repr__(self):
        print("Welcome to",self.name)
        print('........Our teachers----------')
        for teacher in self.teachers:
            print(teacher)
        print('---------Our students-----------')
        for student in self.students:
            print(student)
        return "all done for now"



# alia = Student("Alia",9,1)
# ranbeer = Teacher('Douran beer',"Algorithmn",101)
# print(alia)
# print(ranbeer)


phitron = School("Phitron")
phitron.enroll_student("alia",5200)
phitron.enroll_student("Rani",8000)
phitron.enroll_student("aishwaraiya",7000)
phitron.enroll_student("vaijan",90000)

phitron.add_teacher("Tom cruise","Algo")
phitron.add_teacher("Decap","DS")
phitron.add_teacher("Aj","Database")

print(phitron)


