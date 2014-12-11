'''
Circle Class
Author: Zack Garza
'''

import math

class Circle:

	radius = 0;

	def __init__(self, r):
		self.radius = r;

	def Circumference(self):
		return 2*math.pi*self.radius

	def Area(self):
		return math.pi*(self.radius**2)

	def Diameter(self):
		return 2*self.radius

c = Circle(3.9);
print("Radius: " + str(c.radius));
print("Circumference: " + str(c.Circumference()));
print("Area: " + str(c.Area()));
print("Diameter: " + str(c.Diameter()));
