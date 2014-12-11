"""
Calculates the total shipping charges for several books.

To avoid precision/roundoff errors, all intermediate
values are stored as cents, and only represented as a
dollar mount in the end.
 
Laney College 2014

Zack Garza
"""
from decimal import Decimal

SHIPPING = 299

def total():
	numberOfBooks = 3

	book1 = 1166
	book2 = 2135
	book3 = 1400
	
	return (book1 + book2 + book3 + (numberOfBooks * SHIPPING)) / 100

print(total())

