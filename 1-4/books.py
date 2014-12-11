'''
Author: Zack Garza
CS61A, Laney College
'''

def calculateShippingCharge(books, flatCharge = 3.00, perBookCharge = 1.99):
	return flatCharge + books * perBookCharge;


price = calculateShippingCharge(2)
assert price == 6.98;
price = calculateShippingCharge(3, 0.00)
print(price)
