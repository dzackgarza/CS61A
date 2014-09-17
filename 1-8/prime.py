'''
Prime number checker.
Author: Zack Garza
'''
from math import * 

def checkPrime(n):
	maxCheck = floor(sqrt(n))
	if n % 2 == 0: 
		return False
	else:
		i = 3;
		while(i <= maxCheck):
			if n % i == 0: 
				return False
			else: 
				i+=2;
		return True;

isPrime = checkPrime((2**67)-1)
print("Is is prime? " + str(isPrime));
