"""
CS 61A, Laney College
Author: Zack Garza
"""
from decimal import *;
getcontext().prec = 2

def getTotalPriceOf(gross):
	if gross > 500:
		discount = gross * .15
	elif gross > 100:
		discount = gross * .10
	elif gross > 50:
		discount = gross * .05
	else:
		discount = 0
	result = round(gross-discount, 2)
	return result

print(getTotalPriceOf(499.99));
