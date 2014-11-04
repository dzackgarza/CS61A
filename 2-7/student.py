'''
Students sometimes work for the school or college they attend
Show a design for Multiple Inheritance of a Student/Worker.
'''


class Student():

    name = ""
    classes = []
    gpa = 0.0

    def __init__(self, name="Default name", classes=[], gpa=1.0, **kwargs):
        super(Student, self).__init__(**kwargs)
        self.name = name
        self.classes = classes
        self.gpa = gpa

    def getGPA(self):
        return self.gpa

    def get_classes(self):
        return self.classes


class Worker():

    title = ""
    employer = ""
    wage = 0.00

    def __init__(self, employer="Default School", title="Student Worker", wage=9.00, **kwargs):
        super(Worker, self).__init__(**kwargs)
        self.employer = employer
        self.title = title
        self.wage = wage

    def get_employer(self):
        return self.employer

    def get_title(self):
        return self.title


class StudentWorker(Student, Worker):

    work_study_units = 0

    def __init__(self, work_study_units=1, **kwargs):
        super().__init__(**kwargs)
        self.work_study_units = work_study_units

    def __repr__(self):
        return "Name: " + str(self.name) + ", GPA: " + str(self.gpa) + ", Employer: " + str(self.employer) + ", Wage: " + str(self.wage)

    def __str__(self):
        return "Name: " + str(self.name) + ", GPA: " + str(self.gpa) + ", Employer: " + str(self.employer) + ", Wage: " + str(self.wage)

billy = StudentWorker(work_study_units=3, gpa=3.5)

print (str(billy))
