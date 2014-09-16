'''
CS61A, Laney College
Author: Zack Garza
'''
from math import *

degrees, minutes, seconds = {}, {}, {}

def calcTriangle(degrees, minutes, seconds):	
	d_sum, m_sum, s_sum = 0, 0, 0
	for i in range(0,3):

		s_sum += seconds[i] % 60;
		m_sum += floor(seconds[i]/60)

		m_sum += minutes[i] % 60	
		d_sum += floor(minutes[i] / 60)
		
		d_sum += m_sum % 60
		m_sum = floor(m_sum / 60)

		d_sum += degrees[i]

	print(str(d_sum) + ":" + str(m_sum) + ":" + str(s_sum) + ".")
	#printf("DMS: %d:%d:%d", d_sum, m_sum, s_sum);
	if d_sum == 180 and m_sum == 0 and s_sum == 0:
		print("This is a Euclidean triangle.")
	elif d_sum > 180:
		print("This is an elliptical triangle.")
	else:
		print("This is a hyperbolic triangle.")

for i in range(0,3):
	print("Enter angle " + str(i+1));
	degrees[i] = int(input("Degrees: "));
	minutes[i] = int(input("Minutes: "));
	seconds[i] = int(input("Seconds: "));
calcTriangle(degrees, minutes, seconds);

test1 = [[29, 0, 30], [60, 15, 30], [90, 44, 0]]
calcTriangle(test1[0], test1[1], test1[2]);

test2 = [[59, 59, 59], [59, 59, 59], [59, 59, 59]]
calcTriangle(test2[0], test2[1], test2[2]);

test3 = [[45, 59, 59], [45, 59, 59], [88, 0, 2]]
calcTriangle(test3[0], test3[1], test3[2]);
