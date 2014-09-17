"""

Author: Zack Garza
"""

moreGPAs = True;

GPAs = []
values = ['f', 'd', 'c', 'b', 'a']

while(moreGPAs):

	moreClasses = True;
	totalUnits = 0;
	GPA = 0;

	while(moreClasses):

		classes = []

		units = int(input("Enter number of units for this class: "))
		totalUnits += units;

		letter = input("Enter letter grade for this class: ")

		letterValue = values.index(letter.lower())
		GPA += units * letterValue;

		cont = input("Are there more grades to enter? (y/n) ")
		moreClasses = cont in ['y', 'Y', 'yes', 'Yes']
	
	print("{0:.2f}".format(GPA / totalUnits))
	cont = input("Are there more GPAs to calculate? (y/n) ")
	moreGPAs = cont in ['y', 'Y', 'yes', 'Yes']

		
