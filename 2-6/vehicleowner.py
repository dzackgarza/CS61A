class Vehicle:

	year = 1905
	model = ""
	make = ""
	VIN = 000000000
	license_plate = "ABC29XYZ"

	owner = ""
	address = ""

	fees = 0.00

	def __init__(self, VIN = 000000000, year = 1905, owner = "", make = "Toyota", model = "Camry", address = "123 Jones St."):
		self.VIN = vin
		self.make = make
		self.model = model
		self.owner = owner
		self.address = address
		self.fees = 0.00

	''' Call when making a new title, and pass in how much it costs '''
	def initialize_new_record(self, fee):
		self.fees += fee

	def pay_fee(self, payment):
		if payment > self.fees:
			print "Payed too much"
		else:
			this.fees -= payment

	''' Called when the car is sold to a new owner. '''
	def change_owner(self, owner):
		self.owner = owner

	''' Call if the license plate needs to be changed '''
	def update_license(self, licence):
		self.license_plate = license
		
	def __str__(self): pass

	def __repr__(self): pass
