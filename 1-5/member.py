'''
Author: Zack Garza
CS61A, Laney College
'''
from decimal import Decimal

amount = Decimal(input("What is the total cost of your order? "));

if amount > 50.00:
	print("Your shipping will be free!");
else:
	member = input("Are you a prime member? (y/n) ");
	if member.lower() == "y":
		print("Your shipping will be free!")
	elif member.lower() == "n":
		print("Your shipping will not be free.")

