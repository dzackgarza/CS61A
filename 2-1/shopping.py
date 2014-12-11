'''
Shopping List
Author: Zack Garza
'''

list = []

more = True
while(more):

	list.append(input("Enter item: "));

	valid = False
	while(not valid):
		choice = input("More items? (y/n) ");

		if choice.lower() in ["y", "yes"]:
			valid = True;
			more = True
		elif choice.lower() in ["n", "no"]:
			valid = True;
			more = False;
		else:
			valid = False;
			print("Invalid choice, enter 'y' or 'n'");

for i in range(0, len(list)):
	print("Item #" + str(i+1) + ": " + str(list[i]));
