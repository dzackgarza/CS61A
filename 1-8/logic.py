'''
Logic Comparator - determines if two functions have the same truth tables.
Author: Zack Garza
'''

def LogicComparator(p, q):
	truth = [True, False]

	for i in range(0,2):
		for j in range (0,2):
			t1, t2 = truth[i], truth[j];

			if (p(t1,t2) != q(t1,t2)):
				return False;

	return True;

def dm1(p,q):
	return not(p and q);

def dm2(p,q):
	return (not p) or (not q);

def dm3(p,q):
	return not (p or q);

def dm4(p,q):
	return (not p) and (not q);

print("Identity 1: " + str(LogicComparator(dm1, dm2)));
print("Identity 2: " + str(LogicComparator(dm3, dm4)));
