'''
Author: Zack Garza
'''

class School:

	fullName = ""
	shortName = ""
	address = ""

	def __init__(self, fullName = "", shortName = "", address = ""):
		self.fullName = fullName;
		self.shortName = shortName[:10];
		self.address = address;

	def printAddress(self):
		print("Address: " + self.address);

laney = School("Laney College", "Laney", "900 Fallon St, Oakland, CA 94607");
print("School object created.");

print("Calling printAddress() function:");
laney.printAddress()
