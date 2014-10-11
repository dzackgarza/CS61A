gLook = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0}

numGPAs = int(input("How many individual GPAs would you like to calculate? "))
listGPAs = []
listGrades = []
for i in range(0,numGPAs):
	print("GPA number " + str(i+1))
	numGrades = int(input("How many classes are there to report? "))
	totalUnits = 0
	totalQP = 0
	for j in range(0, numGrades):
		units = int(input("Enter number of units for class " + str(j+1) + ": "))
		totalUnits += units
		grade = input("Enter grade " + str(j+1) + ": ")
		totalQP += gLook.get(grade.upper()) * units
	gpa = totalQP / totalUnits
	listGPAs.append(gpa)

for i in listGPAs:
	print("GPA: " + "{0:.2f}".format(i))


