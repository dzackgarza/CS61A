'''

Author: Zack Garza
CS61A, Laney College
'''

def calculate():
	units = int(input("How many units have you obtained from university? "))
	
	transfer = int(input("How many units will be transferred? "));
	transfer = min(transfer, 25);
	
	service = int(input("How many years of military/public service do you have? "))
	service = min(service * 5, 15);

	total = transfer + service + units;


	print("You have  " + str(total) + " total units.");
	if (total >= 125): 
		print("You have finished your degree!");
	else:
		print("You have " + str(125 - total) + " more units to take before graduating.");

calculate();
