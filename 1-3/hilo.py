'''
Determines a final grade, based on 5 equally weighted exams, as a function of the percentage scored on each.
Also reports the highest, lowest, and average scores.

CS61A, Laney College
Author: Zack Garza
'''

def calculate():
	score = [0] * 5
	for i in range (0, 5):
		query = "What was score number " + str(i+1) + "? ";
		score[i] = int(input(query))

	total, lowest, highest = 0, score[0], score[0];

	for i in range(0, 5):
		total += score[i];
		if score[i] > highest:
			highest = score[i]
		if score[i] < lowest:
			lowest = score[i]		

	average = total / 5;
	print("Highest score: " + str(highest));
	print("Lowest score: " + str(lowest));
	print("Average score: " + str(average));

calculate();
