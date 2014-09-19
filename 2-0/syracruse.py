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
	return steps

print(str(Hailstone(27)));

'''
cont = True;
for i in range(1, 1000000):
	cont = Hailstone(i)
	if(not cont): break;
	else: print(str(cont));

if(not cont): print("Counterexample found");
else: print("No counterexample found");
'''
