'''
Author: Zack Garza
'''

class School:

	fullName = ""
	shortName = ""
	address = ""

	def __init__(self, fullName = "", shortName = "", address = ""):
		self.fullName = fullName;
		self.shortName = shortName;
		self.address = address;

	def printAddress(self):
		print("Address: " + self.address);

laney = School("Laney", "Laney", "add");
laney.printAddress()
