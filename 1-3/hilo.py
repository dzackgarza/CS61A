'''
Determines a final grade, based on 5 equally weighted exams, as a function of the percentage scored on each.
Also reports the highest, lowest, and average scores.

CS61A, Laney College
Author: Zack Garza
'''

def calculate():
	score = [];
	for i in range (0, 5):
		score.append(int(input("What was score number " + str(i+1) + "? ")));

	total = sum(score)	
	highest = max(score)
	lowest = min(score)

	average = total / 5;
	print("Highest score: " + str(highest));
	print("Lowest score: " + str(lowest));
	print("Average score: " + str(average));

calculate();
