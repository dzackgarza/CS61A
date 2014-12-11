
score = {}
sum = 0

from decimal import Decimal

for i in range(0,7):
		score[i] = int(input("What was the score on exam " + str(i+1) + "? "))
		s = Decimal(score[i]);
		if s == 999: break;
		while not (s >= 0 and s <= 101):
			score[i] = input("Sorry, not a valid value. Please enter again: ");

for i in range(0, len(score)):
	sum += score[i];

mean = sum / len(score);

print(str(mean));
