"""
Using Heron's theorem, computes the area of a triangle given the length of three sides.

Laney College

@date 		9/22/2014
@author 	Zack Garza <dzackgarza@gmail.com>i
"""

a = int(input("What is the length of the first side? "))
b = int(input("What is the length of the second side? "))
c = int(input("What is the length of the third side? "))

s = (1/2) * (a + b + c)

radicand = s * (s-a) * (s-b) * (s-c)

A = pow(radicand, 1/2)

print(A)
