'''
Given the radius of a circle, finds a square whose area is (approximately) equal to the area of the circle.

Author: Zack Garza
CS61A, Laney College
'''

import math;

def square():
	r = int(input("What is the radius of the circle? "));
	area = math.pi * r**2
	side = math.sqrt(area)
	print("Length of the square's sides: " + str(side));
square();
