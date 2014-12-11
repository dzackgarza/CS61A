'''
CS61A, Laney College
Author: Zack Garza
'''

def triangularNumber(n):
	sum = 0
	if n == 1: 
		return 1
	else: 
		sum += n + triangularNumber(n-1)
	return sum;

assert triangularNumber(1) == 1
assert triangularNumber(2) == 3
assert triangularNumber(3) == 6
assert triangularNumber(4) == 10
assert triangularNumber(5) == 15

print(triangularNumber(25));
