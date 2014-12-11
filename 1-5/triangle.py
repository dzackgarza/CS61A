'''
CS61A, Laney College
Author: Zack Garza
'''

def checkTriangle(a,b,c):
	longestSide = max(a,b,c);
	if a+b+c < 2 * longestSide:
		print("This can not be a triangle!");
	else:
		print("This is a valid triangle, checking...");
		if a == b or b == c or c == a:
			print("This is an isoceles triangle.");
			if a == b and b == c and c == a:
				print("This is also an equilateral triangle.");
		else:
			print("This is just a regular triangle.");

print("Please input the three sides of a potential triangle.");

a = int(input("Side a: "));
b = int(input("Side b: "));
c = int(input("Side c: "));

checkTriangle(a,b,c);
