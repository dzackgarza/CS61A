class HonorRoll:

    def __init__(self, firstStudent, schoolName="Default School"):
        self.schoolName = schoolName
        self.numStudents = 1
        self.CurrentStudent = self.FirstStudent = Student(firstStudent)

    def AddStudent(self, studentName):
        self.FindEnd()
        self.CurrentStudent.NextStudent = Student(studentName)
        self.numStudents += 1
        self.CurrentStudent = self.CurrentStudent.NextStudent

    def FindEnd(self):
        while self.CurrentStudent.NextStudent:
            self.CurrentStudent = self.CurrentStudent.NextStudent
        return self.CurrentStudent

    def Display(self):
        print("School:", self.schoolName, self.numStudents, "Students:")
        self.CurrentStudent = self.FirstStudent
        self.FirstStudent.Display()
        while(self.CurrentStudent.NextStudent):
            self.CurrentStudent = self.CurrentStudent.NextStudent
            self.CurrentStudent.Display()


class Student:

    def __init__(self, studentName):
        self.studentName = studentName
        self.NextStudent = None

    def Display(self):
        print(self.studentName)

print("Students on a roll\n")

Honor = HonorRoll(schoolName="Berkeley", firstStudent="Norma")

Honor.AddStudent("Oswald")
Honor.AddStudent("Patton")
Honor.AddStudent("Quinn")
Honor.AddStudent("Ronald")
Honor.AddStudent("Sam")
Honor.AddStudent("Tedmund")
Honor.AddStudent("Umbridge")

Honor.Display()
