'''
CS61A, Laney College
Author: Zack Garza
'''

def sumSeries(n):
	sum = 0;
	for i in range(0,n):
		term = 1 / (2**(i+1));
		sum += term;
	return sum;

for n in range(0,500):
	print("Summing n = " + str(n));
	sum = sumSeries(n);
	print(str(sum))
	if sum >= 1:
		print("Sum converges to 1 at n = " + str(n))
		break;

print("Sum at 100k: " + str(sumSeries(100000)))
for i in {10, 50, 53, 54, 100}:
	print("Sum at " +str(i)+ " = " + str(str(sumSeries(i))))
