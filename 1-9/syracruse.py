'''
The Syracruse Conjecture
Author: Zack Garza
'''

def Hailstone(n):
	steps = 0
	while (n != 1):	
		print(str(n) + ", ", end="") 
		if(n%2 == 0): 
			n /= 2
		else:
			n *= 3
			n += 1
		steps += 1
	print("\nNumber of steps: " + str(steps));

Hailstone(27);

