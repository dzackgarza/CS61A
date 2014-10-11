class Student:
	name = ""
	major = ""
	year = 1
	classes = []
	gpa = 0.0

	def __init__(self, name = "", major = "Undeclared", year = 1, classes = [], gpa = 0.0):
		self.name = name;
		self.major = major;
		self.year = year;
		self.classes = classes;
		self.gpa = gpa;

	def isInMajor(self, major):
		return True if self.major == major else False;

	def classStanding(self):
		if self.year == 1: return "Freshman";
		if self.year == 2: return "Sophomore";
		if self.year == 3: return "Junior";
		if self.year == 4: return "Senior";
		# else
		return "Lifelong Student!";

	def academicStanding(self):
		gpa = self.gpa;
		if gpa > 3.0: 
			return "A";
		elif gpa > 2.0: 
			return "B";
		elif gpa > 1.0: 
			return "C";
		else: 
			return "D";
		
		# Takes a list of tuples -- classes and grades -- and updates GPA
		def updateGrade(self, classes): pass;

class Major:
	majorTitle = ""
	students = []

	def __init__(self, title, students):
		self.majorTitle = title;
		self.students = students;

	def listStudents(self):
		for i in self.students:
			print(str(i));

	def isStudentInMajor(self, student):
		for i in self.students:
			if i == student : return True;
		return False;

	def studentGraduated(self, student):
		self.students.reomve(student);

	def numberOfStudentsInMajor(self):
		return students.size();

