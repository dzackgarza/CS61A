'''
Circle Class
Author: Zack Garza
'''

import math

class Circle:

	radius = 1;
	circumference = 2*math.pi;
	area = math.pi;
	diameter = 2;

	def __init__(self, r):
		self.radius = r;
		self.circumference = 2 * math.pi * self.radius
		self.area = math.pi * (self.radius ** 2)
		self.diameter = self.radius * 2

	def summarize(self):
		print("Radius: " + str(self.radius));
		print("Circumference: " + str(self.circumference));
		print("Area: " + str(self.area));
		print("Diameter: " + str(self.diameter));

c = Circle(3.9);
c.summarize();
