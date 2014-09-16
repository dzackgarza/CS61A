'''
CS61, Laney College
Author: Zack Garza
'''
import math

def call_quad(a,b,c):
	if a == 0:
		print("This is not a quadratic polynomial, exiting..");
		return
	discriminant = (b**2)-(4*a*c);

	if discriminant < 0:
		print("There is no real solution.");
	else:
		solution1 = ((-1*b) + math.sqrt(discriminant)) / (2*a);
		solution2 = ((-1*b) - math.sqrt(discriminant)) / (2*a);
		print("Solutions: " + str(solution1) + " and " + str(solution2) + ".");
		return

a = int(input("What is a? "));
b = int(input("What is b? "));
c = int(input("What is c? "));
call_quad(a,b,c)
